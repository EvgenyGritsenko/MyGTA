"""Обработка собтытий игры"""
import pygame
import sys


def events(car, true_pos: bool):
    """
    :param car:
    :param true_pos: true если машинка и заправка пересеклись
    :return:
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car.mleft = True
            elif event.key == pygame.K_RIGHT:
                car.mright = True
            elif event.key == pygame.K_UP:
                car.mup = True
            elif event.key == pygame.K_DOWN:
                car.mdown = True
            elif event.key == pygame.K_z and true_pos:
                car.start_engine()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                car.mleft = False
            elif event.key == pygame.K_RIGHT:
                car.mright = False
            elif event.key == pygame.K_UP:
                car.mup = False
            elif event.key == pygame.K_DOWN:
                car.mdown = False
