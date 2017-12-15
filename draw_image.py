#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (800, 600)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Draw Image Sample")

# イメージを用意
backImg = pygame.image.load("img/images.jpg").convert()
pickImg = pygame.image.load("img/ruby_pickaxe.png").convert_alpha()

while True:
    screen.blit(backImg, (0,0))
    screen.blit(backImg, (620,0))
    screen.blit(backImg, (320,400))
    screen.blit(pickImg, (100,100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
