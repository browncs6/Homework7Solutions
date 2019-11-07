#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

# TODO: create a ascii_hline function

def ascii_hline(puzzle_size):

    if puzzle_size < 0:
        puzzle_size=puzzle_size * -1

    if puzzle_size == 0:
        puzzle_size == 1
    
    ans=""
    
    for row in range(puzzle_size - 1):
        ans += "* "
    ans += "*"
    print(ans)

# TODO: create a ascii_vline function

def ascii_vline(puzzle_size):

    if puzzle_size < 0:
        puzzle_size=puzzle_size * -1

    if puzzle_size == 0:
        puzzle_size == 1

    for row in range(puzzle_size):
        print('*')

# TODO: copy over your ascii_t function and remove the default parameter

def ascii_t(puzzle_size):

    if puzzle_size < 0:
        puzzle_size=puzzle_size * -1

    if (puzzle_size > 2) and (puzzle_size % 2 == 0):
        puzzle_size=puzzle_size + 1

    for row in range(puzzle_size):
        if row == (puzzle_size - 1)/2:
            print('* ' * (puzzle_size - 1) + '*')
        else:
            print(' ' * (puzzle_size - 1) + '*')

# TODO: create a ascii_selector function

def ascii_selector(ascii_functions, selection, puzzle_size):
    if selection == 'hline':
        ascii_functions[0](puzzle_size)

    if selection == 'vline':
        ascii_functions[1](puzzle_size)

    if selection == 't':
        ascii_functions[2](puzzle_size)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('size', nargs='?', type=int, default=1, help='size of the ascii art puzzle')
    parser.add_argument('puzzle', nargs='?', type=str, default='t', help='puzzle choices; includes: hline, vline, or t')

    args = parser.parse_args()

    # TODO: create ascii_functions list 

    ascii_functions = [ascii_hline, ascii_vline, ascii_t]

    # TODO: call ascii_selector function 

    ascii_selector(ascii_functions, args.puzzle, args.size)
