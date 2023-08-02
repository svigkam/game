from src.entites.enemy import Enemy
from src.config import *


class Snake(Enemy):
    def __init__(self, x, y, player):
        super().__init__(x, y, SNAKE_SPEED, SNAKE_HP, SNAKE_POWER, SNAKE_WALK_ANIMATION, SNAKE_IDLE_ANIMATION,
                         SNAKE_DEATH_ANIMATION, SNAKE_INJURY_ANIMATION, SNAKE_ATTACK_ANIMATION, SNAKE_SCALE, player,
                         SNAKE_ATTACK_DISTANCE, SOUND_SNAKE_WALK, SOUND_SNAKE_DEATH, SOUND_SNAKE_DAMAGE, SOUND_SNAKE_ATTACK)
