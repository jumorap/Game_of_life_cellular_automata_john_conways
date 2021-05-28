import pygame
import numpy as np
import time

# Start pygame to prepare a window and define the width and
# height of it. After build the window wit their measure, where
# the background color is defined by [bg] about to black, and
# define the measure of cells in the window
pygame.init()

width, height = 700, 700
screen = pygame.display.set_mode((height, width))
bg = 25, 25, 25

screen.fill(bg)

numb_x_cell, numb_y_cell = 50, 50
dim_cell_w = width / numb_x_cell
dim_cell_h = height / numb_y_cell
pause_execution = False

# We define the state of cells "alive" or "dead"
game_state = np.zeros((numb_x_cell, numb_y_cell))

# We give params to proof the code
game_state[26, 19] = 1
game_state[25, 18] = 1
game_state[25, 17] = 1
game_state[26, 16] = 1
game_state[27, 18] = 1
game_state[27, 17] = 1

game_state[26, 28] = 1
game_state[25, 27] = 1
game_state[25, 26] = 1
game_state[26, 25] = 1
game_state[27, 27] = 1
game_state[27, 26] = 1

game_state[23, 22] = 1
game_state[22, 23] = 1
game_state[21, 23] = 1
game_state[20, 22] = 1
game_state[21, 21] = 1
game_state[22, 21] = 1

game_state[32, 22] = 1
game_state[31, 23] = 1
game_state[30, 23] = 1
game_state[29, 22] = 1
game_state[30, 21] = 1
game_state[31, 21] = 1

game_state[19, 23] = 1
game_state[27, 29] = 1
game_state[33, 21] = 1
game_state[25, 15] = 1

print("\n _______  _______  __   __  _______    _______  _______    ___      ___   _______  _______"
      "\n|       ||   _   ||  |_|  ||       |  |       ||       |  |   |    |   | |       ||       |"
      "\n|    ___||  |_|  ||       ||    ___|  |   _   ||    ___|  |   |    |   | |    ___||    ___|"
      "\n|   | __ |       ||       ||   |___   |  | |  ||   |___   |   |    |   | |   |___ |   |___ "
      "\n|   ||  ||       ||       ||    ___|  |  |_|  ||    ___|  |   |___ |   | |    ___||    ___|"
      "\n|   |_| ||   _   || ||_|| ||   |___   |       ||   |      |       ||   | |   |    |   |___ "
      "\n|_______||__| |__||_|   |_||_______|  |_______||___|      |_______||___| |___|    |_______|\n")

print("REMEMBER THAT TO PAUSE THE GAME, YOU HAVES TO PRESS ANY KEY IN YOUR KEYBOARD,\n"
      "AND IF YOU WANT DRAW NEW BOXES, YOU HAVE TO PRESS ANY KEY AND PAINT WITH THEIR LEFT CLICK OF MOUSE")

# Execution loop
while True:

    new_game_state = np.copy(game_state)

    screen.fill(bg)
    time.sleep(0.1)

    # We register the click event to make better the user experience
    eve = pygame.event.get()

    for event in eve:
        if event.type == pygame.KEYDOWN:
            pause_execution = not pause_execution

        # We save in a variable the button that has been pressed in mouse
        mouse_click = pygame.mouse.get_pressed()

        if sum(mouse_click) > 0:
            pos_x, pos_y = pygame.mouse.get_pos()
            cell_x, cell_y = int(np.floor(pos_x / dim_cell_w)), int(np.floor(pos_y / dim_cell_h))
            new_game_state[cell_x, cell_y] = not mouse_click[2]
            print(cell_x, cell_y)

    for y in range(0, numb_x_cell):
        for x in range(0, numb_y_cell):

            if not pause_execution:

                # We calculate the number of company around the cells
                numb_neighbors = game_state[(x - 1) % numb_x_cell, (y - 1) % numb_y_cell] + \
                                 game_state[x % numb_x_cell, (y - 1) % numb_y_cell] + \
                                 game_state[(x + 1) % numb_x_cell, (y - 1) % numb_y_cell] + \
                                 game_state[(x - 1) % numb_x_cell, y % numb_y_cell] + \
                                 game_state[(x + 1) % numb_x_cell, y % numb_y_cell] + \
                                 game_state[(x - 1) % numb_x_cell, (y + 1) % numb_y_cell] + \
                                 game_state[x % numb_x_cell, (y + 1) % numb_y_cell] + \
                                 game_state[(x + 1) % numb_x_cell, (y + 1) % numb_y_cell]

                # We create the rules for the cells, to define the GAME OF LIFE
                # Rule #1: A cell is "dead" if have 3 neighbors alive around
                if game_state[x, y] == 0 and numb_neighbors == 3:
                    new_game_state[x, y] = 1

                # Rule #2: A cell is "alive" with less of 2 of more than 3 neighbors alive
                elif game_state[x, y] == 1 and (numb_neighbors < 2 or numb_neighbors > 3):
                    new_game_state[x, y] = 0

            polyg = [
                (x * dim_cell_w, y * dim_cell_h),
                ((x + 1) * dim_cell_w, y * dim_cell_h),
                ((x + 1) * dim_cell_w, (y + 1) * dim_cell_h),
                (x * dim_cell_w, (y + 1) * dim_cell_h)
            ]

            # We write the cell for each pair of x and y
            if new_game_state[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), polyg, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), polyg, 0)

    # Update the window and the state of game
    game_state = np.copy(new_game_state)
    pygame.display.flip()

