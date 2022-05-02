from Globals import Globals
import pygame
import random

class Food:
    def spawn_food(self, display, color):
        pygame.draw.rect(display, color, [Globals.x_food, Globals.y_food, Globals.food_block, Globals.food_block])

    def check_eat_food(self, display):
        if abs(Globals.x_food-Globals.x_start) < Globals.food_block and abs(Globals.y_food-Globals.y_start) < Globals.food_block:
            Globals.length_snake += 1
            Globals.snake_speed += 0.5
            Globals.x_food = round(random.randrange(0, Globals.display_width - Globals.food_block) / Globals.food_block) * Globals.food_block
            Globals.y_food = round(random.randrange(0, Globals.display_height - Globals.food_block) / Globals.food_block) * Globals.food_block

