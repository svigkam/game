import pygame.transform

from src.config import TILE_SIZE, DEBUG
from src.level.level_config import RoomObjects
from src.level.room import loadImage
from src.objects.roomObject import RoomObject


class Door(RoomObject):
    def __init__(self, x, y, path, rotation, direction, closed=False):
        super().__init__(x, y, TILE_SIZE, TILE_SIZE, pygame.transform.scale(
            pygame.transform.rotate(pygame.image.load(path).convert_alpha(), rotation),
            [TILE_SIZE, TILE_SIZE]).convert_alpha(), is_obstacle=True)
        self.direction = direction
        self.closed = closed
        if self.closed:
            self.lock_image = pygame.transform.rotate(pygame.image.load(RoomObjects.LOCK.value).convert_alpha(), rotation)

    def update(self, display):
        super().update(display)
        if self.closed:
            display.blit(self.lock_image, self.rect)
        if DEBUG:
            pygame.draw.rect(display, (200, 100, 50) if self.closed else (0, 255, 255), self.rect, 1, 1)
