#!/usr/bin/python3

import os

import pygame
from pygame.locals import *


def get_digits():
    files = os.listdir('segments')

    surfaces = []

    for i in files:
        if i.endswith('.gif'):
            s = pygame.image.load('segments/%s' % i).convert_alpha()
            surfaces.append(s)

    return surfaces


def main():
    pygame.init()
    display = pygame.display.set_mode((1130, 552))

    s = get_digits()
    print(s)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # draw
        display.fill(Color(255, 255, 255))

        # masked.blit(mask, (0, 0), None, pygame.BLEND_RGB_ADD)
        for i in range(75):
            display.blit(s[i], (0, 0))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
