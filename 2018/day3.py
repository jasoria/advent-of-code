import re
import numpy as np


def get_max_dimensions(pieces_info):
    x_origins = [get_origin(string)[0] for string in pieces_info]
    y_origins = [get_origin(string)[1] for string in pieces_info]
    x_pieces = [get_dimensions(string)[0] for string in pieces_info]
    y_pieces = [get_dimensions(string)[1] for string in pieces_info]
    return max(x_origins) + max(x_pieces), max(y_origins) + max(y_pieces)


def get_origin(area_input):
    search = re.search('([0-9]+),([0-9]+)', area_input)
    groups = search.groups()
    return int(groups[0]), int(groups[1])


def get_dimensions(area_input):
    search = re.search('([0-9]+)x([0-9]+)', area_input)
    groups = search.groups()
    return int(groups[0]), int(groups[1])


puzzle_input = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2'
]

fabric_size = get_max_dimensions(puzzle_input)
fabric = np.zeros(fabric_size)

for cut in puzzle_input:
    origin = get_origin(cut)
    size = get_dimensions(cut)
    xo = origin[0]
    yo = origin[1]
    width = size[0]
    heigth = size[1]
    fabric[yo:yo + heigth, xo:xo + width] = 1
    print(fabric)






