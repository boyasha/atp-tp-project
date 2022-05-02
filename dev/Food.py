from Globals import Globals
import random
import pygame


class Food:
    def spawn_food(self, display, color, display_width, display_height, food_block):
        Globals.x_food = round(random.randrange(0, display_width - food_block) / 10.0) * 10.0
        Globals.y_food = round(random.randrange(0, display_width - food_block) / 10.0) * 10.0
        pygame.draw.rect(display, color, [Globals.x_food, Globals.y_food, food_block, food_block])

    def check_eat_food(self, display, x, y,  x_food, y_food):
        if x == x_food and y == y_food:
            print("Yummy!")