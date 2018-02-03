import pygame
import gameobject
import random


class Ball(gameobject.gameObject):

    def __init__(self, startpos):
        super().__init__('./art/ballGrey.png', startpos)

        self.in_play = False
        self.speed = [0, 0]

    def move(self, paddle):
        if self.in_play:
            super().move(self.speed)
        else:
            self.rect.x = paddle.rect.x + 42
            self.rect.y = paddle.rect.y - 40

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and not self.in_play:
            self.speed = [random.choice([-2, 2]), -2]
            self.in_play = True