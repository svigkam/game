import pygame


def fontsize(size):
    font = pygame.font.Font("assets/better-vcr_0.ttf", size)
    return font


class Label:
    def __init__(self, text, x, y, size=20, color="white"):
        self.font = fontsize(size)
        self.image = self.font.render(text, 1, color)
        _, _, w, h = self.image.get_rect()
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

        self.is_collectable = False
        self.isObstacle = False
        self.to_clear = False
        self.visible = True

    def change_text(self, newtext, color="white"):
        self.image = self.font.render(newtext, 1, color)

    def change_font(self, font, size, color="white"):
        self.font = pygame.font.SysFont(font, size)
        self.change_text(self.text, color)

    def update(self, display):
        display.blit(self.image, self.rect)
