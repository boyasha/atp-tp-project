import pygame


class Drawer:
    """
    Class for drawing all object on display by Pygame library
    """
    def __init__(self):
        pass

    def message_of_lose(self, display, text, color, Globals):
        font_style = pygame.font.SysFont(None, 30)
        style_message = font_style.render(text, True, color)
        display.blit(style_message, [Globals.display_width/8, Globals.display_height/8 + 150])

    def message_of_score(self, display, text, color):
        font_style = pygame.font.SysFont(None, 40)
        style_message = font_style.render(text, True, color)
        display.blit(style_message, [320, 10])
