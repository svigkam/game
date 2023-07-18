import pygame
import sys
from config import *
from enemy import Enemy
from player import Player
from key_listener import key_listener


def init_game():
    global display, clock, player, enemies

    pygame.init()

    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(DISPLAY_CAPTION)
    clock = pygame.time.Clock()

    player = Player(400, 300, 52, 80)
    enemies = [Enemy(100, 200, 52, 80, player)]


def game():
    display.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()

    key_listener(pygame.key.get_pressed(), player)

    player.update(display)

    for enemy in enemies:
        enemy.update(display)

    clock.tick(TICK_RATE)  # fps
    pygame.display.update()


if __name__ == '__main__':
    init_game()
    while True: game()
