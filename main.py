import pygame
import sys
from src.config import *
from src.entites.player import Player
from src.key_listener import key_listener
from src.utils import initLevels

pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(DISPLAY_CAPTION)
clock = pygame.time.Clock()
player = Player(600, 300)

level = initLevels(display, player)

new_room_info = "Null"


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
            player.attack(level.current_room.enemies)

    keys = pygame.key.get_pressed()
    key_listener(keys, player, level)
    player.update(display)

    clock.tick(TICK_RATE)  # fps
    pygame.display.update()


def main():
    while True:
        game()


if __name__ == '__main__':
    main()
