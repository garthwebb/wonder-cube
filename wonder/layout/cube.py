from wonder.layout.face import Face
from wonder.utils.opc import Client
from wonder.utils.adjacency import Adjacent


class Cube:
    NUM_FACES = 6

    client = None
    faces = [None for f in range(NUM_FACES)]

    def __init__(self, host):
        self.client = Client(host)
        self.pixels = [[0, 0, 0] for p in range(self.NUM_FACES * Face.NUM_PIXELS)]
        self.init_pixels()
        self.set_adjacent()

    def init_pixels(self):
        for face_idx in range(self.NUM_FACES):
            self.faces[face_idx] = Face(face_idx, self.pixels)

    def set_adjacent(self):
        for face_idx in range(self.NUM_FACES):
            for pixel_idx in range(Face.NUM_PIXELS):
                pixel = self.get_pixel(face_idx, pixel_idx)

                near_face = Adjacent.get_near_face(face_idx, pixel_idx)
                near_idx = Adjacent.get_near_idx(face_idx, pixel_idx)
                pixel.add_adjacent_pixel(self.get_pixel(near_face, near_idx))

                behind_idx = Adjacent.get_behind_idx(face_idx, pixel_idx)
                pixel.add_adjacent_pixel(self.get_pixel(face_idx, behind_idx))

                ahead_idx = Adjacent.get_ahead_idx(face_idx, pixel_idx)
                pixel.add_adjacent_pixel(self.get_pixel(face_idx, ahead_idx))

    def clear(self):
        for face_idx in range(self.NUM_FACES):
            self.faces[face_idx].clear()

    def get_pixel(self, face_idx, pixel_idx):
        return self.faces[face_idx].get_pixel(pixel_idx)

    def write_pixels(self):
        for face_idx in range(self.NUM_FACES):
            channel = self.faces[face_idx].channel
            pixels = self.faces[face_idx].output_values

            self.client.put_pixels(pixels, channel=channel)
