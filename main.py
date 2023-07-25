import pygame
import sys
from src.config import *
from src.entites.player import Player
from src.key_listener import key_listener
from src.level.level import Level
from src.level.level_config import room_base_layout
from src.level.room import Room
from src.utils import initLevels

pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(DISPLAY_CAPTION)
clock = pygame.time.Clock()
player = Player(400, 300, 52, 80)

level = initLevels(display, player)
player.collideObjects = level.current_room.objects


def game():
    display.fill((0, 0, 0))
    level.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            btn = pygame.mouse.get_pressed()
            # player.attack(enemies, pos, btn)


    key_listener(pygame.key.get_pressed(), player)
    player.update(display)
    clock.tick(TICK_RATE)  # fps
    pygame.display.update()


def main():
    while True:
        game()


if __name__ == '__main__':
    main()
