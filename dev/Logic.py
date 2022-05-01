from Globals import Globals
import pygame


class Logic:
    """
    Class for logic of game
    """

    def check_border_crossing(self, check_game_over, display_width, display_height, x, y):
        if x >= display_width or x < 0 or y >= display_height or y < 0:
            check_game_over = True
        return check_game_over
