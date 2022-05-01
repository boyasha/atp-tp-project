class Globals:
    """
    Class for globals variables
    """
    # in pixels
    display_width = 800
    display_height = 600
    display_caption = 'Интересная змейка'

    # colors in RGB
    white_color = (255, 255, 255)
    yellow_color = (255, 255, 102)
    black_color = (0, 0, 0)
    red_color = (213, 50, 80)
    green_color = (0, 255, 0)
    blue_color = (50, 153, 213)

    # in pixels
    snake_block = 20
    snake_speed = 25

    # start point
    x_start = 300
    y_start = 200

    # change x and y when snake is moving
    new_coord = [0, 0]

    # text if you lose
    lose_message = "Ты проиграл!"
