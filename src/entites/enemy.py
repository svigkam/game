import time

import pygame

from src.config import *
from src.entites.entity import Entity


class Enemy(Entity):
    def __init__(self, x, y, speed, hp, power, walk, idle, death, injury, attack, scale, player, radius, smove, sdie, sinj, sattack):
        super().__init__(x, y, speed, hp, power, walk, idle, death, injury, attack, scale, smove, sdie, sinj, sattack)
        self.player = player
        self.radius = radius
        self.attack_radius = pygame.Rect(0, 0, 0, 0)

    def update(self, display):
        super().update(display)
        self.update_attack_radius()

        if DEBUG:
            pygame.draw.rect(display, (255, 51, 51), self.attack_radius, 1, 1)

        if not self.attack_radius.colliderect(self.player.rect):
            self.move()
        else:
            self.attack()

    def update_attack_radius(self):
        self.attack_radius = pygame.Rect(self.rect.x - self.radius / 2,
                                         self.rect.y - self.radius / 2,
                                         self.rect.w + self.radius,
                                         self.rect.h + self.radius)

    def attack(self, **kwargs):
        if time.time() - self.prev_time > self.timer:
            self.prev_time = time.time()
            super().attack(self.player)

    def move(self, **kwargs):
        move_x = 0
        move_y = 0

        if self.player.rect.centerx < self.rect.centerx:
            move_x = -1
        elif self.player.rect.centerx > self.rect.centerx:
            move_x = 1
        if self.player.rect.centery > self.rect.centery:
            move_y = 1
        elif self.player.rect.centery < self.rect.centery:
            move_y = -1
        if move_x != 0 or move_y != 0:
            super().move(move_x, move_y)
