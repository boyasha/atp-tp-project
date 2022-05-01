import pygame
from Globals import Globals


class Display:
    pygame.init()
    display = pygame.display.set_mode([Globals.display_width, Globals.display_width])
    pygame.display.set_caption(Globals.display_caption)

    def showGameScore(self, score):
        value = self.score_font.render("Your score: " + str(score), True, self.yellow)
        self.display.blit(value, [0, 0])

    def drawingSnake(self, snakeBlock, snakeList):
        for i in snakeList:
            pygame.draw.rect(self.display, self.black, [i[0], i[1], snakeBlock, snakeList])

    def message(self, textOfMessage, color):
        self.display.blit(self.font_style.render(textOfMessage, True, color),
                          [self.displayWidth / 2, self.displayHeight / 2])

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

    pygame.quit()
    quit()
