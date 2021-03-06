import pygame
import sys


class EventHelper:

    # обработка ивентов извне (мышь, клава0

    def event_listener(self, enemy, score):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_click_on_enemy(enemy, event, score)

    # Обработка конкретного ивента в зависимости от его типа

    def mouse_click_on_enemy(self, enemy, event, score):
        if event.button == 1:
            pos = pygame.mouse.get_pos()
            if enemy.rect.x < pos[0] < enemy.rect.x+enemy.rect.width:
                if enemy.rect.y < pos[1] < enemy.rect.y+enemy.rect.height:
                    score.update_score()
                    enemy.random_size()
                    enemy.random_position(score)






