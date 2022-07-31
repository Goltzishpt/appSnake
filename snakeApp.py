import sys

import pygame

pygame.init()


class Snake():
    def __init__(self):
        pass


class Fruit():
    def __init__(self):
        pass


class Window():
    def __init__(self):
        pygame.display.set_mode((400, 400))


if __name__ == '__main__':
    window = Window()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()
