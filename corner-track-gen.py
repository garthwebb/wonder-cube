#!/usr/bin/python

from wonder.layout.face import Face

import sys
import re

# Corners are numbered from 0 to 7, starting with the front face to the back face
# and going clockwise:
#  - Corner 0: the lower right corner of face 0
#  - Corner 1: the lower left corner of face 0
#  - Corner 2: the upper left corner of face 0
#  - Corner 3: the upper right corner of face 0
#  - Corner 4: the lower right corner of face 1
#  - Corner 5: the lower left corner of face 1
#  - Corner 6: the upper left corner of face 1
#  - Corner 7: the upper right corner of face 1


class Tree:
    value = None
    left = None
    right = None

    def __init__(self, value):
        self.value = value


# Create a tree from six sides, assuming s1 is the starting side,
# s2 and s3 are the next two possibilities and s4 and s5 are the two possibilities after that
def gen_tree(s1, s2, s3, s4, s5):
    n1 = Tree(s1)
    n2 = Tree(s2)
    n3 = Tree(s3)
    n4 = Tree(s4)
    n5 = Tree(s5)

    n1.left = n2
    n1.right = n3

    n2.left = n4
    n2.right = n5

    n3.left = n4
    n3.right = n5

    return n1


def walk_tree(node, history="            "):
    match = re.search("([fblrto])([0-3])(r?)", node.value)
    if not match:
        return

    face_idx = Face.to_face_idx(match.group(1))
    side_range = Face.sides[int(match.group(2))]
    range_copy = list(side_range)

    if match.group(3) == 'r':
        range_copy.reverse()

    for pixel_idx in range_copy:
        history += "[{}, {}], ".format(face_idx, pixel_idx)

    if node.left is None:
        print("        [")
        print(history)
        print("        ],")
        return

    walk_tree(node.left, history)
    walk_tree(node.right, history)

# Corner 0 : opposes corner 6
corner0 = list()
corner0.append(gen_tree("f0", "f1", "l3r", "t1", "l2r"))
corner0.append(gen_tree("o2r", "o1r", "l0", "b3r", "l1"))
corner0.append(gen_tree("o3", "o0", "b0r", "l1", "b3r"))
corner0.append(gen_tree("r0r", "r3r", "b1", "t2r", "b2"))
corner0.append(gen_tree("f3r", "f2r", "t0", "l2r", "t1"))
corner0.append(gen_tree("r1", "r2", "t3r", "b2", "t2r"))

# Corner 6 : opposite of paths in corner 0

print("corner_tracks = [")
print("    [  # Corner 0")
for num, tree in enumerate(corner0):
    walk_tree(tree)
print("    ],")
print("]")
