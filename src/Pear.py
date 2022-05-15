import pygame
import random
from src.FoodCreator import FoodCreator


class PearCreator(FoodCreator):
    """
    Create class for Apples
    """
    def factory_method(self, display_width, display_height):
        return Pear(display_width, display_height)


class Pear:
    def __init__(self, display_width, display_height):
        self.display_width = display_width
        self.display_height = display_height

        self.pear_block = 7
        self.pear_color = (255, 215, 0)

        self.x_pear = random.randrange(60, self.display_height - 60, 20)
        self.y_pear = random.randrange(60, self.display_height - 60, 20)

    def spawn_pear(self, display):
        pygame.draw.circle(display, self.pear_color, [self.x_pear, self.y_pear], self.pear_block)

    def check_pear_eat(self, x_snake, y_snake):
        if abs(self.x_pear - x_snake) <= 15 and abs(self.y_pear - y_snake) <= 15:
            self.x_pear = random.randrange(60, self.display_height - 60, 20)
            self.y_pear = random.randrange(60, self.display_height - 60, 20)

            return True
