#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (800, 600)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Mouse Event")

backImg = pygame.image.load("img/images.jpg").convert()
pythonImg = pygame.image.load("img/ruby_sword.png").convert_alpha()

cur_pos = (0,0)
pythons_pos = []

while True:
    screen.blit(backImg, (0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        # マウスクリック
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            x -= pythonImg.get_width() / 2
            y -= pythonImg.get_height() / 2
            pythons_pos.append((x,y))
        # マウス移動で移動
        if event.type == MOUSEMOTION:
            x, y = event.pos
            x -= pythonImg.get_width() / 2
            y -= pythonImg.get_height() / 2
            cur_pos = (x,y)

    # 表示
    screen.blit(pythonImg, cur_pos)
    for i, j in pythons_pos:
        screen.blit(pythonImg, (i,j))

    pygame.display.update()
