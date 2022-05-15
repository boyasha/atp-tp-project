import pygame


class Message:
    """
    Class for drawing all object on display by Pygame library
    """
    def __init__(self, display_width, display_height):
        self.display_width = display_width
        self.display_height = display_height

        self.text_of_lose = "Ты проиграл! Нажми U - для игры заново или Q - для выхода."
        self.text_of_score = "Ваш счёт: "

        self.color_message_of_lose = (213, 50, 80)
        self.color_message_of_score = (255, 255, 255)

    def message_of_lose(self, display):
        font_style = pygame.font.SysFont(None, 30)
        style_message = font_style.render(self.text_of_lose, True, self.color_message_of_lose)
        display.blit(style_message, [self.display_width/8, self.display_height/8 + 150])

    def message_of_score(self, display, score):
        font_style = pygame.font.SysFont(None, 40)
        style_message = font_style.render(f'{self.text_of_score} {score-1}', True, self.color_message_of_score)
        display.blit(style_message, [320, 10])
