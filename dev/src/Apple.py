import pygame
import random


class Apple:
    def __init__(self, display_width, display_height):
        self.display_width = display_width
        self.display_height = display_height

        self.apple_block = 15

        self.x_apple = round(random.randrange(0, self.display_height - 200) // self.apple_block) * self.apple_block
        self.y_apple = round(random.randrange(0, self.display_height - 200) // self.apple_block) * self.apple_block

    def spawn_apple(self, display, color):
        pygame.draw.circle(display, color, [self.x_apple, self.y_apple], self.apple_block/2)

    def check_eat_apple(self, x_snake, y_snake):
        if abs(self.x_apple-x_snake) < self.apple_block*1.3 and abs(self.y_apple-y_snake) < self.apple_block*1.3:
            self.x_apple = round(random.randrange(0, self.display_height - 200) // self.apple_block) * self.apple_block
            self.y_apple = round(random.randrange(0, self.display_height - 200) // self.apple_block) * self.apple_block
            return True

