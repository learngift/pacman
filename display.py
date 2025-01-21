import pygame

from settings import WIDTH, HEIGHT, CHAR_SIZE

pygame.font.init()

class Display:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('lucidaconsole', CHAR_SIZE)
        self.game_over_font = pygame.font.SysFont('dejavusansmono', 48)
        self.text_color = pygame.Color(255, 0, 0)

    def show_life(self, life):
        image = pygame.transform.scale(pygame.image.load('assets/life/life.png'), \
                (CHAR_SIZE, CHAR_SIZE))
        x = CHAR_SIZE // 2
        y = HEIGHT + CHAR_SIZE // 2
        for _ in range(life):
            self.screen.blit(image, (x, y))
            x += CHAR_SIZE

    def show_level(self, level):
        msg = self.font.render(f'Level {level}', True, self.text_color)
        self.screen.blit(msg, (WIDTH // 3, HEIGHT + CHAR_SIZE // 2))

    def show_score(self, score):
        msg = self.font.render(f'{score}', True, self.text_color)
        self.screen.blit(msg, (2 * WIDTH // 3, HEIGHT + CHAR_SIZE // 2))

    def game_over(self):
        msg = self.game_over_font.render(f'GAME OVER!!', True, \
            pygame.Color(223, 255, 0))
        self.screen.blit(msg, (WIDTH // 4, HEIGHT // 3))
        msg = self.font.render(f'Press "R" to Restart', True, \
            pygame.Color(0, 255, 255))
        self.screen.blit(msg, (WIDTH // 4, HEIGHT // 2))
