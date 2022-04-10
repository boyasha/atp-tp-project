import pygame


class Display():
    displayWidth = 600
    displayHeight = 400

    def __init__(self, displayWidth, displayHeight):
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight

    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    display = pygame.display.set_mode((self.displayWidth, self.isplayHeight))
    pygame.display.set_caption('Interesting Snake Game')

    snake_block = 10
    snake_speed = 15

    font_style = pygame.font.SysFont("spendthrift", 25)
    score_font = pygame.font.SysFont("cosmeticians", 35)

    def showGameScore(self, score):
        value = self.score_font.render("Your score: " + str(score), True, self.yellow)
        self.display.blit(value, [0, 0])

    def drawingSnake(self, snakeBlock, snakeList):
        for i in snakeList:
            pygame.draw.rect(self.display, self.black, [i[0], i[1], snakeBlock, snakeList])

    def message(self, textOfMessage, color):
        self.display.blit(self.font_style.render(textOfMessage, True, color), [self.displayWidth/2, self.displayHeight/2])
