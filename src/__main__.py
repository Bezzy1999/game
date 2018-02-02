import sys
import pygame

import levels
from gameobject import gameObject

black = 0, 0, 0


def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 50

    screen = pygame.display.set_mode((640, 480))

    objects = []
    objects.append(gameObject('./art/ballGrey.png', startpos=(320, 368)))
    
    paddle = gameObject('./art/paddleBlu.png', startpos=(320, 400))
    objects.append(paddle)

    level = levels.createLevel(levels.levels[0])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill(black)
        levels.drawLevel(level, screen)

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            paddle.move([-3, 0])
        if key[pygame.K_RIGHT]:
            paddle.move([3, 0])

        for obj in objects:
            obj.draw(screen)

        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    main()