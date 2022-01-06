# Usage:
# $ python3
# Python 3.8.5 (default, Jul 21 2020, 10:48:26) 
# [Clang 11.0.3 (clang-1103.0.32.62)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import sudoku
# >>> board=sudoku.init()
# >>> sudoku.set_board(board, [[0,0,2,9,0,0,8,7,0],[8,0,7,0,0,0,9,0,0],[0,0,0,8,0,4,6,0,3],[0,0,0,1,0,0,0,6,0],[0,0,0,2,0,5,0,0,0],[0,8,0,0,0,9,0,0,0],[6,0,3,4,0,8,0,0,0],[0,0,8,0,0,0,7,0,4],[0,2,9,0,0,7,1,0,0]])
# >>> sudoku.solve(board)
# True
# >>> sudoku.print_board(board)
# =========================================
# ||  3|   | 2 ||   |   |   ||   |   |1  ||
# ||   |4  |   ||   | 5 |  6||   |   |   ||
# ||   |   |   ||  9|   |   || 8 |7  |   ||
# -----------------------------------------
# ||   |   |   ||  3| 2 |1  ||   |   |   ||
# ||   |  6|   ||   |   |   ||   |4  | 5 ||
# || 8 |   |7  ||   |   |   ||  9|   |   ||
# -----------------------------------------
# ||   |1  |   ||   |   |   ||   | 2 |  3||
# ||   |   | 5 ||   |   |4  ||  6|   |   ||
# ||  9|   |   || 8 |7  |   ||   |   |   ||
# =========================================
# || 2 |   |   ||1  |   |  3||   |   |   ||
# ||   |   |4  ||   |   |   || 5 |  6|   ||
# ||   |  9|   ||   | 8 |   ||   |   |7  ||
# -----------------------------------------
# ||   |  3|1  || 2 |   |   ||   |   |   ||
# ||   |   |   ||   |  6| 5 ||4  |   |   ||
# ||7  |   |   ||   |   |   ||   |  9| 8 ||
# -----------------------------------------
# ||   |   |   ||   |   |   ||  3|1  | 2 ||
# || 5 |   |  6||   |4  |   ||   |   |   ||
# ||   | 8 |   ||7  |   |  9||   |   |   ||
# =========================================
# ||   |   |  3||   |1  |   || 2 |   |   ||
# ||  6|   |   ||4  |   |   ||   | 5 |   ||
# ||   |7  |   ||   |   | 8 ||   |   |  9||
# -----------------------------------------
# ||1  |   |   ||   |   | 2 ||   |  3|   ||
# ||   | 5 |   ||  6|   |   ||   |   |4  ||
# ||   |   | 8 ||   |  9|   ||7  |   |   ||
# -----------------------------------------
# ||   | 2 |   ||   |  3|   ||1  |   |   ||
# ||4  |   |   || 5 |   |   ||   |   |  6||
# ||   |   |  9||   |   |7  ||   | 8 |   ||
# =========================================




# Each cell in the sudoku board is represented as a list of integers. 
# Initially all cells contain all values 1..9 (list(range(1, 10))). As 
# the board is getting solved,
# each cell eventually end up with only one value, and hence become a 
# single-value list.
# Each row is a list of nine cells. The board is a list of nine rows, 
# hence forming a 9x9 matrix.

# Function init()
# This function initialises the board as defined above. 
# It returns a board where each cell contains all possible values, 
# hence representing a "blank" board.
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

# Function: print_cell_line
# Each cell can contain from one to nine values, and should be displayed
# like this:
# Init   Part   Solved
# -----  -----  -----
# |123|  | 23|  |   |
# |456|  | 5 |  | 5 |
# |789|  |78 |  |   |
# -----  -----  -----
# This function prints one line, i.e. either 123, 456 or 789, replacing any
# missing values with a space
def print_cell_line(cell, line):
    print('|', end='')
    for i in range(line * 3 + 1, line * 3 + 4):
        if i in cell:
            print(i, end='')
        else:
            print(' ', end='')

# Function: print_board_line
# Prints one line from the board, e.g.
# ||456|456|456||456|456|456||456|456|456||
# Each cell is separated by | and each grid (3x3 cells) by ||
def print_board_line(board, row, line):
    print('|', end='')
    for i in range(0, 9):
        print_cell_line(board[row][i], line)
        if i % 3 == 2:
            print('|', end='')
    print('|')

# Function: print_row
# Each row of cells consists of three lines for values 123, 456 and 789
# respectively. Rows are separated by a line
def print_row(board, row):
    for i in range(0, 3):
        print_board_line(board, row, i)

# Function: print_board
# The board consists of nine lines with a separator line after each grid,
# or three lines
# =========================================
# ||1 3|1 3| 2 ||   |1 3|1 3||   |   |1  ||
# ||45 |456|   ||   | 56|  6||   |   | 5 ||
# ||   |   |   ||  9|   |   || 8 |7  |   ||
# -----------------------------------------
# ||   |1 3|   ||  3|123|123||   |12 |12 ||
# ||   |456|   || 56| 56|  6||   |45 | 5 ||
# || 8 |   |7  ||   |   |   ||  9|   |   ||
# -----------------------------------------
# ||1  |1  |1  ||   |12 |   ||   |12 |  3||
# || 5 | 5 | 5 ||   | 5 |4  ||  6| 5 |   ||
# ||  9|  9|   || 8 |7  |   ||   |   |   ||
# =========================================
# || 23|  3|   ||1  |  3|  3|| 23|   | 2 ||
# ||45 |45 |45 ||   |4  |   ||45 |  6| 5 ||
# ||7 9|7 9|   ||   |78 |   ||   |   |789||
# -----------------------------------------
# ||1 3|1 3|1  || 2 |  3|   ||  3|1 3|1  ||
# ||4  |4 6|4 6||   |4 6| 5 ||4  |4  |   ||
# ||7 9|7 9|   ||   |78 |   ||   | 89|789||
# -----------------------------------------
# ||123|   |1  ||  3|  3|   || 23|123|12 ||
# ||45 |   |456||  6|4 6|   ||45 |45 | 5 ||
# ||7  | 8 |   ||7  |7  |  9||   |   |7  ||
# =========================================
# ||   |1  |  3||   |12 |   || 2 | 2 | 2 ||
# ||  6| 5 |   ||4  | 5 |   || 5 | 5 | 5 ||
# ||   |7  |   ||   |  9| 8 ||   |  9|  9||
# -----------------------------------------
# ||1  |1  |   ||  3|123|123||   | 23|   ||
# || 5 | 5 |   || 56| 56|  6||   | 5 |4  ||
# ||   |   | 8 ||   |  9|   ||7  |  9|   ||
# -----------------------------------------
# ||   | 2 |   ||  3|  3|   ||1  |  3|   ||
# ||45 |   |   || 56| 56|   ||   | 5 | 56||
# ||   |   |  9||   |   |7  ||   | 8 | 8 ||
# =========================================
def print_board(board):
    for i in range(0, 9):
        if i % 3 != 0:
            print("-----------------------------------------")
        else:
            print("=========================================")
        print_row(board, i)
    print("=========================================")

# Function: solved
# Check if the board is solved by checking if every cell has only
# one value (length == 1)
def solved (board):
    for i in range(0, 9):
        for j in range(0, 9):
            if len(board[i][j]) > 1:
                return False
    return True

# Algorithm #1: Pruning candidates from cells when a related cell has
# been solved. E.g. if cell board[0][0] (top left corner) is set to 5
# then row 0 can not contain a 5 in any other cell, nor can column 0,
# nor the top left 3x3 grid

# Function prune_row
# Assuming that the cell at board[row][col] only has a single value,
# then that value can be removed from all other cells in the same row
def prune_row(board, row, col):
    changed = False
    [val] = board[row][col]
    l =  list(range(0, 9))
    l.remove(col)
    for i in l:
        if val in board[row][i]:
            board[row][i].remove(val)
            if len(board[row][i])==0:
                print("Removed last:", row, i, val)
            changed = True
    return changed

# Function prune_col
# Assuming that the cell at board[row][col] only has a single value,
# then that value can be removed from all other cells in the same row
def prune_col(board, row, col):
    changed = False
    [val] = board[row][col]
    l =  list(range(0, 9))
    l.remove(row)
    for i in l:
        if val in board[i][col]:
            board[i][col].remove(val)
            if len(board[i][col])==0:
                print("Removed last:", i, col, val)
            changed = True
    return changed

# Function prune_grid
# Assuming that the cell at board[row][col] only has a single value,
# then that value can be removed from all other cells in the same 3x3
# grid
def prune_grid(board, row, col):
    changed = False
    [val] = board[row][col]
    for i in range(row//3*3, row//3*3+3):
        for j in range(col//3*3, col//3*3+3):
            if [row, col] != [i, j]:
                if val in board[i][j]:
                    board[i][j].remove(val)
                    if len(board[i][j])<1:
                        print("Removed last:", i, j, val)
                    changed = True
    return changed

# Function prune
# Checking if the cell at board[row][col] only has a single value,
# and if so, removing that value from all other cells in the same row,
# column and 3x3 grid
def prune(board, row, col):
    changed = False
    if len(board[row][col]) == 1:
        changed = prune_row(board, row, col)
        if prune_col(board, row, col):
            changed = True
        if prune_grid(board, row, col):
            changed = True
    return changed

# Function: prune_all
# Checking the whole board for single values, and pruning row/col/grid
def prune_all(board):
    changed = False
    for i in range(0, 9):
        for j in range(0, 9):
            if prune(board, i, j):
                changed = True
    return changed

# End Algorithm #1, Pruning

# Function: set_prune
# Set the value at board[row][col] to val and prune the row, column and grid
def set_prune(board, row, col, val):
    board[row][col] = [val]
    prune(board, row, col)

# Function: set_board
# Given a 9x9 matrix, set the board to the corresponding values. '0'
# represents an empty cell, e.g.
# [[0,0,2,9,0,0,8,7,0],
#  [8,0,7,0,0,0,9,0,0],
#  [0,0,0,8,0,4,6,0,3],
#  [0,0,0,1,0,0,0,6,0],
#  [0,0,0,2,0,5,0,0,0],
#  [0,8,0,0,0,9,0,0,0],
#  [6,0,3,4,0,8,0,0,0],
#  [0,0,8,0,0,0,7,0,4],
#  [0,2,9,0,0,7,1,0,0]]
def set_board(board, values):
    for i in range(0, 9):
        for j in range(0, 9):
            if values[i][j] != 0:
                set_prune(board, i, j, values[i][j])

# Algorithm #2: Checking if a candidate value only appears once in
# rows, cells or grids, and setting the value accordingly

# Function: unique_in_row
# Checking a row for candidate values that can only be in one cell in
# that row, and if so, setting that cell to that value
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

# Function: unique_in_any_row
# Checking all rows for unique candidates
def unique_in_any_row(board):
    changed = False
    for row in range(0, 9):
        changed = unique_in_row(board, row) or changed
    return changed
                
# Function: unique_in_col
# Checking a column for candidate values that can only be in one cell in
# that column, and if so, setting that cell to that value
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

# Function: unique_in_any_col
# Checking all columns for unique candidates
def unique_in_any_col(board):
    changed = False
    for col in range(0, 9):
        changed = unique_in_col(board, col) or changed
    return changed
                
# Function: unique_in_grid
# Checking a column for candidate values that can only be in one cell in
# that 3x3 grid, and if so, setting that cell to that value
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

# Function: unique_in_any_grid
# Checking all 3x3 grids for unique candidates
def unique_in_any_grid(board):
    changed = False
    for gridx in [0, 3, 6]:
        for gridy in [0, 3, 6]:
            changed = unique_in_grid(board, gridx, gridy) or changed
    return changed

# Function: unique
# Checking all rows, columns and grids for unique candidates
def unique (board):
    changed = unique_in_any_row(board)
    changed = unique_in_any_col(board) or changed
    changed = unique_in_any_grid(board) or changed
    return changed

# End Algorith #2, Unique candidate values

# Algorithm #3: If a value appears multiple times in a grid row (or
# column) but not in any other row (column) in that grid, then that
# value cannot appear in any other cell in that row (column)

# Function: count_val_in_gridrow
# Count the number of appearances of val in a grid row
def count_val_in_gridrow(board, gridrowx, gridrowy, val):
    count = 0
    for y in range(gridrowy, gridrowy + 3):
        if val in board[gridrowx][y]:
            count = count + 1
    return count

# Function: unique_in_gridrow
# Check if val appears in other rows in the same grid
def unique_in_gridrow(board,  gridrowx, gridrowy, val):
    other_rows = list(range(gridrowx//3*3, gridrowx//3*3+3))
    other_rows.remove(gridrowx)
    if ((count_val_in_gridrow(board, other_rows[0], gridrowy, val) > 0)
        or (count_val_in_gridrow(board, other_rows[1], gridrowy, val) > 0)):
        return False
    return True

# Function: remove_in_other_gridrows
# Remove the value from the rest of the row
def remove_in_other_gridrows(board,  gridrowx, gridrowy, val):
    changed = False
    other_cols = [0, 3, 6]
    other_cols.remove(gridrowy)
    for y0 in other_cols:
        for y in range(y0, y0+3):
            if val in board[gridrowx][y]:
                board[gridrowx][y].remove(val)
                changed = True
    return changed

# Function: count_val_in_gridcol
# Count the number of appearances of val in a grid column
def count_val_in_gridcol(board, gridcolx, gridcoly, val):
    count = 0
    for x in range(gridcolx, gridcolx + 3):
        if val in board[x][gridcoly]:
            count = count + 1
    return count

# Function: unique_in_gridcol
# Check if val appears in other columns in the same grid
def unique_in_gridcol(board,  gridcolx, gridcoly, val):
    other_cols = list(range(gridcoly//3*3, gridcoly//3*3+3))
    other_cols.remove(gridcoly)
    if ((count_val_in_gridcol(board, gridcolx, other_cols[0], val) > 0)
        or (count_val_in_gridcol(board, gridcolx, other_cols[1], val) > 0)):
        return False
    return True

# Function: remove_in_other_gridcols
# Remove the value from the rest of the column
def remove_in_other_gridcols(board,  gridcolx, gridcoly, val):
    changed = False
    other_rows = [0, 3, 6]
    other_rows.remove(gridcolx)
    for x0 in other_rows:
        for x in range(x0, x0+3):
            if val in board[x][gridcoly]:
                board[x][gridcoly].remove(val)
                changed = True
    return changed

# Function: check_and_remove_in_grids
# Check every row and column in every grid for unique values in that grid
def check_and_remove_in_grids(board):
    changed = False
    for val in range(1,10):
        for i in range(0, 9):
            for j in [0, 3, 6]:
                if count_val_in_gridrow(board, i, j, val) > 1:
                    if unique_in_gridrow(board, i, j, val):
                        remove_in_other_gridrows(board, i, j, val)
                        changed = True
                if count_val_in_gridcol(board, j, i, val) > 1:
                    if unique_in_gridcol(board, j, i, val):
                        remove_in_other_gridcols(board, j, i, val)
                        changed = True
    return changed

# End of Algorith #3

# Function: solve
def solve (board):
    changed = True
    while (changed):
        changed = prune_all(board)
    if solved(board):
        return True # Algorithm #1 only
    changed = True
    while (changed):
        changed = unique(board)
        changed = prune_all(board) or changed
    if solved(board):
        return True # Algorithms 1 + 2
    check_and_remove_in_grids(board)
    changed = True
    while (changed):
        changed = unique(board)
        changed = prune_all(board)
    if solved(board):
        return True # Algorithms 1 + 2 + 3
    return False # Partially solved - rest left as exercise for user  :-)

def test():
    board = init()
    set_board(board, [[6,0,0,0,0,0,0,0,9],
                      [0,0,4,0,5,0,0,0,0],
                      [0,9,0,0,0,0,1,0,5],
                      [0,0,0,0,9,0,0,0,8],
                      [0,5,0,3,0,0,2,4,0],
                      [0,0,0,0,0,6,3,9,0],
                      [0,0,7,0,3,4,0,0,0],
                      [0,0,0,0,6,8,0,3,0],
                      [1,0,8,2,0,0,0,0,0]])
    solve(board)
    print_board(board)
    return board

if __name__ == "__main__":
    test()
