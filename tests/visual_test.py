import sys
import pygame

import ball
import collide

black = 0, 0, 0
red = (255, 0, 0)
blue = (0, 0, 255)
radius = 30

class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

rect = pygame.Rect(400, 400, 60, 100)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 50

    screen = pygame.display.set_mode((1200, 800))

    ball_pos = point(300, 400)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill(black)

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            ball_pos.x -= 1
        if key[pygame.K_RIGHT]:
            ball_pos.x += 1
        if key[pygame.K_UP]:
            ball_pos.y -= 1
        if key[pygame.K_DOWN]:
            ball_pos.y += 1

        #collide.check(theBall, level, paddle)

        pygame.draw.circle(pygame.display.get_surface(),
                        red, 
                        [ball_pos.x, ball_pos.y],
                        radius, 0)

        pygame.draw.rect(pygame.display.get_surface(),
                        blue if collide.collideBallVsRect(
                            ball_pos, radius, rect) else red,
                        rect
                        )


        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    main()