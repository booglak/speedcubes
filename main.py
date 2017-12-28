import pygame
from enemy import Enemy
from event_helper import EventHelper
from score import Score
from timer import GameTimer
from game_over import GameOver
from settings import Settings


def play():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    event = EventHelper()
    enemy = Enemy(screen)
    enemy.random_position()
    score = Score()
    timer = GameTimer(settings.round_timer)

    while timer.state:
        screen.fill(settings.bg_color)
        event.event_listener(enemy, score)
        score.show(screen)
        enemy.show()
        pygame.display.flip()
        timer.timer_update()
    else:
        g_o = GameOver(settings)
        g_o.play()


play()