# -*- coding: utf-8 -*-
import pygame
from src.Globals import Globals
from src.Drawer import Drawer
from src.Snake import Snake
from src.Game import Game
from src.Apple import Apple
from src.Pear import Pear


class Display:
    def __init__(self):
        self.Globals = Globals()
        self.Drawer = Drawer()
        self.Snake = Snake(self.Globals.display_width, self.Globals.display_height)
        self.Game = Game()
        self.Apple = Apple(self.Globals.display_width, self.Globals.display_height)
        self.Pear = Pear(self.Globals.display_width, self.Globals.display_height)

        pygame.init()
        self.display = pygame.display.set_mode([self.Globals.display_width, self.Globals.display_height])
        pygame.display.set_caption(self.Globals.display_caption)

        self.clock = pygame.time.Clock()
        self.start_game()

    def start_game(self):
        game_over = False
        game_close = False

        while not game_over:
            game_over = self.Game.game(self.Globals, self.Drawer, self.Snake, self, self.display, game_close, game_over)

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

            self.Apple.spawn_apple(self.display, self.Globals.apple_color)
            self.Pear.spawn_pear(self.display, self.Globals.pear_color)

            self.Snake.drawing_snake(self.display, self.Globals.snake_block,
                                     self.Globals.snake_list)
            pygame.display.update()
            self.Apple.check_eat_apple(self.Globals.x_start, self.Globals.y_start)
            self.Pear.check_pear_eat(self.Globals.x_start, self.Globals.y_start)

            self.clock.tick(self.Globals.snake_speed)

        pygame.quit()
        quit()
