import pygame
import os

class Player:
    def __init__(self):
        try:
            pygame.mixer.init()
        except pygame.error as e:
            print(f"Error initializing mixer: {e}")

    def __del__(self):
        pygame.mixer.quit()

    def play(self, file):

        try:
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        except pygame.error as e:
            raise Exception(f"Error playing audio: {e}")

if __name__ == '__main__':
    player = Player()
    player.play(r'D:\Documentos\English\English-tool-learnig\model\audio_files\pronunciation_hello_0.mp3')
