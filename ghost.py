import pygame
import random
import time

from settings import WIDTH, CHAR_SIZE, GHOST_SPEED

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.abs_x = x * CHAR_SIZE
        self.abs_y = y * CHAR_SIZE

        self.rect = pygame.Rect(self.abs_x, self.abs_y, CHAR_SIZE, CHAR_SIZE)
        self.move_speed = GHOST_SPEED
        self.color = pygame.Color(color)

        self.img_path = f'assets/ghosts/{color}/'
        self.moving_dir = 'up'
        self.image = pygame.image.load(self.img_path + self.moving_dir + '.png')
        self.image = pygame.transform.scale(self.image, (CHAR_SIZE, CHAR_SIZE))
        self.rect = self.image.get_rect(topleft = (self.abs_x, self.abs_y))
        self.mask = pygame.mask.from_surface(self.image)

        self.directions = {'left':  (-self.move_speed, 0),
                           'right': (+self.move_speed, 0),
                           'up':    (0, -self.move_speed),
                           'down':  (0, +self.move_speed)}
        self.keys = ['left', 'right', 'up', 'down']
        self.direction = (0, 0)

    def move_to_start_pos(self):
        self.rect.x = self.abs_x
        self.rect.y = self.abs_y

    def _is_collide(self, x, y, walls_collide_list):
        return self.rect.move(x, y).collidelist(walls_collide_list) != -1

    def update(self, walls_collide_list):
        available_moves = [k for k in self.keys if \
            not self._is_collide(*self.directions[k], walls_collide_list)]
        randomizing = len(available_moves) > 2 or self.direction == (0, 0)
        if len(available_moves) == 0:
            print(f'Bug {self.rect.x} {self.rect.y} {self.color}')
        elif randomizing and random.randrange(0, 100) <= 60:
            self.moving_dir = random.choice(available_moves)
            self.direction = self.directions[self.moving_dir]

        if not self._is_collide(*self.direction, walls_collide_list):
            self.rect.move_ip(self.direction)
        else:
            self.direction = (0, 0)

        if self.rect.x < 0:
            self.rect.x = WIDTH
        elif self.rect.x > WIDTH - self.move_speed:
            self.rect.x = 0

        self.image = pygame.image.load(self.img_path + self.moving_dir + '.png')
        self.image = pygame.transform.scale(self.image, (CHAR_SIZE, CHAR_SIZE))
        self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y))
