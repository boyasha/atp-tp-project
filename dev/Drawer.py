import pygame
from Globals import Globals


class Drawer:
    """
    Class for drawing all object on display by Pygame library
    """

    def drawing_snake(self, display, color, position_array):
        pygame.draw.rect(display, color, position_array)

    def moving_snake(self, move_side):
        if move_side.key == pygame.K_LEFT or move_side.key == pygame.K_a or move_side.unicode == "ф":
            Globals.new_coord[0] = -10
            Globals.new_coord[1] = 0
        elif move_side.key == pygame.K_RIGHT or move_side.key == pygame.K_d or move_side.unicode == "в":
            Globals.new_coord[0] = 10
            Globals.new_coord[1] = 0
        elif move_side.key == pygame.K_UP or move_side.key == pygame.K_w or move_side.unicode == "ц":
            Globals.new_coord[0] = 0
            Globals.new_coord[1] = -10
        elif move_side.key == pygame.K_DOWN or move_side.key == pygame.K_s or move_side.unicode == "ы":
            Globals.new_coord[0] = 0
            Globals.new_coord[1] = 10

    def message(self, display, text, color):
        font_style = pygame.font.SysFont(None, 50)
        style_message = font_style.render(text, True, color)
        display.blit(style_message, [Globals.display_width/3 + 20, Globals.display_height/3 + 60])
