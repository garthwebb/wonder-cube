from wonder.layout.pixel import Pixel


class Face:
    NUM_PIXELS = 36

    # Enum for faces
    FRONT = 0
    BACK = 1
    LEFT = 2
    RIGHT = 3
    TOP = 4
    BOTTOM = 5

    face_names = [
        'front',
        'back',
        'left',
        'right',
        'top',
        'bottom'
    ]

    face_names_abbreviated = [
        'f',
        'b',
        'l',
        'r',
        't',
        'o'
    ]

    # Formally define the pixels of each side of the face
    sides = [
        [i for i in range(0, 9)],
        [i for i in range(9, 18)],
        [i for i in range(18, 27)],
        [i for i in range(27, 36)],
    ]

    mapping = [
        # Front
        {
            'channel': 2,
            'pixels': [
                0, 1, 2, 3, 4, 5, 6, 7, 8,
                9, 10, 11, 12, 13, 14, 15, 16, 17,
                18, 19, 20, 21, 22, 23, 24, 25, 26,
                27, 28, 29, 30, 31, 32, 33, 34, 35,
            ]
        },
        # Back
        {
            'channel': 4,
            'pixels': [
                27, 28, 29, 30, 31, 32, 33, 34, 35,
                0, 1, 2, 3, 4, 5, 6, 7, 8,
                9, 10, 11, 12, 13, 14, 15, 16, 17,
                18, 19, 20, 21, 22, 23, 24, 25, 26,
            ]
        },
        # Left
        {
            'channel': 5,
            'pixels': [
                0, 1, 2, 3, 4, 5, 6, 7, 8,
                9, 10, 11, 12, 13, 14, 15, 16, 17,
                18, 19, 20, 21, 22, 23, 24, 25, 26,
                27, 28, 29, 30, 31, 32, 33, 34, 35,
            ]
        },
        # Right
        {
            'channel': 3,
            'pixels': [
                27, 28, 29, 30, 31, 32, 33, 34, 35,
                0, 1, 2, 3, 4, 5, 6, 7, 8,
                9, 10, 11, 12, 13, 14, 15, 16, 17,
                18, 19, 20, 21, 22, 23, 24, 25, 26,
            ]
        },
        # Top
        {
            'channel': 6,
            'pixels': [
                0, 1, 2, 3, 4, 5, 6, 7, 8,
                9, 10, 11, 12, 13, 14, 15, 16, 17,
                18, 19, 20, 21, 22, 23, 24, 25, 26,
                27, 28, 29, 30, 31, 32, 33, 34, 35,
            ]
        },
        # Bottom
        {
            'channel': 1,
            'pixels': [
                26, 25, 24, 23, 22, 21, 20, 19, 18,
                17, 16, 15, 14, 13, 12, 11, 10, 9,
                8, 7, 6, 5, 4, 3, 2, 1, 0,
                35, 34, 33, 32, 31, 30, 29, 28, 27,
            ]
        }
    ]

    # Which channel on the fadecandy to write data to (from "mapping" above)
    channel = None
    # Physical layout of pixels on faces (from "mapping" above)
    pixel_map = None

    # Array of pixel objects
    pixels = None
    # The RGB tuples generated from above "pixels" that should be written
    output_values = None

    all_values = None

    def __init__(self, face_idx, pixels = None):
        self.pixels = [None for p in range(self.NUM_PIXELS)]
        self.output_values = [None for p in range(self.NUM_PIXELS)]
        self.all_values = pixels

        self.pixel_map = self.mapping[face_idx]['pixels']
        self.channel = self.mapping[face_idx]['channel']

        for idx in range(self.NUM_PIXELS):
            new_pixel = Pixel()
            self.pixels[idx] = new_pixel

            # Get a reference to the rgb tuple from the above Pixel object
            mapped_idx = self.pixel_map[idx]
            self.output_values[mapped_idx] = new_pixel.get_rgb()

    # TODO: Make this suck less, probably by using python3 enums
    @staticmethod
    def to_face_idx(value):
        value = value.lower()
        for idx, name in enumerate(Face.face_names):
            if value == name:
                return idx

        for idx, name in enumerate(Face.face_names_abbreviated):
            if value == name:
                return idx

        return 0

    def get_pixel(self, idx):
        return self.pixels[idx]

    def clear(self):
        for idx in range(self.NUM_PIXELS):
            self.pixels[idx].clear()
