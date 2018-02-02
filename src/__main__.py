import sys
import pygame

black = 0, 0, 0

class gameObject(object):
    def __init__(self, bitmap=None):
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

def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 50

    screen = pygame.display.set_mode((640, 480))

    objects = []
    objects.append(gameObject('./art/ballGrey.png'))

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