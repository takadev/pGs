#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
 
SCREEN_SIZE = (800, 600)
 
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Key Event")
 
img = pygame.image.load("img/images.jpg").convert_alpha()
img_rect = img.get_rect()
img_rect.center = (400, 300)
 
vx = vy = 50  # キーを押したときの移動距離
 
while True:
    # 押されているキーをチェック
    pressed_keys = pygame.key.get_pressed()
    # 押されているキーに応じて画像を移動
    if pressed_keys[K_LEFT]:
        img_rect.move_ip(-vx, 0)
    if pressed_keys[K_RIGHT]:
        img_rect.move_ip(vx, 0)
    if pressed_keys[K_UP]:
        img_rect.move_ip(0, -vy)
    if pressed_keys[K_DOWN]:
        img_rect.move_ip(0, vy)

    screen.fill((0,0,0))
    screen.blit(img, img_rect)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
        if event.type == KEYDOWN:  # キーを押したとき
            # ESCキーならスクリプトを終了
            if event.key == K_ESCAPE:
                sys.exit()
