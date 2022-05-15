import random


class Globals:
    """
    Class for globals variables
    """

    def __init__(self):
        # in pixels
        self.display_width = 800
        self.display_height = 600
        self.display_caption = 'Интересная змейка'

        # colors in RGB
        self.black_color = (0, 0, 0)
        self.white_color = (255, 255, 255)
        self.red_color = (213, 50, 80)
        self.apple_color = (178, 34, 34)
        self.pear_color = (50, 205, 50)
        self.green_color = (122, 230, 140)

        # snake data
        self.snake_list = []
        self.length_snake = 1

        # game data
        self.snake_block = 20
        self.snake_speed = 12

        # start point
        self.x_start = round(
            random.randrange(0, self.display_width - self.snake_block) / self.snake_block) * self.snake_block
        self.y_start = round(
            random.randrange(0, self.display_height - self.snake_block) / self.snake_block) * self.snake_block

        # change x and y when snake is moving
        self.new_coord = [0, 0]

        # text if you lose
        self.lose_message = "Ты проиграл! Нажми U - для игры заново или Q - для выхода."
        self.score_message = "Ваш счёт:"

