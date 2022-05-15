import pygame
import random
from src.FoodCreator import FoodCreator


class BombCreator(FoodCreator):
    """
    Create class for Apples
    """
    def factory_method(self, display_width, display_height):
        return Bomb(display_width, display_height)


class Bomb:
    def __init__(self, display_width, display_height):
        self.display_width = display_width
        self.display_height = display_height

        self.bomb_block = 30
        self.bomb_color = (128, 0, 0)
        self.count_for_change_bomb = 0

        self.x_bomb = round(random.randrange(50, self.display_width - 50), 100)
        self.y_bomb = round(random.randrange(50, self.display_height - 50), 100)

    def spawn_bomb(self, display):
        pygame.draw.circle(display, self.bomb_color, [self.x_bomb, self.y_bomb], self.bomb_block)

    def check_bomb_eat(self, x_snake, y_snake):
        if abs(self.x_bomb - x_snake) < self.bomb_block * 1.3 and abs(self.y_bomb - y_snake) < self.bomb_block * 1.3:
            self.x_bomb = round(random.randrange(50, self.display_width - 50), 100)
            self.y_bomb = round(random.randrange(50, self.display_height - 50), 100)
            return True

    def change_coord_bomb(self):
        self.count_for_change_bomb += 1
        if self.count_for_change_bomb % 5 == 0:
            self.x_bomb = round(random.randrange(50, self.display_width - 50), 100)
            self.y_bomb = round(random.randrange(50, self.display_height - 50), 100)

