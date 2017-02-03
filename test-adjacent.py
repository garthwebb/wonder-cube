from wonder.utils.opc import Client
from wonder.layout.face import Face
from wonder.utils.adjacency import Adjacent

import sys


def usage():
    print("\nLight a pixel and its adjacent pixels given a FACE and PIXEL")
    print("light-adjacent.py FACE PIXEL\n")


def get_mapped_pixel(face_idx, pixel_idx):
    return Face.mapping[face_idx]['pixels'][pixel_idx]

face_idx = None
pixel_idx = None

if len(sys.argv) == 3:
    face_idx, pixel_idx = sys.argv[1:3]
    face_idx = int(face_idx)
    pixel_idx = int(pixel_idx)
else:
    print("Need FACE and PIXEL")
    usage()
    exit()

if (pixel_idx > 35) or (pixel_idx < 0):
    print("Pixel value must be between 0-35")
    usage()
    exit()

if (face_idx > 5) or (face_idx < 0):
    print("Face must be between 0-5")
    usage()
    exit()

face_name = Face.face_names[face_idx]
print("Lighting pixel {:d} on {:s} face".format(pixel_idx, face_name))

# Clear the cube
clear = [(0, 0, 0) for p in range(9*4*6*2)]
client = Client("localhost:7890")
client.put_pixels(clear, channel=0)

# Light the target pixel
pixels = [(0, 0, 0) for p in range(Face.NUM_PIXELS)]

channel = Face.mapping[face_idx]['channel']
mapped_pixel = get_mapped_pixel(face_idx, pixel_idx)
pixels[mapped_pixel] = (255, 0, 0)

# Light the behind pixel
behind_idx = Adjacent.get_behind_idx(face_idx, pixel_idx)
mapped_pixel = get_mapped_pixel(face_idx, behind_idx)
pixels[mapped_pixel] = (0, 0, 255)

# Light the ahead pixel
ahead_idx = Adjacent.get_ahead_idx(face_idx, pixel_idx)
mapped_pixel = get_mapped_pixel(face_idx, ahead_idx)
pixels[mapped_pixel] = (0, 0, 255)

client.put_pixels(pixels, channel=channel)

# Light the near pixel
near_face_idx = Adjacent.get_near_face(face_idx, pixel_idx)
pixels = [(0, 0, 0) for p in range(Face.NUM_PIXELS)]
channel = Face.mapping[near_face_idx]['channel']

near_idx = Adjacent.get_near_idx(face_idx, pixel_idx)
mapped_pixel = get_mapped_pixel(near_face_idx, near_idx)
pixels[mapped_pixel] = (0, 0, 255)

client.put_pixels(pixels, channel=channel)
