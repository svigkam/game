import pygame

from src.config import DEBUG


class RoomObject:
    def __init__(self, x, y, width, height, image, is_obstacle, is_collectable=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.rect = pygame.Rect(x, y, width, height)

        self.is_collectable = is_collectable
        self.isObstacle = is_obstacle

        self.to_clear = False

    def update(self, display):
        display.blit(self.image, self.image.get_rect(center=(self.rect.center)))


    def pick_up(self):
        self.to_clear = True

    def get_rect(self):
        return self.rect
