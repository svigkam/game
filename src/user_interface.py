import pygame.image

from src.config import PLAYER_FULL_HEART_IMAGE, PLAYER_EMPTY_HEART_IMAGE, PLAYER_HALF_HEART_IMAGE, PLAYER_COINS_IMAGE


class UserInterface:
    def __init__(self, player):
        self.player = player
        self.full_heart = pygame.transform.scale2x(pygame.image.load(PLAYER_FULL_HEART_IMAGE))
        self.half_heart = pygame.transform.scale2x(pygame.image.load(PLAYER_HALF_HEART_IMAGE))
        self.empty_heart = pygame.transform.scale2x(pygame.image.load(PLAYER_EMPTY_HEART_IMAGE))
        self.coins = pygame.transform.scale_by(pygame.image.load(PLAYER_COINS_IMAGE), 1.5)

    def update(self, display):
        result = []

        if self.player.hp - 2 >= 0:
            result.append(self.full_heart)
        elif self.player.hp - 1 >= 0:
            result.append(self.half_heart)
        else:
            result.append(self.empty_heart)

        if self.player.hp - 4 >= 0:
            result.append(self.full_heart)
        elif self.player.hp - 3 >= 0:
            result.append(self.half_heart)
        else:
            result.append(self.empty_heart)

        if self.player.hp - 6 == 0:
            result.append(self.full_heart)
        elif self.player.hp - 5 >= 0:
            result.append(self.half_heart)
        else:
            result.append(self.empty_heart)

        display.blit(result[0], (100, 100))
        display.blit(result[1], (134, 100))
        display.blit(result[2], (168, 100))
        display.blit(self.coins, (100, 150))

        my_font = pygame.font.SysFont('Unispace', 40)
        text_surface = my_font.render(f"{self.player.coins}", False, "white")

        display.blit(text_surface, (140, 150))


