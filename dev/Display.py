# -*- coding: utf-8 -*-
import pygame
from Globals import Globals
from Drawer import Drawer
from Logic import Logic
from Food import Food
import random


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
                Drawer().message_of_lose(self.display, Globals.lose_message, Globals.red_color)
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

            Drawer().message_of_score(self.display, Globals.score_message + f" {Globals.length_snake - 1}",
                                      Globals.white_color)

            Food().spawn_food(self.display, Globals.green_color)
            snake_head = [Globals.x_start, Globals.y_start]
            Globals.snake_list.append(snake_head)

            if len(Globals.snake_list) > Globals.length_snake:
                del Globals.snake_list[0]

            for i in Globals.snake_list[:-1]:
                if i == snake_head:
                    game_close = True

            Drawer().drawing_snake(self.display, Globals.blue_color)
            pygame.display.update()
            Food().check_eat_food(self.display)

            self.clock.tick(Globals.snake_speed)

        pygame.quit()
        quit()
