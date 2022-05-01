import pygame
from Globals import Globals
from Drawer import Drawer
from Logic import Logic
import time

class Display:
    pygame.init()
    display = pygame.display.set_mode([Globals.display_width, Globals.display_height])
    pygame.display.set_caption(Globals.display_caption)

    clock = pygame.time.Clock()

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                Drawer().moving_snake(event)

        game_over = Logic().check_border_crossing(game_over, Globals.display_width, Globals.display_height, Globals.x_start, Globals.y_start)

        Globals.x_start += Globals.new_coord[0]
        Globals.y_start += Globals.new_coord[1]

        display.fill(Globals.black_color)
        Drawer().drawing_snake(display, Globals.blue_color, [Globals.x_start, Globals.y_start, Globals.snake_block, Globals.snake_block])
        pygame.display.update()
        clock.tick(Globals.snake_speed)

    Drawer().message(display, Globals.lose_message, Globals.red_color)
    pygame.display.update()
    time.sleep(3)

    pygame.quit()
    quit()
