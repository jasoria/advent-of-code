import numpy as np
import helpers


def calc_resulting_frequency(frequency_changes):
    current_frequency = 0
    for change in frequency_changes:
        current_frequency += change
    return current_frequency


def find_first_repeating_frequency(frequency_changes):
    current_frequency = 0
    frequency_history = np.array([current_frequency])
    index = 0
    while index < len(frequency_changes):
        current_frequency += frequency_changes[index]
        if current_frequency in frequency_history:
            return current_frequency
        else:
            frequency_history = np.append(frequency_history, current_frequency)
            index += 1
            if index == len(frequency_changes):
                index = 0


puzzle_input = helpers.read_puzzle_input('day1input.txt')
puzzle_input = [int(line) for line in puzzle_input]

# Part 1
result_part_1 = calc_resulting_frequency(puzzle_input)

# Part 2
result_part_2 = find_first_repeating_frequency(puzzle_input)

print(result_part_2)

