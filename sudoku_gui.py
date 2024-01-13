import numpy as np
import math
import pygame

pygame.init()
res = (820, 820) #screen dimensions
screen = pygame.display.set_mode(res)
font = pygame.font.Font('freesansbold.ttf', 32) #text font

pygame.display.set_caption('Sudoku Bot')

white = (255, 255, 255)
black = (0,0,0)
red = (228, 92, 84)
grey = (220, 220, 220)
pink = (229, 97, 107)
green = (202, 223, 166)

board = [
    [3, 1, 0, 4, 0, 0, 0, 2, 8],
    [0, 0, 8, 0, 6, 0, 0, 5, 0],
    [0, 2, 6, 0, 0, 0, 0, 9, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 7, 0, 6, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 8, 0],
    [4, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 6, 0, 3, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 1, 0, 3, 0, 9]
]

#print(np.matrix(board))

main_box_dim = (540, 540) #dimensions of the parent box
main_box_pos = ((res[0]-main_box_dim[0])/2, ((res[1]-main_box_dim[1])/2)-50) #starting coordinates of the parent box

button_dim = (main_box_dim[0]/3, main_box_dim[0]/9) #dimensions of the "solve" button
button_pos = ((res[0]-button_dim[0])/2, main_box_pos[1]+(1.1*main_box_dim[1])) #starting coordinates of the button

def empty_position(): #function to give empty boxes
    global board
    empty = []
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                empty.append((j+1, i+1))
    return empty

empty_pos = empty_position()
empty_box_num = []
for i in empty_pos:
    num = ((i[1] - 1)*9) + i[0]
    empty_box_num.append(num)

#function to draw boxes
def draw_boxes():
    small_box_dim = (main_box_dim[0]/9, main_box_dim[1]/9)
    small_x = main_box_pos[0] #small box init x
    small_y = main_box_pos[1] #small box init y
    boxes = 0
    for i in range(1, 82):
        if i in empty_box_num and len(empty_position()) != 0:
            pygame.draw.rect(screen, grey, pygame.Rect(small_x, small_y, small_box_dim[0], small_box_dim[1]))
        elif i in empty_box_num and len(empty_position()) == 0:
            pygame.draw.rect(screen, green, pygame.Rect(small_x, small_y, small_box_dim[0], small_box_dim[1]))


        pygame.draw.rect(screen, black, pygame.Rect(small_x, small_y, small_box_dim[0], small_box_dim[1]), 2)
        boxes += 1
        small_x += main_box_dim[0]/9
        if boxes%9 == 0:
            small_x = main_box_pos[0]
            small_y += main_box_dim[1]/9
    
    pygame.draw.line(screen, red, (main_box_pos[0] + (main_box_dim[0]/3), main_box_pos[1]), (main_box_pos[0] + (main_box_dim[0]/3), main_box_pos[1] + main_box_dim[1]), 6)
    pygame.draw.line(screen, red, (main_box_pos[0] + (2*(main_box_dim[0]/3)), main_box_pos[1]), (main_box_pos[0] + (2*(main_box_dim[0]/3)), main_box_pos[1] + main_box_dim[1]), 6)
    pygame.draw.line(screen, red, (main_box_pos[0], main_box_pos[1] + (main_box_dim[1]/3)), (main_box_pos[0] + main_box_dim[0], main_box_pos[1] + (main_box_dim[1]/3)), 6)
    pygame.draw.line(screen, red, (main_box_pos[0], main_box_pos[1] + (2*(main_box_dim[1]/3))), (main_box_pos[0] + main_box_dim[0], main_box_pos[1] + (2*(main_box_dim[1]/3))), 6)

#function to display entered data on the game window
def display_data(data):
    text_x = main_box_pos[0] + (main_box_dim[0]/18)
    text_y = main_box_pos[1] + (main_box_dim[1]/18)
    at_box = 1
    for i in data:
        for j in i:
            text_bg = white
            if str(j) == "0":
                j = "  "

            if at_box in empty_box_num and len(empty_position()) != 0:
                text_bg = grey
            elif at_box in empty_box_num and len(empty_position()) == 0:
                text_bg = green
            text = font.render(str(j), True, black, text_bg)
            textRect = text.get_rect()
            textRect.center = (text_x, text_y)
            screen.blit(text, textRect)

            text_x += main_box_dim[0]/9
            at_box += 1
        text_y += main_box_dim[1]/9
        text_x = main_box_pos[0] + (main_box_dim[0]/18)

def listen(mouse_pos):
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            return("quit")
        if events.type == pygame.MOUSEBUTTONDOWN:
            if button_pos[0] <= mouse_pos[0] <= button_pos[0]+button_dim[0] and button_pos[1] <= mouse_pos[1] <= button_pos[1]+button_dim[1]:
                return("clicked")


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

def solve():
    global board
    i = 0
    win = True
    
    while win:
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
            win = False

        if len(empty_position()) == 0:
            win = False
        #print(np.matrix(board))
        #print("------------------")

run = True
clicked = False

while run:
    mouse = pygame.mouse.get_pos()
    listen_out = listen(mouse)
    if listen_out == "quit":
        run = False
    
    screen.fill(white)
    draw_boxes()
    pygame.draw.rect(screen, black, pygame.Rect(main_box_pos[0],main_box_pos[1],main_box_dim[0],main_box_dim[1]), 6)
    display_data(board)

    if listen_out == "clicked":
        clicked = True
    if not(clicked):
        if button_pos[0] <= mouse[0] <= button_pos[0]+button_dim[0] and button_pos[1] <= mouse[1] <= button_pos[1]+button_dim[1]:
            button_color = red
        else:
            button_color = pink

        pygame.draw.rect(screen, button_color, pygame.Rect(button_pos[0], button_pos[1], button_dim[0], button_dim[1]), 0, 4)

        button_text = font.render("SOLVE", True, white, button_color)
        button_textRect = button_text.get_rect()
        button_textRect.center = (button_pos[0] + (button_dim[0]/2), button_pos[1] + (button_dim[1]/2))
        screen.blit(button_text, button_textRect)

    if len(empty_position()) == 0:
        solved_text = font.render("SOLVED!", True, black, white)
        solved_textRect = solved_text.get_rect()
        solved_textRect.center = (button_pos[0] + (button_dim[0]/2), button_pos[1] + (button_dim[1]/2))
        screen.blit(solved_text, solved_textRect)


    pygame.display.update()

    if len(empty_position()) != 0 and clicked:
        solving_text = font.render("Solving...", True, black, white)
        solving_textRect = solving_text.get_rect()
        solving_textRect.center = (button_pos[0] + (button_dim[0]/2), button_pos[1] + (button_dim[1]/2))
        screen.blit(solving_text, solving_textRect)
        pygame.display.update()
        solve()

#solve()
#print(np.matrix(board))

    