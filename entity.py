import random

import pygame

from config import *


class Entity:
    def __init__(self, x, y, width, height, speed, power, walk_animation, idle_animation):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.animation_count = 0
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.walk_animation = [pygame.image.load(x) for x in walk_animation]
        self.idle_animation = [pygame.image.load(x) for x in idle_animation]

        self.speed = speed
        self.power = power

    def animate(self, display):
        # MOVE ANIMATION
        if self.moving_right:
            display.blit(
                pygame.transform.scale(self.walk_animation[self.animation_count//4], (self.width, self.height)),
                (self.x, self.y))
        elif self.moving_left:
            display.blit(
                pygame.transform.scale(
                    pygame.transform.flip(self.walk_animation[self.animation_count // 4], True, False), (self.width, self.height)
                ), (self.x, self.y))
        else:
            display.blit(pygame.transform.scale(self.idle_animation[self.animation_count // 8], (self.width, self.height)
                ), (self.x, self.y))

    def update(self, display):
        if self.animation_count + 1 >= 32:
            self.animation_count = 0
        self.animation_count += 1

        self.animate(display)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def move(self, is_x, is_y):
        if is_x == 1:
            self.moving_right = True
        elif is_x == -1:
            self.moving_left = True
        if is_y == 1:
            self.moving_down = True
        elif is_y == -1:
            self.moving_up = True

        self.x += self.speed * is_x
        self.y += self.speed * is_y
