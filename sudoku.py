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
    [val] = board[row][col]
    l =  list(range(0, 9))
    l.remove(col)
    for i in l:
        if board[row][i].count(val):
            board[row][i].remove(val)

def prune_col(board, row, col):
    [val] = board[row][col]
    l =  list(range(0, 9))
    l.remove(row)
    for i in l:
        if board[i][col].count(val):
            board[i][col].remove(val)

def prune_grid(board, row, col):
    [val] = board[row][col]
    for i in range(row//3*3, row//3*3+3):
        for j in range(row//3*3, row//3*3+3):
            if [row, col] != [i, j]:
                if board[i][j].count(val):
                    board[i][j].remove(val)

def prune(board, row, col):
    prune_row(board, row, col)
    prune_col(board, row, col)
    prune_grid(board, row, col)

def test():
    board = init()
    board[0][0].remove(1)
    board[3][0].remove(2)
    board[6][0].remove(3)
    board[0][3].remove(4)
    board[3][3].remove(5)
    board[6][3].remove(6)
    board[0][6].remove(7)
    board[3][6].remove(8)
    board[6][6].remove(9)
    print("Cell 0,0, line 0:", end='')
    print_cell_line(board[0][0], 0)
    print()
    print("Cell 4,5, line 2:", end='')
    print_cell_line(board[4][5], 2)
    print()
    print("Row 0, Line 0:", end=' ')
    print_board_line(board, 0, 0)
    print("Row 0, Line 1:", end=' ')
    print_board_line(board, 0, 1)
    print("Row 3, Line 2:", end=' ')
    print_board_line(board, 3, 2)
    board[3][3]=[5]
    print_board(board)
    prune_row(board, 3, 3)
    print_board(board)
    prune_col(board, 3, 3)
    print_board(board)
    return board

if __name__ == "__main__":
    test()
