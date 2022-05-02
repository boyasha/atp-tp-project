from Globals import Globals
import pygame
import random


class Food:
    def __init__(self):
        pass

    def spawn_food(self, display, color, Globals):
        pygame.draw.circle(display, color, [Globals.x_food, Globals.y_food], Globals.food_block/2)

    def check_eat_food(self, Globals):
        if abs(Globals.x_food-Globals.x_start) < Globals.food_block*1.1 and abs(Globals.y_food-Globals.y_start) < Globals.food_block*1.1:
            Globals.length_snake += 1
            Globals.snake_speed += 0.5
            Globals.x_food = round(random.randrange(0, Globals.display_width - 4*Globals.food_block) / Globals.food_block) * Globals.food_block
            Globals.y_food = round(random.randrange(0, Globals.display_height - 4*Globals.food_block) / Globals.food_block) * Globals.food_block

