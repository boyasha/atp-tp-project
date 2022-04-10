import pygame


class Display():
    def __init__(self, displayWidth=600, displayHeight=400):
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight

    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    display = pygame.display.set_mode(displayWidth, displayHeight))
    pygame.display.set_caption('Interesting Snake Game')

    snake_block = 10
    snake_speed = 15

    font_style = pygame.font.SysFont("spendthrift", 25)
    score_font = pygame.font.SysFont("cosmeticians", 35)
