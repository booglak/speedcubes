import pygame
from enemy import Enemy
from event_helper import EventHelper
from score import Score
from timer import GameTimer
from game_over import GameOver


def play():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    event = EventHelper()
    enemy = Enemy(screen)
    enemy.random_position()
    score = Score()
    timer = GameTimer()

    while timer.state:
        screen.fill((0, 255, 0))
        event.event_listener(enemy, score)
        score.show(screen)
        enemy.show()
        pygame.display.flip()
        timer.timer_update()
    else:
        go = GameOver()
        go.play()


play()