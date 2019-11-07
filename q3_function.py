def ascii_t(puzzle_size = 6):
    if puzzle_size < 0:
        puzzle_size = puzzle_size * -1
    if puzzle_size % 2 == 0 and puzzle_size >= 2:
        puzzle_size = puzzle_size + 1
    middle_index = (puzzle_size / 2) - 0.5
    for r in range(puzzle_size):
        for c in range(puzzle_size):
            if r == middle_index:
                print("*", end = " ")
            elif c == middle_index:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print("")
