def ascii_hline(puzzle_size):
    if not puzzle_size > 0:
        if puzzle_size < 0:
            puzzle_size = -1 * puzzle_size
        elif puzzle_size == 0:
            puzzle_size = 1
    for i in range(puzzle_size): 
        print('*', end = ' ')

def ascii_vline(puzzle_size):
    if not puzzle_size > 0:
        if puzzle_size < 0:
            puzzle_size = -1 * puzzle_size
        elif puzzle_size == 0:
            puzzle_size = 1
    for i in range(puzzle_size):
        print('*')

def ascii_t(puzzle_size=6):

    if puzzle_size < 0:
        puzzle_size = -1 * puzzle_size

    if not (puzzle_size < 2) and not (puzzle_size % 2 == 1):
        puzzle_size = puzzle_size + 1
    sp = ' '
    for i in range(puzzle_size):
        if i == ((puzzle_size-1)/2):
            print(('*' + sp)*puzzle_size)
        else:
           print(sp*(puzzle_size-1) + '*' + sp*(puzzle_size-1))

def ascii_selector(ascii_functions,selection,puzzle_size):
    if selection == 'hline':
        ascii_functions[0](puzzle_size)
    elif selection == 'vline':
        ascii_functions[1](puzzle_size)
    elif selection == 't':
        ascii_functions[2](puzzle_size)
