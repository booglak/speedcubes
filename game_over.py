import pygame
import sys


class GameOver:
    def __init__(self, settings, score):
        self.state = 1
        self.settings = settings
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        self.rect_screen = self.screen.get_rect()

        # Текст GAME OVER

        self.go_font = pygame.font.SysFont('TimesNewRoman', 100)
        self.go_text = self.go_font.render('GAME OVER', 50, (0, 0, 0))
        self.go_text_rect = self.go_text.get_rect()
        self.go_text_posx = self.rect_screen.centerx - self.go_text_rect.width / 2
        self.go_text_posy = self.rect_screen.centery - self.go_text_rect.height / 2

        # Text "Your Score"

        self.ys_font = pygame.font.SysFont('TimesNewRoman', 50)
        self.ys_text = self.ys_font.render('Your Score: ' + str(score.score), 50, (0, 0, 0))
        self.ys_text_rect = self.ys_text.get_rect()
        self.ys_text_posx = self.rect_screen.centerx - self.ys_text_rect.width / 2
        self.ys_text_posy = self.rect_screen.centery - self.ys_text_rect.height * 2

        # Text "Try Again"

        self.ta_font = pygame.font.SysFont('TimesNewRoman', 50)
        self.ta_text = self.ta_font.render('Try Again', 50, (0, 0, 0))
        self.ta_text_rect = self.ta_text.get_rect()
        self.ta_text_posx = self.rect_screen.centerx - self.ta_text_rect.width / 2
        self.ta_text_posy = self.rect_screen.centery + self.ta_text_rect.height * 1.2


    def play(self):
        while self.state:
            self.screen.fill(self.settings.bg_color)
            self.screen.blit(self.go_text, [self.go_text_posx, self.go_text_posy])
            self.screen.blit(self.ys_text, [self.ys_text_posx, self.ys_text_posy])
            self.screen.blit(self.ta_text, [self.ta_text_posx, self.ta_text_posy])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        if self.ta_text_posx < pos[0] < self.ta_text_posx + self.ta_text_rect.width:
                            if self.ta_text_posy < pos[1] < self.ta_text_posy + self.ta_text_rect.height:
                                self.state = 0

            pygame.display.flip()