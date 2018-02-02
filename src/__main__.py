import sys
import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((640, 480))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

if __name__ == '__main__':
    main()