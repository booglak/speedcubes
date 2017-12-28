import time

class GameTimer:

    def __init__(self, round_timer):
        self.game_time = round_timer
        self.state = True
        self.start_time = time.time()

    def timer_update(self):
        end_time = time.time()
        if (end_time - self.start_time) > self.game_time:
            self.state = False


