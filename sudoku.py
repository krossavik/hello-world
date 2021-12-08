cell = list(range(1, 10))
board = [[cell, cell, cell, cell, cell, cell, cell, cell, cell],
         [cell, cell, cell, cell, cell, cell, cell, cell, cell],
         [cell, cell, cell, cell, cell, cell, cell, cell, cell],
         [cell, cell, cell, cell, cell, cell, cell, cell, cell],
         [cell, cell, cell, cell, cell, cell, cell, cell, cell],
         [cell, cell, cell, cell, cell, cell, cell, cell, cell],
         [cell, cell, cell, cell, cell, cell, cell, cell, cell],
         [cell, cell, cell, cell, cell, cell, cell, cell, cell],
         [cell, cell, cell, cell, cell, cell, cell, cell, cell]]

def print_cell_line(cell, line):
    for i in range(line, line+3):
        if i in cell:
            print(i, end=' ')
        else:
            print(' ', end=' ')

        
