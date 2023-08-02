from src.entites.enemy import Enemy
from src.config import *


class Wizard(Enemy):
    def __init__(self, x, y, player):
        super().__init__(x, y, WIZARD_SPEED, WIZARD_HP, WIZARD_POWER, WIZARD_WALK_ANIMATION, WIZARD_IDLE_ANIMATION,
                         WIZARD_DEATH_ANIMATION, WIZARD_INJURY_ANIMATION, WIZARD_ATTACK_ANIMATION, WIZARD_SCALE, player,
                         WIZARD_ATTACK_DISTANCE, SOUND_WIZARD_WALK, SOUND_WIZARD_DEATH, SOUND_WIZARD_DAMAGE, SOUND_WIZARD_ATTACK)
