import colorsys


class Pixel:
    MAX_RGB_VALUE = 255
    MAX_HSV_VALUE = 1

    RED = 0
    GREEN = 1
    BLUE = 2

    rgb_tuple = None
    rgb_dirty = 0

    hue = 0
    saturation = 0
    value = 0
    hsv_dirty = 0

    # Store references to adjacent pixels
    adjacent = None

    context = None

    def __init__(self, red=0, green=0, blue=0):
        self.rgb_tuple = [0, 0, 0]
        self.set_rgb(red, green, blue)
        self.adjacent = []

    def clear(self):
        self.set_rgb(0, 0, 0)

    def add_adjacent_pixel(self, pixel):
        self.adjacent.append(pixel)

    def get_adjacent_pixels(self):
        return self.adjacent

    def normalize_rgb(self, value):
        if value > self.MAX_RGB_VALUE:
            value = self.MAX_RGB_VALUE
        if value < 0:
            value = 0

        return int(value)

    def normalize_hsv(self, value):
        if value > self.MAX_HSV_VALUE:
            value = self.MAX_HSV_VALUE
        if value < 0:
            value = 0

        return value

    def get_rgb(self):
        if self.rgb_dirty:
            self.update_rgb_from_hsv()

        return self.rgb_tuple

    def get_hsv(self):
        if self.hsv_dirty:
            self.update_hsv_from_rgb()

        return self.hue, self.saturation, self.value

    def update_rgb_from_hsv(self):
        """
        Update the RGB according to the HSV values
        :return:
        """
        (red, green, blue) = colorsys.hsv_to_rgb(self.hue, self.saturation, self.value)
        self.rgb_tuple[self.RED] = int(self.MAX_RGB_VALUE * red)
        self.rgb_tuple[self.GREEN] = int(self.MAX_RGB_VALUE * green)
        self.rgb_tuple[self.BLUE] = int(self.MAX_RGB_VALUE * blue)
        self.rgb_dirty = 0

    def update_hsv_from_rgb(self):
        """
        Update the HSV according to the RGB values
        :return:
        """
        (hue, saturation, value) = colorsys.rgb_to_hsv(
            self.rgb_tuple[self.RED],
            self.rgb_tuple[self.GREEN],
            self.rgb_tuple[self.BLUE]
        )
        self.hue = hue
        self.saturation = saturation
        self.value = value
        self.hsv_dirty = 0

    def set_rgb(self, red, green, blue):
        self.set_red(red)
        self.set_green(green)
        self.set_blue(blue)
        self.hsv_dirty = 1

    def set_red(self, value):
        self.rgb_tuple[self.RED] = self.normalize_rgb(value)
        self.hsv_dirty = 1

    def set_green(self, value):
        self.rgb_tuple[self.GREEN] = self.normalize_rgb(value)
        self.hsv_dirty = 1

    def set_blue(self, value):
        self.rgb_tuple[self.BLUE] = self.normalize_rgb(value)
        self.hsv_dirty = 1

    def get_red(self):
        return self.rgb_tuple[self.RED]

    def get_green(self):
        return self.rgb_tuple[self.GREEN]

    def get_blue(self):
        return self.rgb_tuple[self.BLUE]

    def set_hsv(self, hue, saturation, value):
        self.hue = hue
        self.saturation = saturation
        self.value = value
        self.rgb_dirty = 1

    def set_hue(self, value):
        self.hue = self.normalize_hsv(value)
        self.rgb_dirty = 1

    def incr_hue(self, step):
        hue = self.hue + step
        hue_int = int(hue)
        hue -= hue_int
        self.set_hue(hue)

    def decr_hue(self, step):
        self.set_hue(self.hue - step)

    def mult_hue(self, factor):
        self.set_hue(self.hue * factor)

    def set_saturation(self, value):
        self.saturation = self.normalize_hsv(value)
        self.rgb_dirty = 1

    def incr_saturation(self, step):
        self.set_saturation(self.saturation + step)

    def decr_saturation(self, step):
        self.set_saturation(self.saturation - step)

    def mult_saturation(self, factor):
        self.set_saturation(self.saturation * factor)

    def set_value(self, value):
        self.value = self.normalize_hsv(value)
        self.rgb_dirty = 1

    def incr_value(self, step):
        self.set_value(self.value + step)

    def decr_value(self, step):
        self.set_value(self.value - step)

    def mult_value(self, factor):
        self.set_value(self.value * factor)
