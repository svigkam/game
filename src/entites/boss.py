import pygame

from src.entites.enemy import Enemy
from src.config import *


class Boss(Enemy):
    def __init__(self, x, y, player):
        super().__init__(x, y, BOSS_SPEED, BOSS_HP, BOSS_POWER, BOSS_WALK_ANIMATION,
                         BOSS_ATTACK_ANIMATION, BOSS_DEATH_ANIMATION, BOSS_INJURY_ANIMATION,
                         BOSS_IDLE_ANIMATION, BOSS_SCALE, player, BOSS_ATTACK_DISTANCE, SOUND_PLAYER_WALK,
                         SOUND_PLAYER_DEATH, SOUND_PLAYER_DAMAGE, SOUND_PLAYER_ATTACK)

    def update(self, display):
        super().update(display)
        if self.hp > 0:
            pygame.draw.rect(display, "red", (self.rect.topleft[0], self.rect.centery - self.rect.h, self.rect.w, 3))
            pygame.draw.rect(display, "green",
                             (self.rect.topleft[0], self.rect.centery - self.rect.h,
                              self.rect.w * (self.hp / self.max_hp),
                              3))
