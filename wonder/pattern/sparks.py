from wonder.layout.cube import Cube
from wonder.layout.face import Face
from wonder.layout.pixel import Pixel

from wonder.utils import color_utils
from wonder.utils.corners import Corners

import time
import random


class Sparks:
    start_time = 0
    layout = None

    max_value = Pixel.MAX_HSV_VALUE

    fire_tracks = None
    ice_tracks = None
    num_tracks = None
    fire_sparks = None
    ice_sparks = None
    max_sparks = 20

    def __init__(self, host=None):
        Corners. gen_derived_corners()
        self.layout = Cube(host)
        self.start_time = time.time()
        self.fire_tracks = Corners.tracks[Corners.CORNER_0]
        self.ice_tracks = Corners.tracks[Corners.CORNER_6]
        self.num_tracks = len(self.fire_tracks)
        self.fire_sparks = []
        self.ice_sparks = []


    def set_brightness(self, pct):
        Sparks.max_value = color_utils.clamp(
            pct * Pixel.MAX_HSV_VALUE,
            0,
            Pixel.MAX_HSV_VALUE
        )

    def iterate(self):

        if len(self.fire_sparks) < self.max_sparks:
            track_num = random.randint(0, self.num_tracks-1)
            self.fire_sparks.append(Spark(self.layout, self.fire_tracks[track_num], 0.111111111, 0.0))

        if len(self.ice_sparks) < self.max_sparks:
            track_num = random.randint(0, self.num_tracks - 1)
            self.ice_sparks.append(Spark(self.layout, self.ice_tracks[track_num], 0.666666666, 0.5))

        remaining = []
        for spark in self.fire_sparks:
            # If our spark has died, stop tracking it
            if spark.update():
                remaining.append(spark)

        self.fire_sparks = remaining

        remaining = []
        for spark in self.ice_sparks:
            # If our spark has died, stop tracking it
            if spark.update():
                remaining.append(spark)

        self.ice_sparks = remaining

        self.layout.write_pixels()


class Spark:
    acceleration = -9.8
    velocity = None
    max_velocity = 40.0
    min_velocity = 18.0
    start = None

    track = None
    position = None
    layout = None

    decay = False
    decay_start = None
    decay_value = None

    start_hue = None

    max_hue = None  # 0.11111111111
    min_hue = None

    # A percentage
    decay_hue = 0.99

    tracked_pixels = None

    def __init__(self, layout, track, max_hue, min_hue):
        self.layout = layout
        self.track = track
        self.start = time.time()

        heat = random.random()
        self.max_hue = max_hue
        self.min_hue = min_hue
        self.start_hue = min_hue + ((max_hue-min_hue) * heat)
        self.velocity = self.min_velocity + ((self.max_velocity-self.min_velocity) * heat)
        self.tracked_pixels = {}

    def init_pixel(self, pixel):
        pixel.value = Sparks.max_value
        pixel.hue = self.start_hue
        pixel.saturation = 1.0
        pixel.update_rgb_from_hsv()

    def update(self):
        if self.position is None:
            self.position = 0.0
            new_pixel = self.get_current_pixel()
            self.init_pixel(new_pixel)
            return True

        old_pixel = self.get_current_pixel()
        old_pixel_value = old_pixel.value
        if old_pixel.context == self:
            old_pixel.value = 0.0
            old_pixel.update_rgb_from_hsv()

        old_position = self.position

        elapsed = time.time() - self.start
        self.position = (self.velocity * elapsed) + (2 * self.acceleration * (elapsed**2))

        if (self.position < old_position) and not self.decay:
            self.decay = True
            self.decay_start = time.time()
            self.decay_value = old_pixel_value

        # See if we're at the end of the track yet
        if self.position >= len(self.track):
            return None

        if self.position <= 0:
            return None

        new_pixel = self.get_current_pixel()
        new_pixel.value = old_pixel_value
        new_pixel.hue = self.min_hue + ((old_pixel.hue - self.min_hue) * self.decay_hue)
        new_pixel.saturation = old_pixel.saturation
        new_pixel.context = self

        if self.decay:
            new_pixel.value = self.decay_value * (1 - (time.time()-self.decay_start)/(0.5*(self.decay_start-self.start)))

        if new_pixel.value < 0:
            return None

        new_pixel.update_rgb_from_hsv()

        return True

    def get_current_pixel(self):
        pair = self.track[int(self.position)]
        return self.layout.get_pixel(pair[0], pair[1])
