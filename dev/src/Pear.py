import pygame
import random


class Pear:
    def __init__(self, display_width, display_height):
        self.display_width = display_width
        self.display_height = display_height

        self.pear_block = 15
        self.pear_color = (255, 215, 0)

        self.x_pear = round(random.randrange(0, self.display_height - 200) // self.pear_block) * self.pear_block
        self.y_pear = round(random.randrange(0, self.display_height - 200) // self.pear_block) * self.pear_block

    def spawn_pear(self, display):
        pygame.draw.circle(display, self.pear_color, [self.x_pear, self.y_pear], self.pear_block / 2)

    def check_pear_eat(self, x_snake, y_snake):
        if abs(self.x_pear - x_snake) < self.pear_block * 1.3 and abs(self.y_pear - y_snake) < self.pear_block * 1.3:
            self.x_pear = round(random.randrange(0, self.display_height - 200) // self.pear_block) * self.pear_block
            self.y_pear = round(random.randrange(0, self.display_height - 200) // self.pear_block) * self.pear_block
            return True
