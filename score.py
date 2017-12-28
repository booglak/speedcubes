import pygame


class Score:

    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont('TimesNewRoman', 25)
        self.text = self.font.render('Score: ' + str(self.score), 0, (0,0,0))

    def show(self, screen):
        screen.blit(self.text, [10, 5])

    def update_score(self):
        self.score += 1
        self.text = self.font.render('Score: ' + str(self.score), 0, (0, 0, 0))