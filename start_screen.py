import pygame
import sys


class StartScreen:
    def __init__(self, settings):

        self.settings = settings
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        self.font = pygame.font.SysFont('TimesNewRoman', 100)
        self.text = self.font.render('Start Game', 50, (0, 0, 0))
        self.rect_screen = self.screen.get_rect()
        self.text_rect = self.text.get_rect()
        self.text_posx = self.rect_screen.centerx - self.text_rect.width/2
        self.text_posy = self.rect_screen.centery - self.text_rect.height / 2
        self.state = 1

    def play(self):
        while self.state:
            self.screen.fill(self.settings.bg_color)
            self.screen.blit(self.text, [self.text_posx, self.text_posy])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        if self.text_posx < pos[0] < self.text_posx + self.text_rect.width:
                            if self.text_posy < pos[1] < self.text_posy + self.text_rect.height:
                                self.state = 0

            pygame.display.flip()