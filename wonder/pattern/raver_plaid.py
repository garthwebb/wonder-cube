from __future__ import division

from wonder.layout.generic import Generic
from wonder.utils import color_utils

import time
import math


class RaverPlaid:
    layout = None

    start_time = 0

    # How many sine wave cycles are squeezed into our n_pixels
    # 24 happens to create nice diagonal stripes on the wall layout
    freq_r = 24
    freq_g = 24
    freq_b = 24

    # How many seconds the color sine waves take to shift through a complete cycle
    speed_r = 7
    speed_g = -13
    speed_b = 19

    brightness = 256
    max_brightness = 256

    def __init__(self, host=None):
        self.layout = Generic(host)
        self.start_time = time.time()

    def iterate(self):
        self.layout.clear_pixels()
        t = (time.time() - self.start_time) * 5

        for ii in range(self.layout.NUM_PIXELS):
            pct = (ii / self.layout.NUM_PIXELS)

            # diagonal black stripes
            pct_jittered = (pct * 77) % 37
            blackstripes = color_utils.cos(pct_jittered, offset=t * 0.05, period=1, minn=-1.5, maxx=1.5)
            blackstripes_offset = color_utils.cos(t, offset=0.9, period=60, minn=-0.5, maxx=3)
            blackstripes = color_utils.clamp(blackstripes + blackstripes_offset, 0, 1)

            # 3 sine waves for r, g, b which are out of sync with each other
            r = blackstripes * color_utils.remap(
                math.cos((t / self.speed_r + pct * self.freq_r) * math.pi * 2),
                -1, 1, 0, self.brightness
            )
            g = blackstripes * color_utils.remap(
                math.cos((t / self.speed_g + pct * self.freq_g) * math.pi * 2),
                -1, 1, 0, self.brightness
            )
            b = blackstripes * color_utils.remap(
                math.cos((t / self.speed_b + pct * self.freq_b) * math.pi * 2),
                -1, 1, 0, self.brightness
            )

            self.layout.add_pixel((r, g, b))

        self.layout.write_pixels()

    def set_brightness(self, pct):
        self.brightness = color_utils.clamp(pct * self.max_brightness, 0, self.max_brightness)
