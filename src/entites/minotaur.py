from src.entites.enemy import Enemy
from src.config import *


class Minotaur(Enemy):
    def __init__(self, x, y, player):
        super().__init__(x, y, MINOTAUR_SPEED, MINOTAUR_HP, MINOTAUR_POWER, MINOTAUR_WALK_ANIMATION,
                         MINOTAUR_ATTACK_ANIMATION, MINOTAUR_DEATH_ANIMATION, MINOTAUR_INJURY_ANIMATION,
                         MINOTAUR_IDLE_ANIMATION, MINOTAUR_SCALE, player, MINOTAUR_ATTACK_DISTANCE, SOUND_MINOTAUR_WALK,
                         SOUND_MINOTAUR_DEATH, SOUND_MINOTAUR_DAMAGE, SOUND_MINOTAUR_ATTACK)
