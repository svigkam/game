import pygame

from src.config import TILE_SIZE
from src.objects.roomObject import RoomObject

class Wall(RoomObject):
    def __init__(self, x, y, path):
        super().__init__(x, y, TILE_SIZE, TILE_SIZE)
        self.image = pygame.image.load(path)
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

    def update(self, display):
        display.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect



