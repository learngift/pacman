import pygame
import time
from settings import *
from pac import Pac
from ghost import Ghost
from berry import Berry
from display import Display

blue_color = pygame.Color('blue2')

class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x * CHAR_SIZE, y * CHAR_SIZE, CHAR_SIZE, CHAR_SIZE)

    def update(self, screen):
        pygame.draw.rect(screen, blue_color, self.rect)

class World:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.game_level = 1

        self.player = pygame.sprite.GroupSingle()
        self.ghosts = pygame.sprite.Group()
        self.walls  = pygame.sprite.Group()
        self.berries= pygame.sprite.Group()
        self.display = Display(screen)

        for y, line in enumerate(MAP):
            for x, char in enumerate(line):
                if char =='1':
                    self.walls.add(Cell(x, y))
                elif char == ' ':
                    self.berries.add(Berry(x, y, CHAR_SIZE // 4))
                elif char == 'B':
                    self.berries.add(Berry(x, y, CHAR_SIZE // 2, is_power_up=True))
                elif char == 'P': # Player
                    self.player.add(Pac(x, y))
                elif char == 's':
                    self.ghosts.add(Ghost(x, y, "skyblue"))
                elif char == 'p':
                    self.ghosts.add(Ghost(x, y, "pink"))
                elif char == 'o':
                    self.ghosts.add(Ghost(x, y, "orange"))
                elif char == 'r':
                    self.ghosts.add(Ghost(x, y, "red"))

        self.walls_collide_list = [w.rect for w in self.walls.sprites()]

    def dashboard(self):
        pygame.draw.rect(self.screen, pygame.Color(139, 136, 120), \
                pygame.Rect(0, HEIGHT, WIDTH, NAV_HEIGHT))
        self.display.show_life(self.player.sprite.life)
        self.display.show_level(self.game_level)
        self.display.show_score(self.score)

    def update(self):
        for w in self.walls.sprites():
            w.update(self.screen)

        if self.player.sprite.life > 0:
            self.player.sprite.animate(pygame.key.get_pressed(), self.walls_collide_list)

            for b in self.berries.sprites():
                if self.player.sprite.rect.colliderect(b.rect):
                    if b.power_up:
                        self.player.sprite.immune_time = 150
                        self.player.sprite.status = 'power_up'
                        self.score += 50
                    else:
                        self.score += 10
                    b.kill()

            reset_pos = False
            for g in self.ghosts.sprites():
                if self.player.sprite.rect.colliderect(g.rect):
                    if self.player.sprite.immune_time > 0:
                        g.move_to_start_pos()
                        self.score += 100
                    else:
                        time.sleep(2)
                        self.player.sprite.life -= 1
                        reset_pos = True

            if reset_pos:
                for g in self.ghosts.sprites():
                    g.move_to_start_pos()
                self.player.sprite.move_to_start_pos()

        for b in self.berries.sprites():
            b.update(self.screen)

        [ ghost.update(self.walls_collide_list) for ghost in self.ghosts.sprites() ]

        self.player.update()
        self.player.draw(self.screen)
        self.ghosts.draw(self.screen)
        self.dashboard()