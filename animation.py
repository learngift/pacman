from os import walk
import pygame

def import_sprite(path):
    res = []
    for _, __, filename in walk(path):
        for image in filename:
            res.append(pygame.image.load(f'{path}/{image}').convert_alpha())
    return res