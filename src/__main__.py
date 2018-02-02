import sys
import pygame

from levels import levels
from gameobject import gameObject

black = 0, 0, 0


def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 50

    screen = pygame.display.set_mode((640, 480))

    objects = []
    objects.append(gameObject('./art/ballGrey.png'))
    objects.append(gameObject('./art/paddleBlu.png'))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill(black)

        for obj in objects:
            obj.move()
            obj.draw(screen)

        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    main()