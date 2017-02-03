from wonder.utils.opc import Client
from wonder.layout.face import Face

import sys


def usage():
    print("\nLight a face if FACE is given or a single pixel on that face if PIXEL is given")
    print("light-test.py FACE [PIXEL]\n")

face_idx = None
pixel_idx = None

if len(sys.argv) == 3:
    face_idx, pixel_idx = sys.argv[1:3]
    face_idx = int(face_idx)
    pixel_idx = int(pixel_idx)
    if (pixel_idx > 35) or (pixel_idx < 0):
        print("Pixel value must be between 0-35")
        usage()
        exit()
elif len(sys.argv) == 2:
    face_idx = sys.argv[1]
    face_idx = int(face_idx)
    pixel_idx = None
else:
    print("Need face and optional pixel")
    usage()
    exit()

if (face_idx > 5) or (face_idx < 0):
    print("Face must be between 0-5")
    usage()
    exit()


channel = Face.mapping[face_idx]['channel']
face_name = Face.face_names[face_idx]
clear = [(0, 0, 0) for p in range(9*4*6*2)]

if pixel_idx is None:
    pixels = [(0, 0, 255) for p in range(Face.NUM_PIXELS)]

    print("Lighting {:s} face".format(face_name))
else:
    mapped_pixel = Face.mapping[face_idx]['pixels'][pixel_idx]
    pixels = [(0, 0, 0) for p in range(mapped_pixel+1)]
    pixels[mapped_pixel] = (255, 0, 0)

    print("Lighting pixel {:d} on {:s} face".format(pixel_idx, face_name))


client = Client("localhost:7890")
client.put_pixels(clear, channel=0)
client.put_pixels(pixels, channel=channel)
