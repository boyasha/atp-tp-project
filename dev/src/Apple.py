import pygame
import random
from src.FoodCreator import FoodCreator, Food


class AppleCreator(FoodCreator):
    """
    Create class for Apples
    """
    def factory_method(self, display_width, display_height):
        return Apple(display_width, display_height)


class Apple:
    def __init__(self, display_width, display_height):
        self.display_width = display_width
        self.display_height = display_height

        self.apple_block = 7
        self.apple_color = (124, 252, 0)

        self.x_apple = round(random.randrange(50, self.display_width - 50))
        self.y_apple = round(random.randrange(50, self.display_height - 50))

    def spawn_apple(self, display):
        pygame.draw.circle(display, self.apple_color, [self.x_apple, self.y_apple], self.apple_block)

    def check_eat_apple(self, x_snake, y_snake):
        if abs(self.x_apple-x_snake) < self.apple_block * 2.2 and abs(self.y_apple-y_snake) < self.apple_block * 2.2:
            self.x_apple = round(random.randrange(50, self.display_width - 50))
            self.y_apple = round(random.randrange(50, self.display_height - 50))
            return True
