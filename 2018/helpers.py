def read_puzzle_input(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]
