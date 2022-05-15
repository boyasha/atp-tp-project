import pygame
import random


class Bomb:
    def __init__(self, display_width, display_height):
        self.display_width = display_width
        self.display_height = display_height

        self.bomb_block = 15
        self.bomb_color = (128, 0, 0)
        self.count_for_change_bomb = 0

        self.x_bomb = round(random.randrange(0, self.display_height - 200) // self.bomb_block) * self.bomb_block
        self.y_bomb = round(random.randrange(0, self.display_height - 200) // self.bomb_block) * self.bomb_block

    def spawn_bomb(self, display):
        pygame.draw.circle(display, self.bomb_color, [self.x_bomb, self.y_bomb], self.bomb_block*2)

    def check_bomb_eat(self, x_snake, y_snake):
        if abs(self.x_bomb - x_snake) < self.bomb_block * 1.3 and abs(self.y_bomb - y_snake) < self.bomb_block * 1.3:
            self.x_bomb = round(random.randrange(0, self.display_height - 200) // self.bomb_block) * self.bomb_block
            self.y_bomb = round(random.randrange(0, self.display_height - 200) // self.bomb_block) * self.bomb_block
            return True

    def change_coord_bomb(self):
        self.count_for_change_bomb += 1
        if self.count_for_change_bomb % 5 == 0:
            self.x_bomb = round(random.randrange(0, self.display_height - 200) // self.bomb_block) * self.bomb_block
            self.y_bomb = round(random.randrange(0, self.display_height - 200) // self.bomb_block) * self.bomb_block
