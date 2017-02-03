from wonder.layout.face import Face

import sys

# Each face has four sides of LEDs, 0-8, 9-17, 18-26, 27-35
# This array links each face and side to its adjacent face and side for the purpose
# of code generating a mapping array to be used in the main program

# Enumerate the sides of a face
SIDE_0 = 0  # LEDs 0-8
SIDE_1 = 1  # LEDs 9-17
SIDE_2 = 2  # LEDs 18-26
SIDE_3 = 3  # LEDs 27-35

# Whether the adjacent side is reversed with respect to the target side
# (e.g Front 0-8 maps to 26-18 of Bottom, the reverse of normal 18-26)
FORWARD = 0
REVERSE = 1

faces = [
    # Face 0 (Front)
    [
        [Face.BOTTOM, SIDE_2, REVERSE],  # Target side 0 (0-8)
        [Face.LEFT, SIDE_3, REVERSE],
        [Face.TOP, SIDE_0, REVERSE],
        [Face.RIGHT, SIDE_1, REVERSE],
    ],
    # Face 1 (Back)
    [
        [Face.BOTTOM, SIDE_0, REVERSE],  # Target side 0 (0-8)
        [Face.RIGHT, SIDE_3, REVERSE],
        [Face.TOP, SIDE_2, REVERSE],
        [Face.LEFT, SIDE_1, REVERSE],
    ],
    # Face 2 (Left)
    [
        [Face.BOTTOM, SIDE_1, REVERSE],  # Target side 0 (0-8)
        [Face.BACK, SIDE_3, REVERSE],
        [Face.TOP, SIDE_1, REVERSE],
        [Face.FRONT, SIDE_1, REVERSE],
    ],
    # Face 3 (Right)
    [
        [Face.BOTTOM, SIDE_3, REVERSE],  # Target side 0 (0-8)
        [Face.FRONT, SIDE_3, REVERSE],
        [Face.TOP, SIDE_3, REVERSE],
        [Face.BACK, SIDE_1, REVERSE],
    ],
    # Face 4 (Top)
    [
        [Face.FRONT, SIDE_2, REVERSE],  # Target side 0 (0-8)
        [Face.LEFT, SIDE_2, REVERSE],
        [Face.BACK, SIDE_2, REVERSE],
        [Face.RIGHT, SIDE_2, REVERSE],
    ],
    # Face 5 (Bottom)
    [
        [Face.BACK, SIDE_0, REVERSE],  # Target side 0 (0-8)
        [Face.LEFT, SIDE_0, REVERSE],
        [Face.FRONT, SIDE_0, REVERSE],
        [Face.RIGHT, SIDE_0, REVERSE],
    ],
]

# Pre reversed ranges
side_range = [
    [idx for idx in range(0, 9)][::-1],
    [idx for idx in range(9, 18)][::-1],
    [idx for idx in range(18, 27)][::-1],
    [idx for idx in range(27, 36)][::-1],
]

# Enumerate the max pixel index for each side
side_ends = [8, 17, 26, 35]

# Enumerate the max pixel index for each side
side_starts = [0, 9, 18, 27]


# Return the side index into the structure above given a pixel index
def get_side_idx(pixel_idx):
    if pixel_idx <= 8:
        return 0
    elif pixel_idx <= 17:
        return 1
    elif pixel_idx <= 26:
        return 2
    else:
        return 3


# Generate code mapping adjacent pixels
#
# Format:
#
# adjacent = [
#    # Face
#     [
#         # Pixel 0
#         [ [Face.BOTTOM, 26], [Face.FRONT, 1], [Face.FRONT, 35] ]
#     ]
# ]

sys.stdout.write("adjacent = [\n")

for face_idx in range(6):
    face_sides = faces[face_idx]
    name = Face.face_names[face_idx].upper()

    sys.stdout.write("    # Face {:s}\n    [\n".format(name))

    for pixel_idx in range(Face.NUM_PIXELS):
        # Get pixel ahead of this one
        ahead = (pixel_idx+1) % Face.NUM_PIXELS

        # Get pixel behind this one
        if pixel_idx == 0:
            behind = 35
        else:
            behind = pixel_idx - 1

        # -- Get pixel near this one on the neighboring face --

        # Get the side this pixel is on
        side_idx = get_side_idx(pixel_idx)

        # Get the mapping of near face and sides
        side_mapping = face_sides[side_idx]

        # Get the near face index
        near_face_idx = side_mapping[0]

        # Get the near face side index
        near_face_side_idx = side_mapping[1]

        # Get the range of pixels for that near side and reverse it (because it turns
        # out they're all reversed)
        near_side_range = side_range[near_face_side_idx]

        side_start_idx = side_starts[side_idx]
        near = near_side_range[pixel_idx - side_start_idx]

        near_name = Face.face_names[near_face_idx].upper()

        sys.stdout.write("        [")
        sys.stdout.write("[Face.{:s}, {:d}], ".format(near_name, near))
        sys.stdout.write("[Face.{:s}, {:d}], ".format(name, behind))
        sys.stdout.write("[Face.{:s}, {:d}]".format(name, ahead))
        sys.stdout.write("],\n")
    sys.stdout.write("    ],\n")
sys.stdout.write("]\n")
