"""Обработка собтытий игры"""
import pygame
import sys
from bullets import BulletPlayer, BulletCop
from cops import Cops


def events(screen, car, true_pos, player_bullets, cops_bullets, police_car_group,
           list_cop_cars):
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
            elif event.key == pygame.K_SPACE:
                new_bullet = BulletPlayer(screen, car, list_cop_cars)
                player_bullets.add(new_bullet)
        elif event.type == pygame.USEREVENT:
            new_cop_car = Cops(screen, car, police_car_group, list_cop_cars)
            new_cop_bullet = BulletCop(screen, cops_bullets, list_cop_cars)
            list_cop_cars.append(new_cop_car)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                car.mleft = False
            elif event.key == pygame.K_RIGHT:
                car.mright = False
            elif event.key == pygame.K_UP:
                car.mup = False
            elif event.key == pygame.K_DOWN:
                car.mdown = False


def update(car, player_bullets, list_cop_cars, police_car_group, cops_bullets):
    for bullet in player_bullets.sprites():
        # bullet.update(car.direction)
        bullet.draw_bullets()
        bullet.collide_with_cop_car()

    car.output()
    car.start_engine()
    car.update_car()
    car.game_border()
    police_car_group.update()
    cops_bullets.update()
    for cop in list_cop_cars:
        cop.collision_with_player_car()

