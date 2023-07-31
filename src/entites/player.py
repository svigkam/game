import time

import pygame

from src.config import *
from src.entites.entity import Entity, AnimationState
from src.level.level_config import RoomObjects
from src.objects.coin import Coin
from src.objects.door import Door
from src.objects.health import Health
from src.objects.key import Key
from src.objects.portal import Portal
from src.objects.spike import Spike


class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_SPEED, PLAYER_HP, PLAYER_POWER, PLAYER_WALK_ANIMATION, PLAYER_IDLE_ANIMATION,
                         PLAYER_DEATH_ANIMATION, PLAYER_INJURY_ANIMATION, PLAYER_ATTACK_ANIMATION, PLAYER_SCALE)
        self.prev_time, self.door_prev_time, self.spike_prev_timer = time.time(), time.time(), time.time()
        self.checking_timer = 0.3
        self.have_key = False
        self.attack_radius = pygame.Rect(0, 0, 0, 0)
        self.spike_radius = pygame.Rect(0, 0, 0, 0)
        self.coins = 0
        self.empty_level = False
        self.power = PLAYER_POWER
        self.e_key = pygame.image.load(RoomObjects.E_KEY.value)

    def update(self, display):
        super().update(display)
        self.update_attack_radius()
        self.checkObjectsInRoom(display)

        if DEBUG:
            pygame.draw.rect(display, (255, 0, 0), self.attack_radius, 1, 1)
            pygame.draw.rect(display, (255, 120, 0), self.spike_radius, 1, 1)

    def attack(self, enemies):
        if time.time() - self.prev_time > self.timer:
            self.prev_time = time.time()
            super().attack(None)
            for enemy in enemies:
                if self.attack_radius.colliderect(enemy.rect):
                    super().attack(enemy)

    def checkObjectsInRoom(self, display):
        # Проверка на дверь
        doors = [x for x in self.collideObjects if isinstance(x, Door) and self.attack_radius.colliderect(x.rect)]
        if doors and (not doors[0].closed or self.have_key) and self.empty_level:
            display.blit(self.e_key, self.e_key.get_rect(center=self.rect.center, y=self.rect.y - 45))

        # Проверка на дверь
        portal = [x for x in self.collideObjects if isinstance(x, Portal) and self.attack_radius.colliderect(x.rect)]
        if portal and self.empty_level:
            display.blit(self.e_key, self.e_key.get_rect(center=self.rect.center, y=self.rect.y - 45))

        # Проверка на ключ
        if not self.have_key:
            keys = [x for x in self.collideObjects if isinstance(x, Key) and self.rect.colliderect(x.rect)]
            if keys and self.rect.colliderect(keys[0].rect):
                keys[0].pick_up()
                self.have_key = True

        # Проверка на монеты
        coins = [x for x in self.collideObjects if isinstance(x, Coin) and self.rect.colliderect(x.rect)]
        if coins:
            for coin in coins:
                coin.pick_up()
                self.coins += 10

        # Проверка на шипы
        spikes = [x for x in self.collideObjects if isinstance(x, Spike) and self.spike_radius.colliderect(x.rect)]
        if spikes and (time.time() - self.spike_prev_timer > 0.7):
            self.spike_prev_timer = time.time()
            self.get_damage(1)

        # Проверка на аптечку
        health = [x for x in self.collideObjects if isinstance(x, Health) and self.rect.colliderect(x.rect)]
        if health:
            for item in health:
                item.pick_up()
                self.hp += 2

    def checkDoors(self):
        if time.time() - self.door_prev_time > self.checking_timer:
            self.door_prev_time = time.time()
            for door in [x for x in self.collideObjects if isinstance(x, Door)]:
                if self.attack_radius.colliderect(door.rect) and (not door.closed or self.have_key):
                    if door.closed:
                        door.closed = False
                        self.have_key = False
                    return door.direction
        return False

    def checkPortal(self) -> bool:
        if time.time() - self.door_prev_time > self.checking_timer:
            self.door_prev_time = time.time()
            for portal in [x for x in self.collideObjects if isinstance(x, Portal)]:
                if self.attack_radius.colliderect(portal.rect) and self.empty_level:
                    return True
        return False

    def update_attack_radius(self):
        self.spike_radius = pygame.Rect(self.rect.x - 5, self.rect.y - 5, self.rect.w + 10, self.rect.h + 10)
        self.attack_radius = pygame.Rect(self.rect.x - PLAYER_ATTACK_DISTANCE / 2,
                                         self.rect.y - PLAYER_ATTACK_DISTANCE / 2,
                                         self.rect.w + PLAYER_ATTACK_DISTANCE,
                                         self.rect.h + PLAYER_ATTACK_DISTANCE)
