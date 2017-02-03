import time

from wonder.controls.fader import Fader
from wonder.pattern.raver_plaid import RaverPlaid
from wonder.pattern.face_chase import FaceChase
from wonder.pattern.fire import Fire
from wonder.pattern.sparks import Sparks
from wonder.config import Config

import sys


class Core:
    brightness_channel = 0
    brightness_control = None
    brightness = None

    speed_channel = 1
    speed_control = None
    speed = None
    speed_max = 120
    speed_min = 10

    fader_poll_freq = 0.200
    last_fader_poll = None

    start = None
    delay = 1.0/24

    pattern = None

    tmp_count = 0

    def __init__(self, host=None):
        self.brightness_control = Fader(Fader.BRIGHTNESS_CHANNEL)
        self.speed_control = Fader(Fader.SPEED_CHANNEL, self.speed_min, self.speed_max)

        if host is None:
            host = Config.FADECANDY_HOST

        self.pattern = RaverPlaid(host)
#        self.pattern = FaceChase(host)
#        self.pattern = Fire(host)
#        self.pattern = Sparks(host)

    def run(self):
        while True:
            self.start = time.time()
            self.run_loop()
            # Sleep for however much time is left for our frame rate
            time.sleep(self.get_delay())

    def run_loop(self):
        self.pattern.iterate()

    def get_delay(self):
        self.check_faders()

        # If delay is positive return it, otherwise we're slower than our frame rate so
        # just return zero
        if self.delay > 0:
            return self.delay
        else:
            return 0

    def check_faders(self):
        if not self.time_to_poll:
            return

        self.check_speed_fader()
        self.check_brightness_fader()

    def check_speed_fader(self):
        fps = self.speed_control.read_value()

#        self.tmp_count = (self.tmp_count+1) % 100
#        if self.tmp_count == 0:
#            sys.stderr.write("Cur delay: {:f}\n".format(self.delay))
#            sys.stderr.write("GOT FPS: {:f}\n".format(fps))

        self.delay = (1.0/fps) - (time.time() - self.start)

    def check_brightness_fader(self):
        value = self.brightness_control.read_value()
        self.pattern.set_brightness(value)

    def time_to_poll(self):
        if not self.last_fader_poll:
            self.last_fader_poll = time.time()
            return True

        if time.time() - self.last_fader_poll > self.fader_poll_freq:
            self.last_fader_poll = time.time()
            return True

        return False
