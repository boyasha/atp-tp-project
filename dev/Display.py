import pygame
from Globals import Globals
from Drawer import Drawer
from Logic import Logic
from Food import Food
import time


class Display:

    def __init__(self):
        self.start_game()

    pygame.init()
    display = pygame.display.set_mode([Globals.display_width, Globals.display_height])
    pygame.display.set_caption(Globals.display_caption)

    clock = pygame.time.Clock()

    def start_game(self):
        game_over = False
        game_close = False

        while not game_over:

            while game_close:

                self.display.fill(Globals.black_color)
                Drawer().message(self.display, Globals.lose_message, Globals.red_color)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q or event.unicode == "й":
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_u or event.unicode == "г":
                            return self.start_game()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    Drawer().moving_snake(event)

            game_close = Logic().check_border_crossing(game_close, Globals.display_width, Globals.display_height,
                                                       Globals.x_start, Globals.y_start)

            Globals.x_start += Globals.new_coord[0]
            Globals.y_start += Globals.new_coord[1]
            self.display.fill(Globals.black_color)

            Drawer().drawing_snake(self.display, Globals.blue_color,
                                   [Globals.x_start, Globals.y_start, Globals.snake_block, Globals.snake_block])
            Food().spawn_food(self.display, Globals.green_color, Globals.display_width, Globals.display_height,
                              Globals.snake_block / 2)
            pygame.display.update()
            Food().check_eat_food(self.display, Globals.x_start, Globals.y_start, Globals.x_food, Globals.y_food)
            self.clock.tick(Globals.snake_speed)

        pygame.display.update()

        pygame.quit()
        quit()
