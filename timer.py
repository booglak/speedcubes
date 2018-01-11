import time

class GameTimer:

    def __init__(self, round_timer):
        self.game_time = round_timer
        self.state = 0
        self.start_time = time.time()

    def start(self):
        self.start_time = time.time()

    def update(self):
        end_time = time.time()
        if (end_time - self.start_time) > self.game_time:
            self.state = 2


