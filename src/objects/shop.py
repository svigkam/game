import pygame

from src.config import PLAYER_FULL_HEART_IMAGE, SWORD_IMAGE, SOUND_PURCHASE
from src.level.level_config import HelpPath
from src.objects.roomObject import RoomObject


class Shop(RoomObject):
    def __init__(self):
        self.rect = pygame.Rect(500, 230, 280, 150)

        self.x1, self.y1 = 500, 350
        self.image1 = pygame.transform.scale_by(pygame.image.load(PLAYER_FULL_HEART_IMAGE), 4)
        self.key1 = pygame.image.load(HelpPath.ONE.value)
        self.label1 = "+ Здоровье"
        self.strong1 = 2
        self.price1 = 35

        self.x2, self.y2 = 700, 350
        self.image2 = pygame.transform.scale_by(pygame.image.load(SWORD_IMAGE), 0.2)
        self.key2 = pygame.image.load(HelpPath.TWO.value)
        self.label2 = "+ Урон"
        self.strong2 = 2
        self.price2 = 42

        self.font = pygame.font.SysFont('Unispace', 24)

        self.is_collectable = False
        self.isObstacle = False
        self.to_clear = False
        self.visible = True

    def update(self, display):
        label1 = self.font.render(f"{self.label1}", False, "white")
        cost1 = self.font.render(f"{self.price1}", False, "white")
        display.blit(self.image1, (self.x1 + 15, self.y1 - 80))
        display.blit(self.key1, (self.x1 + 30, self.y1 - 120))
        display.blit(label1, (self.x1, self.y1))
        display.blit(cost1, (self.x1 + 40, self.y1 - 60))

        label2 = self.font.render(f"{self.label2}", False, "white")
        cost2 = self.font.render(f"{self.price2}", False, "white")
        display.blit(self.image2, (self.x2, self.y2 - 80))
        display.blit(self.key2, (self.x2 + 15, self.y2 - 120))
        display.blit(label2, (self.x2, self.y2))
        display.blit(cost2, (self.x2 + 23, self.y2 - 55))

    def buy(self, player, num):
        if (num == 1 or num == 2) and not self.to_clear:
            if num == 1 and player.coins >= self.price1:
                if player.hp + self.strong1 >= 6:
                    player.hp = 6
                else:
                    player.hp += self.strong1
                player.coins -= self.price1
                self.to_clear = True
                self.visible = False
                pygame.mixer.Sound(SOUND_PURCHASE).play()
            elif num == 2 and player.coins >= self.price2:
                player.power += self.strong2
                player.coins -= self.price2
                self.to_clear = True
                self.visible = False
                pygame.mixer.Sound(SOUND_PURCHASE).play()


