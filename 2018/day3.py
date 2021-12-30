import re
import numpy as np
import helpers


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


def cut_factory(cut_information, fabric_size):
    fabric = np.zeros(fabric_size)
    origin = get_origin(cut_information)
    size = get_dimensions(cut_information)
    x_o, y_o = origin[0], origin[1]
    width, heigth = size[0], size[1]
    fabric[y_o:y_o + heigth, x_o:x_o + width] = 1
    return fabric


def get_common_area(puzzle_input, fabric_size):
    cut_number = 1
    for cut_info in puzzle_input:
        if cut_number == 1:
            cut = cut_factory(cut_info, fabric_size)
        else:
            cut += cut_factory(cut_info, fabric_size)
        cut_number += 1
    common_area = np.zeros(fabric_size)
    common_area[np.where(cut >= 2)] = 1
    return common_area


def solve_part_1(puzzle_input):
    fabric_size = get_max_dimensions(puzzle_input)
    common_area = get_common_area(puzzle_input, fabric_size)
    return np.sum(common_area)


def solve_part_2(puzzle_input):
    untouched_cut = None
    fabric_size = get_max_dimensions(puzzle_input)
    commom_area = get_common_area(puzzle_input, fabric_size)
    cut_number = 1
    for cut_info in puzzle_input:
        cut = cut_factory(cut_info, fabric_size)
        intersection = np.logical_and(cut, commom_area)
        if not np.any(intersection):
            untouched_cut = cut_number
            break
        cut_number += 1
    return untouched_cut


puzzle_input = helpers.read_puzzle_input('day3input.txt')

# print(solve_part_1(puzzle_input))
print(solve_part_2(puzzle_input))















