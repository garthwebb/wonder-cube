# Import the ADS1x15 module for doing the ADC
import Adafruit_ADS1x15


class Fader:
    BRIGHTNESS_CHANNEL = 0
    SPEED_CHANNEL = 1
    VOLUME_CHANNEL = 2

    # Max value returned by the adc call
    max_value = 1700.0
    address = 0x4a
    bus = 1
    gain = 0

    # Adjust the range returned by read_value to have this max value
    max_adjusted = None
    min_adjusted = 0
    range = 0

    # Which chanel (0-3) to read
    channel = None
    # Holds the Adafruit instance
    adc = None

    def __init__(self, channel, min=0.0, max=1.0):
        self.channel = channel
        self.min_adjusted = min
        self.max_adjusted = max

        self.range = max-min

        self.adc = Adafruit_ADS1x15.ADS1015(address=self.address, busnum=self.bus)

    def read_value(self):
        value = self.adc.read_adc(self.channel, gain=self.gain)
        value = (self.range*(value/self.max_value)) + self.min_adjusted

        if value > self.max_adjusted:
            value = self.max_adjusted

        if value < self.min_adjusted:
            value = self.min_adjusted

        return value
