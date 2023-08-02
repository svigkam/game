import pygame.image

from src.config import TILE_SIZE, DEBUG, SOUND_COIN_UP
from src.level.level_config import RoomObjects
from src.objects.roomObject import RoomObject


class Coin(RoomObject):
    def __init__(self, x, y):
        self.anim = [pygame.transform.scale_by(pygame.image.load(x), 2) for x in RoomObjects.COIN.value]
        self.anim_index = 0
        self.anim_count = 0
        self.anim_delay = 7
        super().__init__(x, y, TILE_SIZE, TILE_SIZE, self.anim[0], is_obstacle=False)

    def update(self, display):
        if self.anim_index >= len(self.anim) - 1:
            self.anim_index = 0
            self.anim_count = 0
        if self.anim_count >= self.anim_delay:
            self.anim_count = 0
            self.anim_index += 1
        self.anim_count += 1

        self.image = self.anim[self.anim_index]
        super().update(display)

        if DEBUG:
            pygame.draw.rect(display, (255, 255, 0), self.rect, 1, 1)


    def pick_up(self):
        pygame.mixer.Sound(SOUND_COIN_UP).play()
        super().pick_up()