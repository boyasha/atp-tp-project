import random


class Globals:
    """
    Class for globals variables
    """
    # in pixels
    display_width = 800
    display_height = 600
    display_caption = 'Интересная змейка'

    # colors in RGB
    black_color = (0, 0, 0)
    white_color = (255, 255, 255)
    red_color = (213, 50, 80)
    green_color = (122, 230, 140)
    blue_color = (13, 143, 141)

    # snake data
    snake_list = []
    length_snake = 1


    # game data
    snake_block = 20
    snake_speed = 12
    food_block = 15

    # start point
    x_start = round(random.randrange(0, display_width - snake_block) / snake_block) * snake_block
    y_start = round(random.randrange(0, display_height - snake_block) / snake_block) * snake_block

    # change x and y when snake is moving
    new_coord = [0, 0]

    # text if you lose
    lose_message = "Ты проиграл! Нажми U - для игры заново или Q - для выхода."
    score_message = "Ваш счёт:"

    # x y coord of food
    x_food = round(random.randrange(0, display_width - food_block) / food_block) * food_block
    y_food = round(random.randrange(0, display_height - food_block) / food_block) * food_block