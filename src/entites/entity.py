import pygame
from src.config import DEBUG


class Entity:
    def __init__(self, x, y, width, height, speed, power, hp, walk_animation, idle_animation):
        self.x, self.y = x, y
        self.rect = pygame.Rect(x, y, width, height)
        self.width = width
        self.height = height

        # Анимация
        self.animation_count = 0
        self.moving_left, self.moving_right = False, False
        self.moving_up, self.moving_down = False, False
        self.is_dying, self.getting_damage = False, False
        self.is_throw_attack = False
        self.is_attack = False
        self.is_dead = False
        self.walk_animation = [pygame.image.load(x) for x in walk_animation]
        self.idle_animation = [pygame.image.load(x) for x in idle_animation]

        # Характеристики
        self.speed = speed
        self.power = power
        self.hp = hp

    def get_damage(self, damage):
        if not self.is_dying:  # получение урона если не умирает
            self.hp -= damage
        self.getting_damage = True  # включение анимации получения урона
        if self.hp <= 0: self.death()  # Проверка на жизнеспособность

    def animate(self, display):
        if self.animation_count + 1 >= 32:
            self.animation_count = 0
        self.animation_count += 1

        if self.is_dying:  # Анимация смерти
            # TODO: horizontal_move = ...
            self.is_dead = True  # когда кончится анимация
        if self.getting_damage:  # Анимация получения урона
            # TODO: horizontal_move = ...
            self.getting_damage = False  # когда кончится анимация
        if self.is_attack:  # Анимация атаки
            # TODO: horizontal_move = ...
            self.is_attack = False  # когда кончится анимация
        if self.is_throw_attack:  # Анимация броска
            # TODO: horizontal_move = ...
            self.is_throw_attack = False  # когда кончится анимация
        if self.moving_right:  # Движение вправо
            horizontal_move = pygame.transform.scale(self.walk_animation[self.animation_count // 4],
                                                     (self.width, self.height))
        elif self.moving_left:  # Движение влево
            horizontal_move = pygame.transform.scale(
                pygame.transform.flip(self.walk_animation[self.animation_count // 4], True, False),
                (self.width, self.height))
        # elif self.moving_up:  # Движение вверх
        # elif self.moving_down:  # Движение вниз
        else:  # Статика
            horizontal_move = pygame.transform.scale(self.idle_animation[self.animation_count // 8],
                                                     (self.width, self.height))

        display.blit(horizontal_move, (self.x, self.y))

    def update(self, display):
        self.debug(display) if DEBUG else ...  # DEBUG

        self.animate(display)  # Анимация
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def move(self, is_x, is_y):  # is_x (+ вправо, - влево) is_y (+ вниз, - вверх)
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

    def attack(self, num=0):
        if num == 1:
            self.is_throw_attack = True
        else:
            self.is_attack = True

    def death(self):
        self.is_dying = True
        # TODO: вызов анимации с задержкой

    def debug(self, display):
        font = pygame.font.Font(None, 36)
        hp = font.render(f"HP: {self.hp}", 1, (0, 255, 0))
        display.blit(hp, (self.x - 5, self.y - 30))
        pygame.draw.rect(display, (0, 255, 0), self.rect, 1, 1)
