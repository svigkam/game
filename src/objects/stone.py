import random

import pygame.image

from src.config import TILE_SIZE, DEBUG
from src.level.level_config import RoomObjects
from src.objects.roomObject import RoomObject


class Stone(RoomObject):
    def __init__(self, x, y):
        super().__init__(x, y, TILE_SIZE, TILE_SIZE, pygame.transform.scale(pygame.image.load(RoomObjects.STONE.value[random.randint(0, 5)]).convert_alpha(), (TILE_SIZE, TILE_SIZE)), is_obstacle=True)

    def update(self, display):
        super().update(display)

        if DEBUG:
            pygame.draw.rect(display, (125, 0, 255), self.rect, 1, 1)

