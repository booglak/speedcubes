import pygame
from enemy import Enemy
from event_helper import EventHelper
from score import Score
from start_screen import StartScreen
from timer import GameTimer
from game_over import GameOver
from settings import Settings


def play():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    event = EventHelper()
    enemy = Enemy(screen)
    score = Score()
    enemy.random_position(score)
    timer = GameTimer(settings.round_timer)

    while 1:

        # пока таймер нейтральный (0) рисуем стартовый экран

        if timer.state == 0:
            ss = StartScreen(settings)
            ss.play()
            timer.state = 1
            timer.start()

        # пока таймер тикает (1) рисуем главный экран

        while timer.state == 1:
            screen.fill(settings.bg_color)
            event.event_listener(enemy, score)
            score.show(screen)
            enemy.show()
            pygame.display.flip()
            timer.update()

        # когда таймер закончился (2) рисуем экран ГеймОвер

        if timer.state == 2:
            g_o = GameOver(settings, score)

            # Write Score into file

            file_score = open('topscore.txt', 'w')
            file_score.write(str(score.score))
            file_score.close()

            g_o.play()
            timer.state = 0


play()