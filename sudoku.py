import numpy as np
import math

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
#print(np.matrix(board))

def possible(x, y, n):
    global board
    row = True
    column = True
    box = True
    for i in board:
        if i[x-1] == n:
            row = False
    
    if n in board[y-1]:
        column = False

    box_num = (math.ceil(x/3), math.ceil(y/3))
    box_start_coord = ((3*(box_num[0]-1)), (3*(box_num[1]-1)))
    for i in range(box_start_coord[1], box_start_coord[1] + 3):
        for j in range(box_start_coord[0], box_start_coord[0] + 3):
            if board[i][j] == n:
                box = False
    
    if row == column == box == True:
        return True
    else:
        return False

def empty_position():
    global board
    empty = []
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                empty.append((j+1, i+1))
    return empty

empty_pos = empty_position()

def solve():
    global board
    i = 0
    win = 0
    
    while win == 0:
        for sol in range((board[empty_pos[i][1] - 1][empty_pos[i][0] - 1])+1, 10):
            found = False
            if possible(empty_pos[i][0], empty_pos[i][1], sol):
                found = True
                board[empty_pos[i][1] - 1][empty_pos[i][0] - 1] = sol
                i += 1
                break
        if found == False and i != 0:
            board[empty_pos[i][1] - 1][empty_pos[i][0] - 1] = 0
            i -= 1
        elif found == False and i == 0:
            print("Invalid Board!")
            win = 1

        if len(empty_position()) == 0:
            win = 1


solve()
print(np.matrix(board))

    