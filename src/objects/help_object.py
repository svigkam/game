import pygame.image

from src.config import TILE_SIZE


class HelpObject:
    def __init__(self, x, y, path=None, anim=None):
        self.x = x
        self.y = y
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.is_anim = anim is not None
        if anim is not None:
            self.anim = [pygame.image.load(x) for x in anim]
        if path is not None:
            self.image = pygame.image.load(path)
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

        self.is_collectable = False
        self.isObstacle = False
        self.to_clear = False
        self.visible = True

        self.anim_index = 0
        self.anim_count = 0

    def update(self, display):
        if self.is_anim:
            if self.anim_index >= len(self.anim) - 1:
                self.anim_index = 0
                self.anim_count = 0
            if self.anim_count >= 6:
                self.anim_count = 0
                self.anim_index += 1
            self.anim_count += 1

            self.image = self.anim[self.anim_index]
        display.blit(self.image, self.image.get_rect(center=(self.rect.center)))
