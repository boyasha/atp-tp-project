import pygame
from Globals import Globals


class Drawer:
    """
    Class for drawing all object on display by Pygame library
    """

    def drawing_snake(self, display, color):
        for item in Globals.snake_list:
            pygame.draw.rect(display, color, [item[0], item[1], Globals.snake_block, Globals.snake_block],\
                             border_radius=5)

    def moving_snake(self, move_side):
        snake_block = Globals.snake_block

        if move_side.key == pygame.K_LEFT or move_side.key == pygame.K_a or move_side.unicode == "ф":
            Globals.new_coord[0] = -snake_block
            Globals.new_coord[1] = 0
        elif move_side.key == pygame.K_RIGHT or move_side.key == pygame.K_d or move_side.unicode == "в":
            Globals.new_coord[0] = snake_block
            Globals.new_coord[1] = 0
        elif move_side.key == pygame.K_UP or move_side.key == pygame.K_w or move_side.unicode == "ц":
            Globals.new_coord[0] = 0
            Globals.new_coord[1] = -snake_block
        elif move_side.key == pygame.K_DOWN or move_side.key == pygame.K_s or move_side.unicode == "ы":
            Globals.new_coord[0] = 0
            Globals.new_coord[1] = snake_block

    def message_of_lose(self, display, text, color):
        font_style = pygame.font.SysFont(None, 30)
        style_message = font_style.render(text, True, color)
        display.blit(style_message, [Globals.display_width/8, Globals.display_height/8 + 150])

    def message_of_score(self, display, text, color):
        font_style = pygame.font.SysFont(None, 40)
        style_message = font_style.render(text, True, color)
        display.blit(style_message, [10, 10])
