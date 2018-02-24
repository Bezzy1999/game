import sys
import math
import pygame

import ball
import collide

black = 0, 0, 0
red = (255, 0, 0)
blue = (0, 0, 255)
radius = 30

class vec():
    def __init__(self, x, y):
        self.x = x
        self.y = y

rect = pygame.Rect(400, 400, 60, 100)

def draw_current_state(ball_pos_start, ball_velocity):
    pygame.draw.circle(pygame.display.get_surface(),
                red, 
                [ball_pos_start.x, ball_pos_start.y],
                radius, 1)

    pygame.draw.circle(pygame.display.get_surface(),
                red, 
                [ball_pos_start.x + ball_velocity.x, ball_pos_start.y + ball_velocity.y],
                radius, 1)

    scalarSq = (ball_velocity.x * ball_velocity.x) + \
                (ball_velocity.y * ball_velocity.y)

    scalar = math.sqrt(scalarSq)

    normal = vec(
            ball_velocity.x / scalar,
            ball_velocity.y / scalar
        )

    left_normal = vec(
        -normal.y, normal.x
        )
    right_normal = vec(
        normal.y, -normal.x
        )

    left_start = vec(
        ball_pos_start.x + \
            (left_normal.x * radius),
        ball_pos_start.y + \
            (left_normal.y * radius)
        )

    left_end = vec(
        ball_pos_start.x + ball_velocity.x + \
            (left_normal.x * radius),
        ball_pos_start.y + ball_velocity.y + \
            (left_normal.y * radius)
        )

    right_start = vec(
        ball_pos_start.x + \
            (right_normal.x * radius),
        ball_pos_start.y + \
            (right_normal.y * radius)
        )

    right_end = vec(
        ball_pos_start.x + ball_velocity.x + \
            (right_normal.x * radius),
        ball_pos_start.y + ball_velocity.y + \
            (right_normal.y * radius)
        )

    pygame.draw.line(pygame.display.get_surface(),
                red, 
                [left_start.x, left_start.y],
                [left_end.x, left_end.y])

    pygame.draw.line(pygame.display.get_surface(),
                red, 
                [right_start.x, right_start.y],
                [right_end.x, right_end.y])

def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 50

    screen = pygame.display.set_mode((1200, 800))

    ball_pos_start = vec(300, 400)
    ball_velocity = vec(3, 4)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill(black)

        key = pygame.key.get_pressed()

        adjust = vec(0,0)
        if key[pygame.K_LEFT]:
            adjust.x = -1
        if key[pygame.K_RIGHT]:
            adjust.x = 1
        if key[pygame.K_UP]:
            adjust.y = -1
        if key[pygame.K_DOWN]:
            adjust.y = 1
        if key[pygame.K_SPACE]:
            ball_velocity.x += adjust.x
            ball_velocity.y += adjust.y
        else:
            ball_pos_start.x += adjust.x
            ball_pos_start.y += adjust.y

        #collide.check(theBall, level, paddle)
        draw_current_state(ball_pos_start, ball_velocity)

        pygame.draw.circle(pygame.display.get_surface(),
                        red, 
                        [ball_pos_start.x, ball_pos_start.y],
                        radius, 1)

        pygame.draw.circle(pygame.display.get_surface(),
                        red, 
                        [ball_pos_start.x + ball_velocity.x, ball_pos_start.y + ball_velocity.y],
                        radius, 1)

        pygame.draw.rect(pygame.display.get_surface(),
                        blue if collide.collideBallVsRect(
                            ball_pos_start, radius, rect) else red,
                        rect
                        )


        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    main()