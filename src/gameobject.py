import pygame

class gameObject(object):
    def __init__(self, bitmap=None, startpos=None):

        if bitmap:
            self.image = pygame.image.load(bitmap)
            self.rect = self.image.get_rect()
            self.rect.x = startpos[0]
            self.rect.y = startpos[1]

    def move(self, speed):
        if self.rect:
            self.rect = self.rect.move(speed)

    def draw(self, screen):
        if self.rect:
            screen.blit(self.image, self.rect)
