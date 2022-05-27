"""Обработка собтытий игры"""
import pygame
import sys
from bullets import BulletPlayer, BulletCop
from cops import Cops
from bombs import Bomb
from bullets_box import BulletsBox
from get_health import GetHealth

STATE_OF_EVENTS = True


def events(screen, car, player_bullets, cops_bullets, police_car_group,
           list_cop_cars, db, bomb_group, bullets_box_group, get_health_group):
    if STATE_OF_EVENTS:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                db.update_hp(100)
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
                BulletCop(screen, car, cops_bullets, list_cop_cars, db)

            elif event.type == pygame.USEREVENT + 1:
                Bomb(screen, bomb_group, car, list_cop_cars, player_bullets,
                     cops_bullets, db)

            elif event.type == pygame.USEREVENT + 2:
                BulletsBox(screen, car, db, bullets_box_group)

            elif event.type == pygame.USEREVENT + 3:
                GetHealth(screen, car, get_health_group, db)
    else:
        backup_events(db)


def update(car, player_bullets, list_cop_cars, police_car_group, cops_bullets,
           bomb_group, bullets_box, get_health_group, screen, db):
    for bullet in player_bullets.sprites():
        bullet.draw_bullets()
        bullet.collide_with_cop_car()

    for cop_bullet in cops_bullets:
        cop_bullet.update()
        cop_bullet.collide_with_player_car()

    for bomb in bomb_group:
        bomb.update()
        bomb.collide_with_all_objects()

    for bullet_box in bullets_box:
        bullet_box.update()
        bullet_box.collide_with_car()

    for get_health in get_health_group:
        get_health.update()
        get_health.collide_with_car()

    car.output()
    car.update_car()
    car.game_border()
    police_car_group.update()
    for cop in list_cop_cars:
        cop.collision_with_player_car()


def backup_events(db):
    """Используется при отключении всех событий в функции events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            db.update_hp(100)
            sys.exit()
