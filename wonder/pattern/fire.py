from wonder.layout.cube import Cube
from wonder.layout.face import Face
from wonder.layout.pixel import Pixel

from wonder.utils import color_utils

import time
import random


class Fire:
    start_time = 0
    layout = None

    max_value = 1.0

    gas_max_hue = 40.0/360
    embers_max_hue = 60.0/360

    vary_max = 0.05

    def __init__(self, host=None):
        self.layout = Cube(host)
        self.start_time = time.time()

        self.seed_gas_hue()

    def seed_gas_hue(self):
        for face_idx in range(Cube.NUM_FACES):
            for pixel_idx in range(Face.NUM_PIXELS):
                pixel = self.layout.get_pixel(face_idx, pixel_idx)
                hue = self.gas_max_hue * random.random()
                saturation = self.get_min_saturation(hue)
                pixel.set_hue(hue)
                pixel.set_saturation(saturation)
                pixel.set_value(self.max_value)
                pixel.update_rgb_from_hsv()

        self.layout.write_pixels()

    # The closer to red, the less range of saturation we should have with red
    # having zero range, returning a min saturation of 1.0, e.g. it will always
    # have a saturation of 1.0.  Yellow on the other hand (the embers_max_hue value)
    # will have a min saturation of 0.0, e.g. it can have any saturation between 0 and 1
    def get_min_saturation(self, hue):
        return 1.0 - (hue/self.embers_max_hue)

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
                hue = pixel.hue
                saturation = pixel.saturation

                adjacents = pixel.get_adjacent_pixels()
                average_hue = (hue + adjacents[0].hue + adjacents[1].hue + adjacents[2].hue)/4.0
                average_saturation = (saturation + adjacents[0].saturation + adjacents[1].saturation + adjacents[2].saturation)/4.0

                # Perturb
                if random.random() < 0.5:
                    average_hue -= self.vary_max * random.random()
                else:
                    average_hue += self.vary_max * random.random()

                if random.random() < 0.5:
                    average_saturation -= self.vary_max * random.random()
                else:
                    average_saturation += self.vary_max * random.random()

                if average_hue > self.gas_max_hue:
                    average_hue = (2 * self.gas_max_hue) - average_hue

                if average_hue < 0:
                    average_hue *= -1

                if average_saturation > 1.0:
                    average_saturation = 2.0 - average_saturation

                if average_saturation < 0:
                    average_saturation *= -1

                pixel.set_hue(average_hue)
                pixel.set_saturation(average_saturation)
                pixel.set_value(self.max_value)

                pixel.update_rgb_from_hsv()

        self.layout.write_pixels()
