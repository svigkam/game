import pygame


def key_listener(keys, player):
    move_x, move_y = 0, 0

    if keys[pygame.K_a]:
        move_x = -1
    elif keys[pygame.K_d]:
        move_x = 1

    if keys[pygame.K_w]:
        move_y = -1
    elif keys[pygame.K_s]:
        move_y = 1

    if move_x != 0 or move_y != 0:
        player.move(move_x, move_y)

    if keys[pygame.K_1]:
        player.buyAtShop(1)
    if keys[pygame.K_2]:
        player.buyAtShop(2)

