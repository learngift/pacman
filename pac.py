import pygame
from settings import *
from animation import import_sprite

class Pac(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.abs_x = x * CHAR_SIZE
        self.abs_y = y * CHAR_SIZE

        self.frame_index = 0
        self.animation_speed = 0.5

        self.anim = dict()
        for a in ['up', 'down', 'left', 'right', 'idle', 'power_up']:
            self.anim[a] = import_sprite('assets/pac/' + a)

        self.status = 'idle'

        self.image = self.anim[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft=(self.abs_x, self.abs_y))
        self.mask = pygame.mask.from_surface(self.image)

        self.directions = {'left' : (-PLAYER_SPEED, 0),
                           'right': (+PLAYER_SPEED, 0),
                           'up'   : (0, -PLAYER_SPEED),
                           'down' : (0, +PLAYER_SPEED)}
        self.keys = {'left':  pygame.K_LEFT,
                     'right': pygame.K_RIGHT,
                     'up':    pygame.K_UP,
                     'down':  pygame.K_DOWN}
        self.direction = (0, 0)
        self.life = 3
        self.pac_score = 0
        self.immune_time = 0

    def move_to_start_pos(self):
        self.rect.x = self.abs_x
        self.rect.y = self.abs_y
        self.direction = (0, 0)
        self.status = 'idle'

    def _is_collide(self, x, y):
        return self.rect.move(x, y).collidelist(self.walls_collide_list) != -1

    def animate(self, pressed_key, walls_collide_list):
        animation = self.anim[self.status]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
        	self.frame_index = 0
        image = animation[int(self.frame_index)]
        self.image = pygame.transform.scale(image, (CHAR_SIZE, CHAR_SIZE))

        self.walls_collide_list = walls_collide_list
        for key, key_value in self.keys.items():
            if pressed_key[key_value] and not self._is_collide(*self.directions[key]):
                self.direction = self.directions[key]
                self.status = key
                break

        if not self._is_collide(*self.direction):
            self.rect.move_ip(self.direction)
            if self.rect.x < 0:
                self.rect.x = WIDTH
            elif self.rect.x > WIDTH - PLAYER_SPEED:
                self.rect.x = 0
        else:
            self.status = 'idle'

        if self.immune_time > 0:
            self.status = 'power_up'

    def update(self):
        if self.immune_time > 0:
            self.immune_time -= 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))