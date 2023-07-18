from entity import Entity
from config import *


class Enemy(Entity):
    def __init__(self, x, y, width, height, player):
        super().__init__(x, y, width, height, NORMAL_ENEMY_BASE_SPEED, NORMAL_ENEMY_BASE_POWER,
                         PLAYER_WALK_ANIMATION, PLAYER_IDLE_ANIMATION)
        self.player = player

    def update(self, display):
        super().update(display)
        self.move()

    def move(self, **kwargs):
        move_x = 0
        move_y = 0

        if self.player.x < self.x:
            move_x = -1
        elif self.player.x > self.x:
            move_x = 1

        if self.player.y > self.y:
            move_y = 1
        elif self.player.y < self.y:
            move_y = -1

        if move_x != 0 or move_y != 0:
            super().move(move_x, move_y)
