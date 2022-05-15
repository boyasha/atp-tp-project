import pygame
import random


class Snake:
    """
    Class for logic of game
    """
    def __init__(self, display_width, display_height):
        self.display_width = display_width
        self.display_height = display_height
        self.snake_length = 1
        self.snake_list = []

        self.snake_speed = 10
        self.snake_block = 20
        self.snake_color = (13, 143, 141)

        self.x_snake = round(random.randrange(0, self.display_width - self.snake_block) / self.snake_block) * self.snake_block
        self.y_snake = round(random.randrange(0, self.display_height - self.snake_block) / self.snake_block) * self.snake_block

        self.check_snake_move_side = ''

    def drawing_snake(self, display, color, snake_block, snake_list):
        for item in snake_list:
            pygame.draw.rect(display, color, [item[0], item[1], snake_block, snake_block], border_radius=5)

    def check_border_crossing(self, display_width, display_height, x, y):
        if x >= display_width or x < 0 or y >= display_height or y < 0:
            return True

    def check_snake_cross_snake(self, Globals, snake_head):
        if len(Globals.snake_list) > Globals.length_snake:
            del Globals.snake_list[0]

        for i in Globals.snake_list[:-1]:
            if i == snake_head:
                game_close = True
                return game_close

    def moving_snake(self, move_side, snake_block):
        new_coord = [0, 0]

        if move_side.key == pygame.K_LEFT or move_side.key == pygame.K_a or move_side.unicode == "ф":
            if self.check_snake_move_side == 'right':
                new_coord[0] = snake_block
                new_coord[1] = 0
            else:
                new_coord[0] = -snake_block
                new_coord[1] = 0
                self.check_snake_move_side = 'left'

        elif move_side.key == pygame.K_RIGHT or move_side.key == pygame.K_d or move_side.unicode == "в":
            if self.check_snake_move_side == 'left':
                new_coord[0] = -snake_block
                new_coord[1] = 0
            else:
                new_coord[0] = snake_block
                new_coord[1] = 0
                self.check_snake_move_side = 'right'

        elif move_side.key == pygame.K_UP or move_side.key == pygame.K_w or move_side.unicode == "ц":
            if self.check_snake_move_side == 'down':
                new_coord[0] = 0
                new_coord[1] = snake_block
            else:
                new_coord[0] = 0
                new_coord[1] = -snake_block
                self.check_snake_move_side = 'up'

        elif move_side.key == pygame.K_DOWN or move_side.key == pygame.K_s or move_side.unicode == "ы":
            if self.check_snake_move_side == 'up':
                new_coord[0] = 0
                new_coord[1] = -snake_block
            else:
                new_coord[0] = 0
                new_coord[1] = snake_block
                self.check_snake_move_side = 'down'

        return new_coord
