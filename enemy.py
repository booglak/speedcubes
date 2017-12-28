import random

import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):

    def __init__(self, screen):
        super().__init__()
        self.width = 20
        self.height = 20
        self.color = (200, 200, 0)
        self.screen = screen
        self.size = 0

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect_screen = screen.get_rect()

    def show(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def random_position(self):
        self.rect.x = random.randint(0, self.rect_screen.right-self.rect.width)
        self.rect.y = random.randint(0, self.rect_screen.bottom-self.rect.height)

    def random_size(self):
        self.size = random.randint(0, 2)
        if self.size == 0:
            self.rect.width = 20
            self.rect.height = 20
        elif self.size == 1:
            self.rect.width = 40
            self.rect.height = 40
        elif self.size == 2:
            self.rect.width = 60
            self.rect.height = 60


