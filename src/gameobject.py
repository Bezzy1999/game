import pygame

class gameObject(object):
    def __init__(self, bitmap=None, startpos=None):
        self.speed = [0, 0]

        if bitmap:
            self.image = pygame.image.load(bitmap)
            self.rect = self.image.get_rect()

    def move(self):
        if self.rect:
            self.rect = self.rect.move(self.speed)

    def draw(self, screen):
        if self.rect:
            screen.blit(self.image, self.rect)
