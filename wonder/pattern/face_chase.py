from wonder.layout.cube import Cube
from wonder.layout.face import Face
from wonder.layout.pixel import Pixel

from wonder.utils import color_utils

import time


class FaceChase:
    start_time = 0
    layout = None

    cur_face = 0
    cur_pixel = 0

    dot_value = Pixel.MAX_HSV_VALUE
    dot_hue = Pixel.MAX_HSV_VALUE

    # Amount to dim each pixel per frame
    value_decr = .01

    hue_incr = 0.001

    def __init__(self, host=None):
        self.layout = Cube(host)
        self.start_time = time.time()

    def move_dot(self):
        self.cur_pixel = (self.cur_pixel+1) % 36

        if self.cur_pixel == 0:
            self.cur_face = (self.cur_face+1) % 6

        new_hue = self.dot_hue + self.hue_incr
        new_hue -= int(new_hue)
        self.dot_hue = new_hue

    def set_brightness(self, pct):
        self.dot_value = color_utils.clamp(
            pct * Pixel.MAX_HSV_VALUE,
            0,
            Pixel.MAX_HSV_VALUE
        )

    def iterate(self):

        for face_idx in range(Cube.NUM_FACES):
            for pixel_idx in range(Face.NUM_PIXELS):
                pixel = self.layout.get_pixel(face_idx, pixel_idx)

                if face_idx == self.cur_face and pixel_idx == self.cur_pixel:
                    pixel.set_hsv(self.dot_hue, Pixel.MAX_HSV_VALUE, self.dot_value)

                    adjacents = pixel.get_adjacent_pixels()
                    near_pixel = adjacents[0]
                    near_hue = self.dot_hue + 0.2
                    near_hue -= int(near_hue)

                    near_pixel.set_hsv(near_hue, Pixel.MAX_HSV_VALUE, self.dot_value)
                    near_pixel.update_rgb_from_hsv()
                else:
                    if pixel.value > 0:
                        pixel.decr_value(self.value_decr)
                pixel.update_rgb_from_hsv()

        self.move_dot()
        self.layout.write_pixels()
