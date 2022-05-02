# -*- coding: utf-8 -*-
import pygame
from Globals import Globals
from Drawer import Drawer
from Snake import Snake
from Food import Food
import random


class Display:

    def __init__(self):
        self.Globals = Globals()
        self.Food = Food()
        self.Drawer = Drawer()
        self.Snake = Snake()
        pygame.init()
        self.display = pygame.display.set_mode([self.Globals.display_width, self.Globals.display_height])
        pygame.display.set_caption(self.Globals.display_caption)

        self.clock = pygame.time.Clock()
        self.start_game()

    def start_game(self):
        game_over = False
        game_close = False

        while not game_over:

            while game_close:
                self.display.fill(self.Globals.black_color)
                self.Drawer.message_of_lose(self.display, self.Globals.lose_message, self.Globals.red_color,
                                            self.Globals)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q or event.unicode == "й":
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_u or event.unicode == "г":
                            return Display()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    self.Globals.new_coord = self.Snake.moving_snake(event, self.Globals.snake_block)

            snake_head = [self.Globals.x_start, self.Globals.y_start]
            self.Globals.snake_list.append(snake_head)

            game_close = self.Snake.check_border_crossing(self.Globals.display_width,
                                                          self.Globals.display_height,
                                                          self.Globals.x_start,
                                                          self.Globals.y_start) or self.Snake.check_snake_cross_snake(
                self.Globals, snake_head)

            self.Globals.x_start += self.Globals.new_coord[0]
            self.Globals.y_start += self.Globals.new_coord[1]
            self.display.fill(self.Globals.black_color)

            self.Drawer.message_of_score(self.display, self.Globals.score_message + f" {self.Globals.length_snake - 1}",
                                         self.Globals.white_color)

            self.Food.spawn_food(self.display, self.Globals.green_color, self.Globals)


            self.Snake.drawing_snake(self.display, self.Globals.blue_color, self.Globals.snake_block,
                                     self.Globals.snake_list)
            pygame.display.update()
            self.Food.check_eat_food(self.Globals)

            self.clock.tick(self.Globals.snake_speed)

        pygame.quit()
        quit()
