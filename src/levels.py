import pygame

level1 = [
"BBBBBBBBBBBBBBBBBBBB",
"B                  B",
"B                  B",
"B                  B",
"B                  B",
"B                  B",
"B                  B",
"B                  B",
"B                  B",
"B                  B",
"B                  B",
"B                  B",
"B                  B",
"B                  B",
"B                  B",
]

levels = [
    level1
]

level_image = pygame.image.load('art/element_blue_square.png')

def createLevel(level):
    rects = []
    for row_index, row in enumerate(level):
        for col_index, col in enumerate(row):
            if col == 'B':
                rects.append(pygame.Rect(col_index * 32, row_index * 32, 32, 32))

    return rects

def drawLevel(rects, screen):
    for rect in rects:
        screen.blit(level_image, rect)
