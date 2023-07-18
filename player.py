import pygame.draw
from entity import Entity
from config import *


class Player(Entity):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, PLAYER_BASE_SPEED, PLAYER_BASE_POWER,
                         PLAYER_WALK_ANIMATION, PLAYER_IDLE_ANIMATION)
