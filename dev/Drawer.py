import pygame
from Globals import Globals


class Drawer:
    """
    Class for drawing all object on display by Pygame library
    """

    def drawing_snake(self, display, color, position_array):
        return pygame.draw.rect(display, color, position_array)

    def moving_snake(self, move_side):
        if move_side == pygame.K_LEFT or move_side == pygame.K_a:
            Globals.new_coord[0] = -10
            Globals.new_coord[1] = 0
        elif move_side == pygame.K_RIGHT or move_side == pygame.K_d:
            Globals.new_coord[0] = 10
            Globals.new_coord[1] = 0
        elif move_side == pygame.K_UP or move_side == pygame.K_w:
            Globals.new_coord[0] = 0
            Globals.new_coord[1] = -10
        elif move_side == pygame.K_DOWN or move_side == pygame.K_s:
            Globals.new_coord[0] = 0
            Globals.new_coord[1] = 10
