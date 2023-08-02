import time
from enum import Enum

import pygame
from src.config import DEBUG


class AnimationState(Enum):
    IDLE = "idle"
    INJURY = "injury"
    DEATH = "death"
    ATTACK = "attack"
    MOVING = "moving"


class Entity:
    def __init__(self, x, y, speed, hp, power, walk_anim, idle_anim, death_anim, injury_anim, attack_anim, scale_factor, smove, sdeath, sinjury, sattack):
        # Анимация и состояния
        self.walk_anim = [pygame.transform.scale_by(pygame.image.load(x), scale_factor) for x in walk_anim]
        self.idle_anim = [pygame.transform.scale_by(pygame.image.load(x), scale_factor) for x in idle_anim]
        self.death_anim = [pygame.transform.scale_by(pygame.image.load(x), scale_factor) for x in death_anim]
        self.injury_anim = [pygame.transform.scale_by(pygame.image.load(x), scale_factor) for x in injury_anim]
        self.attack_anim = [pygame.transform.scale_by(pygame.image.load(x), scale_factor) for x in attack_anim]

        self.sound_move = smove
        self.sound_injury = sinjury
        self.sound_death = sdeath
        self.sound_attack = sattack

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
        self.max_hp = hp
        self.hp = hp
        self.ratio = 1

        self.timer = 1
        self.prev_time = time.time()

    def get_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.death()
        else:
            pygame.mixer.Sound(self.sound_injury).play()
            self.ratio -= 0.00001
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
        if self.anim_index + 1 == len(self.cur_anim):
            if self.anim_state == AnimationState.DEATH:
                self.is_dead = True
            self.changeAnimation(AnimationState.IDLE, force=True)

        display.blit(cur_frame, self.rect)  # Отрисовка

    def update(self, display):
        if DEBUG:  # Debug
            self.debug(display)

        if self.ratio != 1 and DEBUG:
            self.showHealth(display)
        self.animate(display)  # Анимация

        if not self.is_freeze:
            self.changeAnimation(AnimationState.IDLE)

    def move(self, is_x, is_y):  # is_x (+ вправо, - влево) is_y (+ вниз, - вверх)
        if not self.is_freeze:
            # pygame.mixer.Sound(self.sound_move).play()
            if is_x == 1:
                self.changeAnimation(AnimationState.MOVING)
                self.is_watching_left = False
            elif is_x == -1:
                self.changeAnimation(AnimationState.MOVING)
                self.is_watching_left = True

            self.rect.centerx += self.speed * is_x

            block_hit_list = pygame.sprite.spritecollide(self, [x for x in self.collideObjects if x.isObstacle == True],
                                                         0)
            for block in block_hit_list:
                if is_x > 0:
                    self.rect.right = block.rect.left
                else:
                    self.rect.left = block.rect.right

            self.rect.centery += self.speed * is_y
            block_hit_list = pygame.sprite.spritecollide(self, [x for x in self.collideObjects if x.isObstacle == True],
                                                         0)
            for block in block_hit_list:
                if is_y > 0:
                    self.rect.bottom = block.rect.top
                else:
                    self.rect.top = block.rect.bottom

    def attack(self, target):
        if self.anim_state != AnimationState.DEATH and self.anim_state != AnimationState.INJURY:
            pygame.mixer.Sound(self.sound_attack).play()
            if target:
                target.get_damage(self.power)
            self.changeAnimation(AnimationState.ATTACK, False)

    def showHealth(self, display):
        self.ratio = self.hp / self.max_hp
        pygame.draw.rect(display, "red", (self.rect.topleft[0], self.rect.centery - self.rect.h, self.rect.w, 3))
        pygame.draw.rect(display, "green",
                         (self.rect.topleft[0], self.rect.centery - self.rect.h, self.rect.w * self.ratio, 3))

    def changeAnimation(self, state, is_freeze=False, force=False):
        self.is_freeze = is_freeze
        anim_is_change = False

        if force:
            self.anim_state = state
            self.cur_anim = self.idle_anim
            anim_is_change = True

        if state == AnimationState.DEATH:
            if self.cur_anim != self.death_anim:
                self.anim_state = state
                self.cur_anim = self.death_anim
                anim_is_change = True
        elif state == AnimationState.INJURY and self.anim_state != AnimationState.DEATH:
            if self.cur_anim != self.injury_anim:
                self.anim_state = state
                self.cur_anim = self.injury_anim
                anim_is_change = True
        elif state == AnimationState.ATTACK and self.anim_state != AnimationState.DEATH and self.anim_state != AnimationState.INJURY:
            if self.cur_anim != self.attack_anim:
                self.anim_state = state
                self.cur_anim = self.attack_anim
                anim_is_change = True
        elif self.anim_state != AnimationState.DEATH and self.anim_state != AnimationState.INJURY and self.anim_state != AnimationState.ATTACK:
            if state == AnimationState.IDLE:
                if self.cur_anim != self.idle_anim:
                    self.anim_state = state
                    self.cur_anim = self.idle_anim
                    anim_is_change = True
            elif state == AnimationState.MOVING:
                if self.cur_anim != self.walk_anim:
                    self.anim_state = state
                    self.cur_anim = self.walk_anim
                    anim_is_change = True

        if anim_is_change and self.is_freeze:
            self.anim_index, self.anim_count = 0, 0

    def death(self):
        pygame.mixer.Sound(self.sound_death).play()
        self.anim_delay += 5
        self.changeAnimation(AnimationState.DEATH, True)

    def debug(self, display):
        font = pygame.font.Font(None, 24)
        hp = font.render(f"HP: {self.hp}", 1, (0, 255, 0))
        display.blit(hp, (self.rect.x, self.rect.y - 30))
        pygame.draw.rect(display, (0, 255, 0), self.rect, 1, 1)
