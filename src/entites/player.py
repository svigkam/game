import time

from src.objects.blade import Blade

from src.config import *
from src.entites.entity import Entity


class Player(Entity):
    def __init__(self, x, y, width, height):
        self.blade = Blade()
        self.attack_start_time = time.time()
        self.timer = 1
        super().__init__(x, y, width, height, PLAYER_BASE_SPEED, self.blade.get_blade_power(), PLAYER_BASE_HP,
                         PLAYER_WALK_ANIMATION, PLAYER_IDLE_ANIMATION)

    def update(self, display):
        super().update(display)
        self.power = self.blade.get_blade_power()
        if time.time() - self.attack_start_time > self.timer:
            self.is_attack = False

    def attack(self, enemies, pos, btn):
        if time.time() - self.attack_start_time > self.timer:
            if btn[0]:
                super().attack()
                self.timer = 1
            elif btn[2]:
                super().attack(1)
                # TODO: Бросок клинка по pos(x,y) и возврат бумерангом
                self.timer = 2

            if self.is_attack or self.is_throw_attack:
                self.attack_start_time = time.time()

                rect = self.rect

                for enemy in enemies:
                    if rect.colliderect(enemy.rect):
                        enemy.get_damage(self.power)

    def leftAttack(self):
        pass
    def rightAttack(self):
        pass
