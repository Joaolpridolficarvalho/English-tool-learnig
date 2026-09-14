import pygame
import os
import pathlib

class Player:
    def __init__(self):
        try:
            pygame.mixer.init()
            self.available = True
        except pygame.error as e:
            print(f"Audio playback is not available: {e}")
            self.available = False
    def __del__(self):
        if self.available:
            pygame.mixer.quit()

    def play(self, file):
        print(f"Playing audio: {file}")
        if not self.available:
            return False

        try:
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            return True
        except (pygame.error, FileNotFoundError, AttributeError) as e:
            print(f"Audio playback failed: {e}")
            return False


if __name__ == "__main__":
    player = Player()
    player.play(
os.path.join(pathlib.Path(__file__).parent.resolve(), "Test.mp3")
    )
