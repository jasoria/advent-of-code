from collections import Counter
import numpy as np
import helpers


def get_count_of_letters(set_of_letters):
    return Counter(set_of_letters)


def counter_has(repetitions, count_of_letters):
    result = False
    for letter in count_of_letters:
        number_of_repetitions = count_of_letters[letter]
        if number_of_repetitions == repetitions:
            result = True
            break
    return result


def cummulative_counter(repetitions, strings):
    result = 0
    for a_string in strings:
        count_of_letters = get_count_of_letters(a_string)
        add_to_result = counter_has(repetitions, count_of_letters)
        if add_to_result:
            result += 1
    return result


def solve_part_1(strings):
    count_of_2 = cummulative_counter(2, strings)
    count_of_3 = cummulative_counter(3, strings)
    return count_of_2 * count_of_3


def convert_string_to_numpy_array(a_string):
    return np.array(list(a_string))


def get_index_of_different_letters(np_array_1, np_array_2):
    search_result = np.where(np_array_1 != np_array_2)
    return search_result[0]


def differs_by_one_letter(np_array_of_index):
    if np_array_of_index.size == 1:
        return True
    else:
        return False


def concatenate_string(np_array_of_letters, index):
    result = ''
    for i in range(len(np_array_of_letters)):
        if i != index:
            result += np_array_of_letters[i]
    return result


def solve_part_2(strings):
    for string_a in strings:
        for string_b in strings:
            np_string_a = convert_string_to_numpy_array(string_a)
            np_string_b = convert_string_to_numpy_array(string_b)
            index_array = get_index_of_different_letters(np_string_a, np_string_b)
            if differs_by_one_letter(index_array):
                return concatenate_string(np_string_a, index_array[0])


puzzle_input = helpers.read_puzzle_input('day2input.txt')

print(solve_part_1(puzzle_input))
print(solve_part_2(puzzle_input))








