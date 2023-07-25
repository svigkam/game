import pygame


class RoomObject:
    def __init__(self, x, y, width, height, path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(path)
        self.rect = pygame.Rect(x, y, width, height)

    def update(self, display):
        display.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect
