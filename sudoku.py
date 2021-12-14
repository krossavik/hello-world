def init():
    board = [[list(range(1, 10)), list(range(1, 10)), list(range(1, 10)),
              list(range(1, 10)), list(range(1, 10)), list(range(1, 10)),
              list(range(1, 10)), list(range(1, 10)), list(range(1, 10))],
             [list(range(1, 10)), list(range(1, 10)), list(range(1, 10)),
              list(range(1, 10)), list(range(1, 10)), list(range(1, 10)),
              list(range(1, 10)), list(range(1, 10)), list(range(1, 10))],
             [list(range(1, 10)), list(range(1, 10)), list(range(1, 10)),
              list(range(1, 10)), list(range(1, 10)), list(range(1, 10)),
              list(range(1, 10)), list(range(1, 10)), list(range(1, 10))],
             [list(range(1, 10)), list(range(1, 10)), list(range(1, 10)),
              list(range(1, 10)), list(range(1, 10)), list(range(1, 10)),
              list(range(1, 10)), list(range(1, 10)), list(range(1, 10))],
             [list(range(1, 10)), list(range(1, 10)), list(range(1, 10)),
              list(range(1, 10)), list(range(1, 10)), list(range(1, 10)),
              list(range(1, 10)), list(range(1, 10)), list(range(1, 10))],
             [list(range(1, 10)), list(range(1, 10)), list(range(1, 10)),
              list(range(1, 10)), list(range(1, 10)), list(range(1, 10)),
              list(range(1, 10)), list(range(1, 10)), list(range(1, 10))],
             [list(range(1, 10)), list(range(1, 10)), list(range(1, 10)),
              list(range(1, 10)), list(range(1, 10)), list(range(1, 10)),
              list(range(1, 10)), list(range(1, 10)), list(range(1, 10))],
             [list(range(1, 10)), list(range(1, 10)), list(range(1, 10)),
              list(range(1, 10)), list(range(1, 10)), list(range(1, 10)),
              list(range(1, 10)), list(range(1, 10)), list(range(1, 10))],
             [list(range(1, 10)), list(range(1, 10)), list(range(1, 10)),
              list(range(1, 10)), list(range(1, 10)), list(range(1, 10)),
              list(range(1, 10)), list(range(1, 10)), list(range(1, 10))]
             ]
    return board

def print_cell_line(cell, line):
    for i in range(line * 3 + 1, line * 3 + 4):
        if i in cell:
            print(i, end='')
        else:
            print(' ', end='')

def print_board_line(board, row, line):
    print('||', end='')
    for i in range(0, 9):
        print_cell_line(board[row][i], line)
        print('|', end='')
        if i % 3 == 2:
            print('|', end='')
    print()

def print_row(board, row):
    for i in range(0, 3):
        print_board_line(board, row, i)
    print("-----------------------------------------")

def print_board(board):
    print("-----------------------------------------")
    for i in range(0, 9):
        print_row(board, i)
        if i % 3 == 2:
            print("-----------------------------------------")

def prune_row(board, row, col):
    changed = False
    [val] = board[row][col]
    l =  list(range(0, 9))
    l.remove(col)
    for i in l:
        if board[row][i].count(val):
            board[row][i].remove(val)
            changed = True
    return changed

def prune_col(board, row, col):
    changed = False
    [val] = board[row][col]
    l =  list(range(0, 9))
    l.remove(row)
    for i in l:
        if board[i][col].count(val):
            board[i][col].remove(val)
            changed = True
    return changed

def prune_grid(board, row, col):
    changed = False
    [val] = board[row][col]
    for i in range(row//3*3, row//3*3+3):
        for j in range(col//3*3, col//3*3+3):
            if [row, col] != [i, j]:
                if board[i][j].count(val):
                    board[i][j].remove(val)
                    changed = True
    return changed

def prune(board, row, col):
    changed = False
    if len(board[row][col]) == 1:
        changed = prune_row(board, row, col)
        if prune_col(board, row, col):
            changed = True
        if prune_grid(board, row, col):
            changed = True
    return changed

def set_prune(board, row, col, val):
    board[row][col] = [val]
    prune(board, row, col)

def set_board(board, values):
    for i in range(0, 9):
        for j in range(0, 9):
            if values[i][j] != 0:
                set_prune(board, i, j, values[i][j])

def prune_all(board):
    changed = False
    for i in range(0, 9):
        for j in range(0, 9):
            if prune(board, i, j):
                changed = True
    return changed

def unique_in_row(board, row):
    changed = False
    for val in range(1, 10):
        found = 9
        for col in range(0, 9):
            if val in board[row][col]:
                if found == 9:
                    found = col
                else:
                    found = 10 # duplicate
                    break
        if found < 9:
            if len(board[row][found]) > 1:
                set_prune(board, row, found, val)
                changed = True
    return changed

def unique_in_any_row(board):
    changed = False
    for row in range(0, 9):
        changed = unique_in_row(board, row) or changed
    return changed
                
def unique_in_col(board, col):
    changed = False
    for val in range(1, 10):
        found = 9
        for row in range(0, 9):
            if val in board[row][col]:
                if found == 9:
                    found = row
                else:
                    found = 10 # duplicate
                    break
        if found < 9:
            if len(board[found][col]) > 1:
                set_prune(board, found, col, val)
                changed = True
    return changed

def unique_in_any_col(board):
    changed = False
    for col in range(0, 9):
        changed = unique_in_col(board, col) or changed
    return changed
                
def unique_in_grid(board, gridx, gridy):
    changed = False
    for val in range(1, 10):
        foundx = 9
        for row in range(gridx, gridx+3):
            for col in range(gridy, gridy+3):
                if val in board[row][col]:
                    if foundx == 9:
                        foundx = row
                        foundy = col
                    else:
                        foundx = 10 # duplicate
                        break
        if foundx < 9:
            if len(board[foundx][foundy]) > 1:
                set_prune(board, foundx, foundy, val)
                changed = True
    return changed

def unique_in_any_grid(board):
    changed = False
    for gridx in [0, 3, 6]:
        for gridy in [0, 3, 6]:
            changed = unique_in_grid(board, gridx, gridy) or changed
    return changed
                
def test():
    board = init()
    set_board(board, [[0,3,0,2,0,0,0,0,0],[0,6,0,3,0,0,0,0,4],
                      [7,0,5,0,0,9,0,0,0],[4,0,3,0,0,7,6,0,0],
                      [9,0,0,5,0,4,0,0,1],[0,0,2,6,0,0,9,0,7],
                      [0,0,0,7,0,0,4,0,8],[8,0,0,0,0,1,0,7,0],
                      [0,0,0,0,0,3,0,2,0]])
    prune_all(board)
    prune_all(board)
    prune_all(board)
    prune_all(board)
    prune_all(board)
    unique_in_any_row(board)
    unique_in_row(board,0)
    print_board(board)
    return board

if __name__ == "__main__":
    test()
