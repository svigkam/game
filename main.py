import pygame
import sys
from src.config import *
from src.entites.enemy import Enemy
from src.entites.player import Player
from src.key_listener import key_listener
from src.level.level_config import room_base_layout
from src.level.room import Room

pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(DISPLAY_CAPTION)
clock = pygame.time.Clock()


def init_game():
    global player, enemies, current_room
    player = Player(400, 300, 52, 80)
    enemies = [Enemy(100, 200, 52, 80, player), Enemy(500, 500, 52, 80, player)]
    current_room = Room(display)


def game():
    display.fill((0, 0, 0))
    current_room.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            btn = pygame.mouse.get_pressed()
            player.attack(enemies, pos, btn)

    key_listener(pygame.key.get_pressed(), player)

    # ENTITY
    player.update(display)
    for enemy in enemies:
        enemy.update(display)
        if enemy.is_dead:
            enemies.remove(enemy)

    clock.tick(TICK_RATE)  # fps
    pygame.display.update()


if __name__ == '__main__':
    init_game()
    while True: game()
