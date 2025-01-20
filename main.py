import pygame
from settings import *
from world import World

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT + NAV_HEIGHT))
pygame.display.set_caption('PacMan')

world = World(screen)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    world.update()

    pygame.display.flip()
    clock.tick(30)
pygame.quit()
