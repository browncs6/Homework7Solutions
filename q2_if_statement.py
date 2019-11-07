# TODO: use "argparse" to parse an argument named size of type int assigning it to variable puzzle_size
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('size', type=int)
puzzle_size = parser.parse_args().size


# TODO: write some if statements
if puzzle_size < 0:
    puzzle_size *= -1
if puzzle_size > 1 and puzzle_size % 2 == 0:
    puzzle_size += 1
