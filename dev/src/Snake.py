import pygame
import random


class Snake:
    """
    Class for logic of game
    """

    def __init__(self, display_width, display_height):
        self.display_width = display_width
        self.display_height = display_height

        self.snake_speed = 12
        self.snake_length = 1
        self.snake_block = 20
        self.snake_color = (13, 143, 141)

        self.x_snake = round(
            random.randrange(0, self.display_width - self.snake_block) / self.snake_block) * self.snake_block
        self.y_snake = round(
            random.randrange(0, self.display_height - self.snake_block) / self.snake_block) * self.snake_block

        self.snake_list = []

        self.check_snake_move_side = ''

    def drawing_snake(self, display):
        for item in self.snake_list:
            pygame.draw.rect(display, self.snake_color, [item[0], item[1], self.snake_block, self.snake_block],
                             border_radius=5)

    def check_border_crossing(self):
        if self.x_snake >= self.display_width or self.x_snake < 0 or self.y_snake >= self.display_height or self.y_snake < 0:
            return True

    def check_snake_cross_snake(self, snake_head):
        if len(self.snake_list) > self.snake_length:
            del self.snake_list[0]

        for i in self.snake_list[:-1]:
            if i == snake_head:
                game_close = True
                return game_close

    def moving_snake(self, move_side):
        new_coord = [0, 0]

        if move_side.key == pygame.K_LEFT or move_side.key == pygame.K_a or move_side.unicode == "ф":
            if self.check_snake_move_side == 'right':
                new_coord[0] = self.snake_block
                new_coord[1] = 0
            else:
                new_coord[0] = -self.snake_block
                new_coord[1] = 0
                self.check_snake_move_side = 'left'

        elif move_side.key == pygame.K_RIGHT or move_side.key == pygame.K_d or move_side.unicode == "в":
            if self.check_snake_move_side == 'left':
                new_coord[0] = -self.snake_block
                new_coord[1] = 0
            else:
                new_coord[0] = self.snake_block
                new_coord[1] = 0
                self.check_snake_move_side = 'right'

        elif move_side.key == pygame.K_UP or move_side.key == pygame.K_w or move_side.unicode == "ц":
            if self.check_snake_move_side == 'down':
                new_coord[0] = 0
                new_coord[1] = self.snake_block
            else:
                new_coord[0] = 0
                new_coord[1] = -self.snake_block
                self.check_snake_move_side = 'up'

        elif move_side.key == pygame.K_DOWN or move_side.key == pygame.K_s or move_side.unicode == "ы":
            if self.check_snake_move_side == 'up':
                new_coord[0] = 0
                new_coord[1] = -self.snake_block
            else:
                new_coord[0] = 0
                new_coord[1] = self.snake_block
                self.check_snake_move_side = 'down'

        return new_coord

    def snake_eat_apple(self):
        self.snake_length += 1
        self.snake_speed += 0.5

    def snake_eat_pale(self):
        if self.snake_speed == 8:
            self.snake_speed = 12
        self.snake_length += 1
        self.snake_speed -= 0.5
