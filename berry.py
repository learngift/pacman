import pygame

from settings import CHAR_SIZE

class Berry(pygame.sprite.Sprite):
    def __init__(self, x, y, size, is_power_up = False):
        super().__init__()
        self.power_up = is_power_up
        self.size = size
        self.color = pygame.Color('violetred')
        self.abs_x = (x * CHAR_SIZE) + CHAR_SIZE // 2
        self.abs_y = (y * CHAR_SIZE) + CHAR_SIZE // 2
        self.rect = pygame.Rect(self.abs_x, self.abs_y, size * 2, size * 2)

    def update(self, screen):
        pygame.draw.circle(screen, self.color, \
            (self.abs_x, self.abs_y), self.size, self.size)