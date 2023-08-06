import socket

from .constants import Command, CommandFlag, MonoEffect
from .utils import clamp
from .WifiLedShopLightState import WifiLedShopLightState


class WifiLedShopLight:
    """
    A Wifi LED Shop Light
    """

    def __init__(self, ip, port=8189, timeout=5, retries=5):
        """
        Creates a new Wifi LED Shop light

        :param ip: The IP of the controller on the network (STA Mode, not AP mode).
        :param port: The port the controller should listen on. It should almost always be left as the default.
        :param timeout: The timeout in seconds to wait listening to the socket.
        :param retries: The number of times to retry sending a command if it fails or times out before giving up.
        """
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.retries = retries
        self.state = WifiLedShopLightState()

        self.sock = None
        self.reconnect()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def reconnect(self):
        """
        Try to (re-)connect to the controller via a socket
        """
        if self.sock:
            self.close()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(self.timeout)
        self.sock.connect((self.ip, self.port))

    def close(self):
        """
        Closes the socket connection to the light
        """
        self.sock.close()
        self.sock = None

    def set_color(self, r=0, g=0, b=0):
        """
        Sets the color of the light (rgb each 0 to 255)
        """
        r = clamp(r)
        g = clamp(g)
        b = clamp(b)
        self.state.color = (r, g, b)
        self.send_command(Command.SET_COLOR, [int(r), int(g), int(b)])

    def set_brightness(self, brightness=0):
        """
        Sets the brightness of the light

        :param brightness: An int describing the brightness (0 to 255, where 255 is the brightest)
        """
        brightness = clamp(brightness)
        self.state.brightness = brightness
        self.send_command(Command.SET_BRIGHTNESS, [int(brightness)])

    def set_speed(self, speed=0):
        """
        Sets the speed of the effect. Not all effects use the speed, but it can be safely set regardless

        :param speed: An int describing the speed an effect will play at. (0 to 255, where 255 is the fastest)
        """
        speed = clamp(speed)
        self.state.speed = speed
        self.send_command(Command.SET_SPEED, [int(speed)])

    def set_preset(self, preset=0):
        """
        Sets the light effect to the provided built-in effect number

        :param preset: The preset effect to use. Valid values are 0 to 255. See the MonoEffect enum, or MONO_EFFECTS and PRESET_EFFECTS for mapping.
        """
        preset = clamp(preset)
        self.state.mode = preset
        self.send_command(Command.SET_PRESET, [int(preset)])

    def set_custom(self, custom):
        """
        Sets the light effect to the provided custom effect number

        :param custom: The custom effect to use. Valid values are 1 to 12. See the CustomEffect enum.
        """
        custom = clamp(custom, 1, 12)
        self.state.mode = custom
        self.send_command(Command.SET_CUSTOM, [int(custom)])

    def toggle(self):
        """
        Toggles the state of the light without checking the current state
        """
        self.state.is_on = not self.state.is_on
        self.send_command(Command.TOGGLE)

    def turn_on(self):
        """
        Toggles the light on only if it is not already on
        """
        if not self.state.is_on:
            self.toggle()

    def turn_off(self):
        """
        Toggles the light off only if it is not already off
        """
        if self.state.is_on:
            self.toggle()

    def set_segments(self, segments):
        """
        Sets the total number of segments. Total lights is segments * lights_per_segment.

        :param segments: The number of segments
        """
        self.send_command(Command.SET_SEGMENT_COUNT, [segments])

    def set_lights_per_segment(self, lights_per_segment):
        """
        Sets the number of lights per segment. Total lights is segments * lights_per_segment.

        :param lights_per_segment: The number of lights per segment
        """
        lights_per_segment_data = list(
            lights_per_segment.to_bytes(2, byteorder="little")
        )
        self.send_command(Command.SET_LIGHTS_PER_SEGMENT, lights_per_segment_data)

    def set_calculated_segments(self, total_lights, segments):
        """
        Helper function to automatically set the number of segments and lights per segment
        to reach the target total lights (rounded down to never exceed total_lights)

        Usually you know the total number of lights you have available on a light strip
        and want to split it into segments that take up the whole strip

        :param total_lights: The target total number of lights to use
        :param segments: The number of segments to split the total into
        """
        self.set_segments(segments)
        self.set_lights_per_segment(int(total_lights / segments))

    def send_command(self, command, data=[]):
        """
        Helper method to send a command to the controller.

        Mostly for internal use, prefer the specific functions where possible.

        Formats the low level message details like Start/End flag, binary data, and command

        :param command: The command to send to the controller. See the Command enum for valid commands.
        """
        min_data_len = 3
        padded_data = data + [0] * (min_data_len - len(data))
        raw_data = [CommandFlag.START, *padded_data, command, CommandFlag.END]
        self.send_bytes(raw_data)

    def send_bytes(self, data):
        """
        Helper method to send raw bytes directly to the controller

        Mostly for internal use, prefer the specific functions where possible
        """
        raw_data = bytes(data)

        attempts = 0
        while True:
            try:
                self.sock.sendall(raw_data)
                return
            except (socket.timeout, BrokenPipeError):
                if attempts < self.retries:
                    self.reconnect()
                    attempts += 1
                else:
                    raise

    def sync_state(self):
        """
        Syncs the state of the controller with the state of this object
        """
        attempts = 0
        while True:
            try:
                # Send the request for sync data
                self.send_command(Command.SYNC)

                response = self.sock.recv(1024)

                # Extract the state data
                state = bytearray(response)
                self.state.update_from_sync(state)
                return
            except (socket.timeout, BrokenPipeError):
                # When there is an error with the socket, close the connection and connect again
                if attempts < self.retries:
                    self.reconnect()
                    attempts += 1
                else:
                    raise

    def __repr__(self):
        return f"""WikiLedShopLight @ {self.ip}:{self.port}
      state: {self.state}
    """
