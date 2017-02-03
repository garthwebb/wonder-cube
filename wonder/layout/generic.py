from wonder.utils.opc import Client


class Generic:
    NUM_PIXELS = 36*6*2

    pixels = []

    def __init__(self, host="localhost:7890"):
        print("Connecting to host at {:s}".format(host))
        self.client = Client(host)

    def clear_pixels(self):
        self.pixels = []

    def add_pixel(self, rgb_tuple):
        self.pixels.append(rgb_tuple)

    def write_pixels(self):
        self.client.put_pixels(self.pixels, channel=0)
