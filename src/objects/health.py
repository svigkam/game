import pygame.image

from src.config import TILE_SIZE, DEBUG, SOUND_HEALTH_UP
from src.level.level_config import RoomObjects
from src.objects.roomObject import RoomObject


class Health(RoomObject):
    def __init__(self, x, y):
        self.anim = [pygame.transform.scale2x(pygame.image.load(x)) for x in RoomObjects.HEALTH.value]
        self.anim_index = 0
        self.anim_count = 0
        self.anim_delay = 6
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
            pygame.draw.rect(display, (125, 142, 255), self.rect, 1, 1)

    def pick_up(self):
        pygame.mixer.Sound(SOUND_HEALTH_UP).play()
        super().pick_up()