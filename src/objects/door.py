import pygame.transform

from src.config import TILE_SIZE, DEBUG
from src.objects.roomObject import RoomObject


class Door(RoomObject):
    def __init__(self, x, y, path, rotation, direction):
        super().__init__(x, y, TILE_SIZE, TILE_SIZE, path, is_obstacle=True)
        self.image = pygame.transform.scale(pygame.transform.rotate(self.image, rotation), [TILE_SIZE, TILE_SIZE])
        self.direction = direction
        self.is_door = True
        self.closed = False

    def update(self, display):
        super().update(display)
        if DEBUG: pygame.draw.rect(display, (0, 0, 255), self.rect, 1, 1)
