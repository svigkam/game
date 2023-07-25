import time

import pygame

from src.objects.blade import Blade

from src.config import *
from src.entites.entity import Entity
from src.objects.door import Door


class Player(Entity):
    def __init__(self, x, y):
        self.blade = Blade()
        self.prev_time = time.time()
        self.door_timer = 0.5
        self.attack_timer = 2
        super().__init__(x, y, PLAYER_BASE_SPEED, self.blade.get_blade_power(), PLAYER_BASE_HP,
                         PLAYER_WALK_ANIMATION, PLAYER_IDLE_ANIMATION, PLAYER_SCALE)
        self.attack_radius = pygame.Rect(0, 0, 0, 0)

    def update(self, display):
        super().update(display)
        self.power = self.blade.get_blade_power()
        self.attack_radius = pygame.Rect(self.rect.x - PLAYER_ATTACK_DISTANCE / 2,
                                         self.rect.y - PLAYER_ATTACK_DISTANCE / 2, self.rect.w + PLAYER_ATTACK_DISTANCE,
                                         self.rect.h + PLAYER_ATTACK_DISTANCE)
        pygame.draw.rect(display, (255, 0, 0), self.attack_radius, 1, 1)

    def attack(self, enemies):
        super().attack()
        for enemy in enemies:
            if self.attack_radius.colliderect(enemy.rect):
                enemy.get_damage(self.power)

    def checkDoors(self):
        if time.time() - self.prev_time > self.door_timer:
            self.prev_time = time.time()
            for door in [x for x in self.collideObjects if x.is_door]:
                if self.attack_radius.colliderect(door.rect) and not door.closed:
                    print("Ты поменял комнату", door.direction)
                    return door.direction
        return False
