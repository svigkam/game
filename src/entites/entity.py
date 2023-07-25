from enum import Enum

import pygame
from src.config import DEBUG, PLAYER_ATTACK_ANIMATION


class AnimationState(Enum):
    IDLE = "idle"
    INJURY = "injury"
    DEATH = "death"
    ATTACK = "attack"
    MOVING = "moving"



class Entity:
    def __init__(self, x, y, speed, power, hp, walk_animation, idle_animation, scale_factor):
        # Анимация и состояния
        self.walk_anim = [pygame.transform.scale_by(pygame.image.load(x), scale_factor) for x in walk_animation]
        self.idle_anim = [pygame.transform.scale_by(pygame.image.load(x), scale_factor) for x in idle_animation]
        self.attack_anim = [pygame.transform.scale_by(pygame.image.load(x), scale_factor) for x in PLAYER_ATTACK_ANIMATION]
        self.cur_anim = self.idle_anim
        self.anim_state = AnimationState.IDLE
        self.anim_index = 0
        self.anim_count = 0
        self.anim_delay = 6
        self.is_freeze = False
        self.is_dead = False
        self.is_watching_left = False

        # Коллизия, координаты сущности
        self.rect = self.idle_anim[0].get_rect()
        self.rect.x = x
        self.rect.y = y

        # Объекты в комнате
        self.collideObjects = None

        # Характеристики
        self.speed = speed
        self.power = power
        self.hp = hp

    def get_damage(self, damage):
        self.is_freeze = True
        self.hp -= damage
        if self.hp <= 0:
            self.death()
        else:
            self.changeAnimation(AnimationState.INJURY, True)

    def animate(self, display):
        # Счётчик анимации
        if self.anim_index >= len(self.cur_anim) - 1:
            self.anim_index = 0
            self.anim_count = 0
        if self.anim_count >= self.anim_delay:
            self.anim_count = 0
            self.anim_index += 1
        self.anim_count += 1

        # Текущий кадр
        cur_frame = self.cur_anim[self.anim_index]
        if self.is_watching_left:
            cur_frame = pygame.transform.flip(cur_frame, True, False)
        if self.anim_index + 1 == len(self.cur_anim) and self.is_freeze:
            self.is_freeze = False

        display.blit(cur_frame, self.rect)  # Отрисовка

    def update(self, display):
        if DEBUG:  # Debug
            self.debug(display)

        self.animate(display)  # Анимация

        if not self.is_freeze:  # Если не заморожен, то вкл idle анимация
            self.changeAnimation(AnimationState.IDLE)

    def move(self, is_x, is_y):  # is_x (+ вправо, - влево) is_y (+ вниз, - вверх)
        '''
        Движение опеределяется от знака входящих is_x и is_y
        Перемещение происходит прибавляя скорость помноженную на знак движения по координате

        block_hit_list содержит объекты, с которыми self.rect пересекается, затем идет итерация по массиву для отката

        :param is_x: Движение +вправо -влево
        :param is_y: Движение +вниз -вверх
        '''
        if not self.is_freeze:
            if is_x == 1:
                self.changeAnimation(AnimationState.MOVING)
                self.is_watching_left = False
            elif is_x == -1:
                self.changeAnimation(AnimationState.MOVING)
                self.is_watching_left = True
            if is_y == 1:
                pass
                # self.changeAnimation(AnimationState.MOVING_DOWN)
            elif is_y == -1:
                pass
                # self.changeAnimation(AnimationState.MOVING_UP)

            self.rect.centerx += self.speed * is_x
            block_hit_list = pygame.sprite.spritecollide(self, [x for x in self.collideObjects if x.isObstacle == True], 0)
            for block in block_hit_list:
                if is_x > 0:
                    self.rect.right = block.rect.left
                else:
                    self.rect.left = block.rect.right

            self.rect.centery += self.speed * is_y
            block_hit_list = pygame.sprite.spritecollide(self, [x for x in self.collideObjects if x.isObstacle == True], 0)
            for block in block_hit_list:
                if is_y > 0:
                    self.rect.bottom = block.rect.top
                else:
                    self.rect.top = block.rect.bottom



    def attack(self):
        self.changeAnimation(AnimationState.ATTACK, True)

    def changeAnimation(self, state, is_freeze=None):
        if is_freeze is not None:
            self.is_freeze = is_freeze
        self.anim_state = state

        anim_is_change = False

        match self.anim_state:
            case AnimationState.IDLE:
                if self.cur_anim != self.idle_anim:
                    self.cur_anim = self.idle_anim
                    anim_is_change = True
            case AnimationState.MOVING:
                if self.cur_anim != self.walk_anim:
                    self.cur_anim = self.walk_anim
                    anim_is_change = True
            case AnimationState.ATTACK:
                if self.cur_anim != self.attack_anim:
                    self.cur_anim = self.attack_anim
                    anim_is_change = True

        if anim_is_change and self.is_freeze:
            self.anim_index, self.anim_count = 0, 0

    def death(self):
        self.changeAnimation(AnimationState.DEATH, True)
        # TODO: вызов анимации с задержкой
        self.is_dead = True

    def debug(self, display):
        font = pygame.font.Font(None, 24)
        hp = font.render(f"HP: {self.hp}", 1, (0, 255, 0))
        display.blit(hp, (self.rect.x, self.rect.y - 30))
        pygame.draw.rect(display, (0, 255, 0), self.rect, 1, 1)
