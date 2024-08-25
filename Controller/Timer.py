import time

class Timer:
    def __init__(self):
        self.interval_seconds = 0

    def set_interval(self, interval):
        self.interval_seconds = interval

    def start(self):
        time.sleep(self.interval_seconds)
        print('Time is up!')



if __name__ == '__main__':
    timer = Timer()
    timer.set_interval(10)
    timer.start()

