from wonder.layout.face import Face


class Adjacent:

    adjacent = [
        # Face FRONT
        [
            [[Face.BOTTOM, 26], [Face.FRONT, 35], [Face.FRONT, 1]],
            [[Face.BOTTOM, 25], [Face.FRONT, 0], [Face.FRONT, 2]],
            [[Face.BOTTOM, 24], [Face.FRONT, 1], [Face.FRONT, 3]],
            [[Face.BOTTOM, 23], [Face.FRONT, 2], [Face.FRONT, 4]],
            [[Face.BOTTOM, 22], [Face.FRONT, 3], [Face.FRONT, 5]],
            [[Face.BOTTOM, 21], [Face.FRONT, 4], [Face.FRONT, 6]],
            [[Face.BOTTOM, 20], [Face.FRONT, 5], [Face.FRONT, 7]],
            [[Face.BOTTOM, 19], [Face.FRONT, 6], [Face.FRONT, 8]],
            [[Face.BOTTOM, 18], [Face.FRONT, 7], [Face.FRONT, 9]],
            [[Face.LEFT, 35], [Face.FRONT, 8], [Face.FRONT, 10]],
            [[Face.LEFT, 34], [Face.FRONT, 9], [Face.FRONT, 11]],
            [[Face.LEFT, 33], [Face.FRONT, 10], [Face.FRONT, 12]],
            [[Face.LEFT, 32], [Face.FRONT, 11], [Face.FRONT, 13]],
            [[Face.LEFT, 31], [Face.FRONT, 12], [Face.FRONT, 14]],
            [[Face.LEFT, 30], [Face.FRONT, 13], [Face.FRONT, 15]],
            [[Face.LEFT, 29], [Face.FRONT, 14], [Face.FRONT, 16]],
            [[Face.LEFT, 28], [Face.FRONT, 15], [Face.FRONT, 17]],
            [[Face.LEFT, 27], [Face.FRONT, 16], [Face.FRONT, 18]],
            [[Face.TOP, 8], [Face.FRONT, 17], [Face.FRONT, 19]],
            [[Face.TOP, 7], [Face.FRONT, 18], [Face.FRONT, 20]],
            [[Face.TOP, 6], [Face.FRONT, 19], [Face.FRONT, 21]],
            [[Face.TOP, 5], [Face.FRONT, 20], [Face.FRONT, 22]],
            [[Face.TOP, 4], [Face.FRONT, 21], [Face.FRONT, 23]],
            [[Face.TOP, 3], [Face.FRONT, 22], [Face.FRONT, 24]],
            [[Face.TOP, 2], [Face.FRONT, 23], [Face.FRONT, 25]],
            [[Face.TOP, 1], [Face.FRONT, 24], [Face.FRONT, 26]],
            [[Face.TOP, 0], [Face.FRONT, 25], [Face.FRONT, 27]],
            [[Face.RIGHT, 17], [Face.FRONT, 26], [Face.FRONT, 28]],
            [[Face.RIGHT, 16], [Face.FRONT, 27], [Face.FRONT, 29]],
            [[Face.RIGHT, 15], [Face.FRONT, 28], [Face.FRONT, 30]],
            [[Face.RIGHT, 14], [Face.FRONT, 29], [Face.FRONT, 31]],
            [[Face.RIGHT, 13], [Face.FRONT, 30], [Face.FRONT, 32]],
            [[Face.RIGHT, 12], [Face.FRONT, 31], [Face.FRONT, 33]],
            [[Face.RIGHT, 11], [Face.FRONT, 32], [Face.FRONT, 34]],
            [[Face.RIGHT, 10], [Face.FRONT, 33], [Face.FRONT, 35]],
            [[Face.RIGHT, 9], [Face.FRONT, 34], [Face.FRONT, 0]],
        ],
        # Face BACK
        [
            [[Face.BOTTOM, 8], [Face.BACK, 35], [Face.BACK, 1]],
            [[Face.BOTTOM, 7], [Face.BACK, 0], [Face.BACK, 2]],
            [[Face.BOTTOM, 6], [Face.BACK, 1], [Face.BACK, 3]],
            [[Face.BOTTOM, 5], [Face.BACK, 2], [Face.BACK, 4]],
            [[Face.BOTTOM, 4], [Face.BACK, 3], [Face.BACK, 5]],
            [[Face.BOTTOM, 3], [Face.BACK, 4], [Face.BACK, 6]],
            [[Face.BOTTOM, 2], [Face.BACK, 5], [Face.BACK, 7]],
            [[Face.BOTTOM, 1], [Face.BACK, 6], [Face.BACK, 8]],
            [[Face.BOTTOM, 0], [Face.BACK, 7], [Face.BACK, 9]],
            [[Face.RIGHT, 35], [Face.BACK, 8], [Face.BACK, 10]],
            [[Face.RIGHT, 34], [Face.BACK, 9], [Face.BACK, 11]],
            [[Face.RIGHT, 33], [Face.BACK, 10], [Face.BACK, 12]],
            [[Face.RIGHT, 32], [Face.BACK, 11], [Face.BACK, 13]],
            [[Face.RIGHT, 31], [Face.BACK, 12], [Face.BACK, 14]],
            [[Face.RIGHT, 30], [Face.BACK, 13], [Face.BACK, 15]],
            [[Face.RIGHT, 29], [Face.BACK, 14], [Face.BACK, 16]],
            [[Face.RIGHT, 28], [Face.BACK, 15], [Face.BACK, 17]],
            [[Face.RIGHT, 27], [Face.BACK, 16], [Face.BACK, 18]],
            [[Face.TOP, 26], [Face.BACK, 17], [Face.BACK, 19]],
            [[Face.TOP, 25], [Face.BACK, 18], [Face.BACK, 20]],
            [[Face.TOP, 24], [Face.BACK, 19], [Face.BACK, 21]],
            [[Face.TOP, 23], [Face.BACK, 20], [Face.BACK, 22]],
            [[Face.TOP, 22], [Face.BACK, 21], [Face.BACK, 23]],
            [[Face.TOP, 21], [Face.BACK, 22], [Face.BACK, 24]],
            [[Face.TOP, 20], [Face.BACK, 23], [Face.BACK, 25]],
            [[Face.TOP, 19], [Face.BACK, 24], [Face.BACK, 26]],
            [[Face.TOP, 18], [Face.BACK, 25], [Face.BACK, 27]],
            [[Face.LEFT, 17], [Face.BACK, 26], [Face.BACK, 28]],
            [[Face.LEFT, 16], [Face.BACK, 27], [Face.BACK, 29]],
            [[Face.LEFT, 15], [Face.BACK, 28], [Face.BACK, 30]],
            [[Face.LEFT, 14], [Face.BACK, 29], [Face.BACK, 31]],
            [[Face.LEFT, 13], [Face.BACK, 30], [Face.BACK, 32]],
            [[Face.LEFT, 12], [Face.BACK, 31], [Face.BACK, 33]],
            [[Face.LEFT, 11], [Face.BACK, 32], [Face.BACK, 34]],
            [[Face.LEFT, 10], [Face.BACK, 33], [Face.BACK, 35]],
            [[Face.LEFT, 9], [Face.BACK, 34], [Face.BACK, 0]],
        ],
        # Face LEFT
        [
            [[Face.BOTTOM, 17], [Face.LEFT, 35], [Face.LEFT, 1]],
            [[Face.BOTTOM, 16], [Face.LEFT, 0], [Face.LEFT, 2]],
            [[Face.BOTTOM, 15], [Face.LEFT, 1], [Face.LEFT, 3]],
            [[Face.BOTTOM, 14], [Face.LEFT, 2], [Face.LEFT, 4]],
            [[Face.BOTTOM, 13], [Face.LEFT, 3], [Face.LEFT, 5]],
            [[Face.BOTTOM, 12], [Face.LEFT, 4], [Face.LEFT, 6]],
            [[Face.BOTTOM, 11], [Face.LEFT, 5], [Face.LEFT, 7]],
            [[Face.BOTTOM, 10], [Face.LEFT, 6], [Face.LEFT, 8]],
            [[Face.BOTTOM, 9], [Face.LEFT, 7], [Face.LEFT, 9]],
            [[Face.BACK, 35], [Face.LEFT, 8], [Face.LEFT, 10]],
            [[Face.BACK, 34], [Face.LEFT, 9], [Face.LEFT, 11]],
            [[Face.BACK, 33], [Face.LEFT, 10], [Face.LEFT, 12]],
            [[Face.BACK, 32], [Face.LEFT, 11], [Face.LEFT, 13]],
            [[Face.BACK, 31], [Face.LEFT, 12], [Face.LEFT, 14]],
            [[Face.BACK, 30], [Face.LEFT, 13], [Face.LEFT, 15]],
            [[Face.BACK, 29], [Face.LEFT, 14], [Face.LEFT, 16]],
            [[Face.BACK, 28], [Face.LEFT, 15], [Face.LEFT, 17]],
            [[Face.BACK, 27], [Face.LEFT, 16], [Face.LEFT, 18]],
            [[Face.TOP, 17], [Face.LEFT, 17], [Face.LEFT, 19]],
            [[Face.TOP, 16], [Face.LEFT, 18], [Face.LEFT, 20]],
            [[Face.TOP, 15], [Face.LEFT, 19], [Face.LEFT, 21]],
            [[Face.TOP, 14], [Face.LEFT, 20], [Face.LEFT, 22]],
            [[Face.TOP, 13], [Face.LEFT, 21], [Face.LEFT, 23]],
            [[Face.TOP, 12], [Face.LEFT, 22], [Face.LEFT, 24]],
            [[Face.TOP, 11], [Face.LEFT, 23], [Face.LEFT, 25]],
            [[Face.TOP, 10], [Face.LEFT, 24], [Face.LEFT, 26]],
            [[Face.TOP, 9], [Face.LEFT, 25], [Face.LEFT, 27]],
            [[Face.FRONT, 17], [Face.LEFT, 26], [Face.LEFT, 28]],
            [[Face.FRONT, 16], [Face.LEFT, 27], [Face.LEFT, 29]],
            [[Face.FRONT, 15], [Face.LEFT, 28], [Face.LEFT, 30]],
            [[Face.FRONT, 14], [Face.LEFT, 29], [Face.LEFT, 31]],
            [[Face.FRONT, 13], [Face.LEFT, 30], [Face.LEFT, 32]],
            [[Face.FRONT, 12], [Face.LEFT, 31], [Face.LEFT, 33]],
            [[Face.FRONT, 11], [Face.LEFT, 32], [Face.LEFT, 34]],
            [[Face.FRONT, 10], [Face.LEFT, 33], [Face.LEFT, 35]],
            [[Face.FRONT, 9], [Face.LEFT, 34], [Face.LEFT, 0]],
        ],
        # Face RIGHT
        [
            [[Face.BOTTOM, 35], [Face.RIGHT, 35], [Face.RIGHT, 1]],
            [[Face.BOTTOM, 34], [Face.RIGHT, 0], [Face.RIGHT, 2]],
            [[Face.BOTTOM, 33], [Face.RIGHT, 1], [Face.RIGHT, 3]],
            [[Face.BOTTOM, 32], [Face.RIGHT, 2], [Face.RIGHT, 4]],
            [[Face.BOTTOM, 31], [Face.RIGHT, 3], [Face.RIGHT, 5]],
            [[Face.BOTTOM, 30], [Face.RIGHT, 4], [Face.RIGHT, 6]],
            [[Face.BOTTOM, 29], [Face.RIGHT, 5], [Face.RIGHT, 7]],
            [[Face.BOTTOM, 28], [Face.RIGHT, 6], [Face.RIGHT, 8]],
            [[Face.BOTTOM, 27], [Face.RIGHT, 7], [Face.RIGHT, 9]],
            [[Face.FRONT, 35], [Face.RIGHT, 8], [Face.RIGHT, 10]],
            [[Face.FRONT, 34], [Face.RIGHT, 9], [Face.RIGHT, 11]],
            [[Face.FRONT, 33], [Face.RIGHT, 10], [Face.RIGHT, 12]],
            [[Face.FRONT, 32], [Face.RIGHT, 11], [Face.RIGHT, 13]],
            [[Face.FRONT, 31], [Face.RIGHT, 12], [Face.RIGHT, 14]],
            [[Face.FRONT, 30], [Face.RIGHT, 13], [Face.RIGHT, 15]],
            [[Face.FRONT, 29], [Face.RIGHT, 14], [Face.RIGHT, 16]],
            [[Face.FRONT, 28], [Face.RIGHT, 15], [Face.RIGHT, 17]],
            [[Face.FRONT, 27], [Face.RIGHT, 16], [Face.RIGHT, 18]],
            [[Face.TOP, 35], [Face.RIGHT, 17], [Face.RIGHT, 19]],
            [[Face.TOP, 34], [Face.RIGHT, 18], [Face.RIGHT, 20]],
            [[Face.TOP, 33], [Face.RIGHT, 19], [Face.RIGHT, 21]],
            [[Face.TOP, 32], [Face.RIGHT, 20], [Face.RIGHT, 22]],
            [[Face.TOP, 31], [Face.RIGHT, 21], [Face.RIGHT, 23]],
            [[Face.TOP, 30], [Face.RIGHT, 22], [Face.RIGHT, 24]],
            [[Face.TOP, 29], [Face.RIGHT, 23], [Face.RIGHT, 25]],
            [[Face.TOP, 28], [Face.RIGHT, 24], [Face.RIGHT, 26]],
            [[Face.TOP, 27], [Face.RIGHT, 25], [Face.RIGHT, 27]],
            [[Face.BACK, 17], [Face.RIGHT, 26], [Face.RIGHT, 28]],
            [[Face.BACK, 16], [Face.RIGHT, 27], [Face.RIGHT, 29]],
            [[Face.BACK, 15], [Face.RIGHT, 28], [Face.RIGHT, 30]],
            [[Face.BACK, 14], [Face.RIGHT, 29], [Face.RIGHT, 31]],
            [[Face.BACK, 13], [Face.RIGHT, 30], [Face.RIGHT, 32]],
            [[Face.BACK, 12], [Face.RIGHT, 31], [Face.RIGHT, 33]],
            [[Face.BACK, 11], [Face.RIGHT, 32], [Face.RIGHT, 34]],
            [[Face.BACK, 10], [Face.RIGHT, 33], [Face.RIGHT, 35]],
            [[Face.BACK, 9], [Face.RIGHT, 34], [Face.RIGHT, 0]],
        ],
        # Face TOP
        [
            [[Face.FRONT, 26], [Face.TOP, 35], [Face.TOP, 1]],
            [[Face.FRONT, 25], [Face.TOP, 0], [Face.TOP, 2]],
            [[Face.FRONT, 24], [Face.TOP, 1], [Face.TOP, 3]],
            [[Face.FRONT, 23], [Face.TOP, 2], [Face.TOP, 4]],
            [[Face.FRONT, 22], [Face.TOP, 3], [Face.TOP, 5]],
            [[Face.FRONT, 21], [Face.TOP, 4], [Face.TOP, 6]],
            [[Face.FRONT, 20], [Face.TOP, 5], [Face.TOP, 7]],
            [[Face.FRONT, 19], [Face.TOP, 6], [Face.TOP, 8]],
            [[Face.FRONT, 18], [Face.TOP, 7], [Face.TOP, 9]],
            [[Face.LEFT, 26], [Face.TOP, 8], [Face.TOP, 10]],
            [[Face.LEFT, 25], [Face.TOP, 9], [Face.TOP, 11]],
            [[Face.LEFT, 24], [Face.TOP, 10], [Face.TOP, 12]],
            [[Face.LEFT, 23], [Face.TOP, 11], [Face.TOP, 13]],
            [[Face.LEFT, 22], [Face.TOP, 12], [Face.TOP, 14]],
            [[Face.LEFT, 21], [Face.TOP, 13], [Face.TOP, 15]],
            [[Face.LEFT, 20], [Face.TOP, 14], [Face.TOP, 16]],
            [[Face.LEFT, 19], [Face.TOP, 15], [Face.TOP, 17]],
            [[Face.LEFT, 18], [Face.TOP, 16], [Face.TOP, 18]],
            [[Face.BACK, 26], [Face.TOP, 17], [Face.TOP, 19]],
            [[Face.BACK, 25], [Face.TOP, 18], [Face.TOP, 20]],
            [[Face.BACK, 24], [Face.TOP, 19], [Face.TOP, 21]],
            [[Face.BACK, 23], [Face.TOP, 20], [Face.TOP, 22]],
            [[Face.BACK, 22], [Face.TOP, 21], [Face.TOP, 23]],
            [[Face.BACK, 21], [Face.TOP, 22], [Face.TOP, 24]],
            [[Face.BACK, 20], [Face.TOP, 23], [Face.TOP, 25]],
            [[Face.BACK, 19], [Face.TOP, 24], [Face.TOP, 26]],
            [[Face.BACK, 18], [Face.TOP, 25], [Face.TOP, 27]],
            [[Face.RIGHT, 26], [Face.TOP, 26], [Face.TOP, 28]],
            [[Face.RIGHT, 25], [Face.TOP, 27], [Face.TOP, 29]],
            [[Face.RIGHT, 24], [Face.TOP, 28], [Face.TOP, 30]],
            [[Face.RIGHT, 23], [Face.TOP, 29], [Face.TOP, 31]],
            [[Face.RIGHT, 22], [Face.TOP, 30], [Face.TOP, 32]],
            [[Face.RIGHT, 21], [Face.TOP, 31], [Face.TOP, 33]],
            [[Face.RIGHT, 20], [Face.TOP, 32], [Face.TOP, 34]],
            [[Face.RIGHT, 19], [Face.TOP, 33], [Face.TOP, 35]],
            [[Face.RIGHT, 18], [Face.TOP, 34], [Face.TOP, 0]],
        ],
        # Face BOTTOM
        [
            [[Face.BACK, 8], [Face.BOTTOM, 35], [Face.BOTTOM, 1]],
            [[Face.BACK, 7], [Face.BOTTOM, 0], [Face.BOTTOM, 2]],
            [[Face.BACK, 6], [Face.BOTTOM, 1], [Face.BOTTOM, 3]],
            [[Face.BACK, 5], [Face.BOTTOM, 2], [Face.BOTTOM, 4]],
            [[Face.BACK, 4], [Face.BOTTOM, 3], [Face.BOTTOM, 5]],
            [[Face.BACK, 3], [Face.BOTTOM, 4], [Face.BOTTOM, 6]],
            [[Face.BACK, 2], [Face.BOTTOM, 5], [Face.BOTTOM, 7]],
            [[Face.BACK, 1], [Face.BOTTOM, 6], [Face.BOTTOM, 8]],
            [[Face.BACK, 0], [Face.BOTTOM, 7], [Face.BOTTOM, 9]],
            [[Face.LEFT, 8], [Face.BOTTOM, 8], [Face.BOTTOM, 10]],
            [[Face.LEFT, 7], [Face.BOTTOM, 9], [Face.BOTTOM, 11]],
            [[Face.LEFT, 6], [Face.BOTTOM, 10], [Face.BOTTOM, 12]],
            [[Face.LEFT, 5], [Face.BOTTOM, 11], [Face.BOTTOM, 13]],
            [[Face.LEFT, 4], [Face.BOTTOM, 12], [Face.BOTTOM, 14]],
            [[Face.LEFT, 3], [Face.BOTTOM, 13], [Face.BOTTOM, 15]],
            [[Face.LEFT, 2], [Face.BOTTOM, 14], [Face.BOTTOM, 16]],
            [[Face.LEFT, 1], [Face.BOTTOM, 15], [Face.BOTTOM, 17]],
            [[Face.LEFT, 0], [Face.BOTTOM, 16], [Face.BOTTOM, 18]],
            [[Face.FRONT, 8], [Face.BOTTOM, 17], [Face.BOTTOM, 19]],
            [[Face.FRONT, 7], [Face.BOTTOM, 18], [Face.BOTTOM, 20]],
            [[Face.FRONT, 6], [Face.BOTTOM, 19], [Face.BOTTOM, 21]],
            [[Face.FRONT, 5], [Face.BOTTOM, 20], [Face.BOTTOM, 22]],
            [[Face.FRONT, 4], [Face.BOTTOM, 21], [Face.BOTTOM, 23]],
            [[Face.FRONT, 3], [Face.BOTTOM, 22], [Face.BOTTOM, 24]],
            [[Face.FRONT, 2], [Face.BOTTOM, 23], [Face.BOTTOM, 25]],
            [[Face.FRONT, 1], [Face.BOTTOM, 24], [Face.BOTTOM, 26]],
            [[Face.FRONT, 0], [Face.BOTTOM, 25], [Face.BOTTOM, 27]],
            [[Face.RIGHT, 8], [Face.BOTTOM, 26], [Face.BOTTOM, 28]],
            [[Face.RIGHT, 7], [Face.BOTTOM, 27], [Face.BOTTOM, 29]],
            [[Face.RIGHT, 6], [Face.BOTTOM, 28], [Face.BOTTOM, 30]],
            [[Face.RIGHT, 5], [Face.BOTTOM, 29], [Face.BOTTOM, 31]],
            [[Face.RIGHT, 4], [Face.BOTTOM, 30], [Face.BOTTOM, 32]],
            [[Face.RIGHT, 3], [Face.BOTTOM, 31], [Face.BOTTOM, 33]],
            [[Face.RIGHT, 2], [Face.BOTTOM, 32], [Face.BOTTOM, 34]],
            [[Face.RIGHT, 1], [Face.BOTTOM, 33], [Face.BOTTOM, 35]],
            [[Face.RIGHT, 0], [Face.BOTTOM, 34], [Face.BOTTOM, 0]],
        ],
    ]

    def __init__(self):
        None

    @staticmethod
    def get_near(face_idx, pixel_idx):
        return Adjacent.adjacent[face_idx][pixel_idx][0]

    @staticmethod
    def get_near_face(face_idx, pixel_idx):
        return Adjacent.adjacent[face_idx][pixel_idx][0][0]

    @staticmethod
    def get_near_idx(face_idx, pixel_idx):
        return Adjacent.adjacent[face_idx][pixel_idx][0][1]

    @staticmethod
    def get_behind(face_idx, pixel_idx):
        return Adjacent.adjacent[face_idx][pixel_idx][1]

    @staticmethod
    def get_behind_face(face_idx, pixel_idx):
        return Adjacent.adjacent[face_idx][pixel_idx][1][0]

    @staticmethod
    def get_behind_idx(face_idx, pixel_idx):
        return Adjacent.adjacent[face_idx][pixel_idx][1][1]

    @staticmethod
    def get_ahead(face_idx, pixel_idx):
        return Adjacent.adjacent[face_idx][pixel_idx][2]

    @staticmethod
    def get_ahead_face(face_idx, pixel_idx):
        return Adjacent.adjacent[face_idx][pixel_idx][2][0]

    @staticmethod
    def get_ahead_idx(face_idx, pixel_idx):
        return Adjacent.adjacent[face_idx][pixel_idx][2][1]
