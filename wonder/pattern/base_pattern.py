from wonder.layout.cube import Cube
from wonder.layout.face import Face
from wonder.layout.pixel import Pixel

from wonder.utils import color_utils

import time


class BasePattern:
    start_time = 0
    layout = None

    max_value = Pixel.MAX_HSV_VALUE

    def __init__(self, host=None):
        self.layout = Cube(host)
        self.start_time = time.time()

    def set_brightness(self, pct):
        self.max_value = color_utils.clamp(
            pct * Pixel.MAX_HSV_VALUE,
            0,
            Pixel.MAX_HSV_VALUE
        )

    def iterate(self):

        for face_idx in range(Cube.NUM_FACES):
            for pixel_idx in range(Face.NUM_PIXELS):
                pixel = self.layout.get_pixel(face_idx, pixel_idx)

        self.layout.write_pixels()