import pygame


class Game:
    def __init__(self):
        pass

    def game(self, Globals, Drawer, Snake, Display, display, game_close, game_over):
        while game_close:
            display.fill(Globals.black_color)
            Drawer.message_of_lose(display)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.unicode == "й":
                        return True
                    if event.key == pygame.K_u or event.unicode == "г":
                        Display.__init__()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                return True
            if event.type == pygame.KEYDOWN:
                Display.new_coord = Snake.moving_snake(event)
