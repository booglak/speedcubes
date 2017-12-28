import pygame
import sys


class GameOver:
    def __init__(self, settings):

        self.settings = settings
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        self.font = pygame.font.SysFont('TimesNewRoman', 100)
        self.text = self.font.render('GAME OVER', 50, (0, 0, 0))
        self.rect_screen = self.screen.get_rect()
        self.text_rect = self.text.get_rect()
        self.text_posx = self.rect_screen.centerx - self.text_rect.width/2
        self.text_posy = self.rect_screen.centery - self.text_rect.height / 2

    def play(self):
        while 1:
            self.screen.fill(self.settings.bg_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.blit(self.text, [self.text_posx, self.text_posy])
            pygame.display.flip()