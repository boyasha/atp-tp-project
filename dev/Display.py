import pygame
from Globals import Globals
from Drawer import Drawer


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
                Drawer().moving_snake(event.type)

        Globals.x_start += Globals.new_coord[0]
        Globals.y_start += Globals.new_coord[1]

        Drawer().drawing_snake(display, Globals.blue_color, [Globals.x_start, Globals.y_start, 10, 10])
        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()
