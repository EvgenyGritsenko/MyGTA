"""Обработка собтытий игры"""
import pygame
import sys
from bullets import BulletPlayer, BulletCop
from cops import Cops

CAR_MOVE = True


def events(screen, car, player_bullets, cops_bullets, police_car_group,
           list_cop_cars, db):
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
            elif event.key == pygame.K_SPACE:
                if db.get_shells() > 0:
                    new_bullet = BulletPlayer(screen, car, list_cop_cars, db)
                    player_bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                car.mleft = False
            elif event.key == pygame.K_RIGHT:
                car.mright = False
            elif event.key == pygame.K_UP:
                car.mup = False
            elif event.key == pygame.K_DOWN:
                car.mdown = False

        elif event.type == pygame.USEREVENT:
            new_cop_car = Cops(screen, car, police_car_group, list_cop_cars, db)
            list_cop_cars.append(new_cop_car)
            new_bullet_cop = BulletCop(screen, car, cops_bullets, list_cop_cars, db)


def update(car, player_bullets, list_cop_cars, police_car_group, cops_bullets):
    for bullet in player_bullets.sprites():
        bullet.draw_bullets()
        bullet.collide_with_cop_car()

    for cop_bullet in cops_bullets:
        cop_bullet.update()
        cop_bullet.collide_with_player_car()

    car.output()
    car.update_car()
    car.game_border()
    police_car_group.update()
    for cop in list_cop_cars:
        cop.collision_with_player_car()
