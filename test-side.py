from wonder.utils.opc import Client
from wonder.layout.face import Face

import sys
import re

def usage():
    print("\nLight a side of a face given by FACE and SIDE")
    print("light-side.py FACE SIDE\n")

face_idx = None
side_idx = None

if len(sys.argv) == 3:
    face_idx, side_idx = sys.argv[1:3]
    if re.search("[0-5]", face_idx):
        face_idx = int(face_idx)
    else:
        face_idx = Face.to_face_idx(face_idx)

    side_idx = int(side_idx)
else:
    print("Need FACE and SIDE")
    usage()
    exit()

if (side_idx > 3) or (side_idx < 0):
    print("Side value must be between 0-3")
    usage()
    exit()

if (face_idx > 5) or (face_idx < 0):
    print("Face must be between 0-5")
    usage()
    exit()

channel = Face.mapping[face_idx]['channel']
face_name = Face.face_names[face_idx]

clear = [(0, 0, 0) for p in range(9*4*6*2)]
pixels = [(0, 0, 0) for p in range(Face.NUM_PIXELS)]

for pixel_idx in Face.sides[side_idx]:
    mapped_pixel = Face.mapping[face_idx]['pixels'][pixel_idx]
    pixels[mapped_pixel] = (0, 255, 0)

print("Lighting side {:d} on {:s} face".format(side_idx, face_name))

client = Client("localhost:7890")
client.put_pixels(clear, channel=0)
client.put_pixels(pixels, channel=channel)
