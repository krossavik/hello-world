cell = list(range(1, 9))
board = [[cell, cell, cell, cell, cell, cell, cell, cell, cell],
         [cell, cell, cell, cell, cell, cell, cell, cell, cell],
         [cell, cell, cell, cell, cell, cell, cell, cell, cell],
         [cell, cell, cell, cell, cell, cell, cell, cell, cell],
         [cell, cell, cell, cell, cell, cell, cell, cell, cell],
         [cell, cell, cell, cell, cell, cell, cell, cell, cell],
         [cell, cell, cell, cell, cell, cell, cell, cell, cell],
         [cell, cell, cell, cell, cell, cell, cell, cell, cell],
         [cell, cell, cell, cell, cell, cell, cell, cell, cell]]

def print-cell-line(cell, line):
    for i in range(1, 3):
        print(cell[i])
