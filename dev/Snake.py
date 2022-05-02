import pygame


class Snake:
    """
    Class for logic of game
    """

    def __init__(self):
        pass

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
            new_coord[0] = -snake_block
            new_coord[1] = 0
        elif move_side.key == pygame.K_RIGHT or move_side.key == pygame.K_d or move_side.unicode == "в":
            new_coord[0] = snake_block
            new_coord[1] = 0
        elif move_side.key == pygame.K_UP or move_side.key == pygame.K_w or move_side.unicode == "ц":
            new_coord[0] = 0
            new_coord[1] = -snake_block
        elif move_side.key == pygame.K_DOWN or move_side.key == pygame.K_s or move_side.unicode == "ы":
            new_coord[0] = 0
            new_coord[1] = snake_block

        return new_coord
