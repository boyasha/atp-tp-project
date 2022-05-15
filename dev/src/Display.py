# -*- coding: utf-8 -*-
import pygame
from src.Globals import Globals
from src.Message import Message
from src.Snake import Snake
from src.Game import Game
from src.Apple import AppleCreator
from src.Pear import PearCreator
from src.Bomb import BombCreator


class Display:
    def __init__(self):
        self.Globals = Globals()
        self.Game = Game()
        self.Message = Message(self.Globals.display_width, self.Globals.display_height)
        self.Snake = Snake(self.Globals.display_width, self.Globals.display_height)
        self.Apple = AppleCreator().factory_method(self.Globals.display_width, self.Globals.display_height)
        self.Pear = PearCreator().factory_method(self.Globals.display_width, self.Globals.display_height)
        self.Bomb = BombCreator().factory_method(self.Globals.display_width, self.Globals.display_height)

        pygame.init()
        self.display = pygame.display.set_mode([self.Globals.display_width, self.Globals.display_height])
        pygame.display.set_caption(self.Globals.display_caption)

        self.clock = pygame.time.Clock()
        self.new_coord = [0, 0]

        self.game_over = False
        self.game_close = False
        self.start_game()

    def start_game(self):

        while not self.game_over:
            self.game_over = self.Game.game(self.Globals, self.Message, self.Snake, self, self.display, self.game_close,
                                            self.game_over)

            snake_head = [self.Snake.x_snake, self.Snake.y_snake]
            self.Snake.snake_list.append(snake_head)

            self.game_close = self.Snake.check_border_crossing() or self.Snake.check_snake_cross_snake(snake_head) \
                              or self.Bomb.check_bomb_eat(self.Snake.x_snake, self.Snake.y_snake)

            self.Snake.x_snake += self.new_coord[0]
            self.Snake.y_snake += self.new_coord[1]
            self.display.fill(self.Globals.black_color)

            self.Message.message_of_score(self.display, self.Snake.snake_length)

            self.Apple.spawn_apple(self.display)
            self.Pear.spawn_pear(self.display)
            self.Bomb.spawn_bomb(self.display)

            self.Snake.drawing_snake(self.display)
            pygame.display.update()

            if self.Apple.check_eat_apple(self.Snake.snake_list[-1][0], self.Snake.snake_list[-1][1]):
                self.Snake.snake_eat_apple()
                self.Bomb.change_coord_bomb()

            if self.Pear.check_pear_eat(self.Snake.snake_list[-1][0], self.Snake.snake_list[-1][1]):
                self.Snake.snake_eat_pale()
                self.Bomb.change_coord_bomb()

            self.clock.tick(self.Snake.snake_speed)

        pygame.quit()
        quit()
