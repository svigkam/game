from src.entites.enemy import Enemy
from src.config import *


class Zombie(Enemy):
    def __init__(self, x, y, player):
        super().__init__(x, y, ZOMBIE_SPEED, ZOMBIE_HP, ZOMBIE_POWER, ZOMBIE_WALK_ANIMATION, ZOMBIE_IDLE_ANIMATION,
                         ZOMBIE_DEATH_ANIMATION, ZOMBIE_INJURY_ANIMATION, ZOMBIE_ATTACK_ANIMATION, ZOMBIE_SCALE, player,
                         ZOMBIE_ATTACK_DISTANCE, SOUND_ZOMBIE_WALK, SOUND_ZOMBIE_DEATH, SOUND_ZOMBIE_DAMAGE, SOUND_ZOMBIE_ATTACK)
