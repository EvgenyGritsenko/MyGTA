"""Инициализирующий файл игры"""
import time

import pygame
import world_objects
from car import Car
import controls
from fill_car import Fill
import database
import statistics_player
import notifications
import states
import bullets
from pygame.sprite import Group
from cops import Cops
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grand Theft Auto by Gritsenko")


def info_text():
    text_field = pygame.Surface((WIDTH, 50))
    text_field.fill((184, 184, 184))

    font = pygame.font.SysFont("arial", text_field.get_height() // 2)
    liter_now = db.get_liter()
    render_liter_now = font.render(f"Литров: {str(liter_now)}", True, (255, 255, 255))
    text_money = "Money: "
    render_text_money = font.render(text_money, True, (255, 255, 255))
    text_field.blit(render_text_money, (10, 10))
    text_field.blit(render_liter_now, (WIDTH - 200, 10))

    screen.blit(text_field, (0, 0))


db = database.DataBase()


def run():
    get_reg = db.cursor.execute("SELECT player_registered FROM stats").fetchone()
    if not get_reg:
        db.add_record()
        print("Запись в БД создана")
    stats = statistics_player.Stats(db)
    car = Car(screen, stats, db, notifications.Notifications)
    fill = Fill(screen, notifications.Notifications, stats)

    background = world_objects.CreateBackground(screen)
    # state = states.StatePlayer(car, background)

    LIST_COP_CARS = []

    cops_bullets = Group()
    player_bullets = Group()
    police_car_group = Group()

    police_car = Cops(screen, car, police_car_group, LIST_COP_CARS)
    LIST_COP_CARS.append(police_car)
    pygame.time.set_timer(pygame.USEREVENT, 3000)

    while True:
        background.move()
        controls.events(screen, car, fill.true_pos, player_bullets, cops_bullets, police_car_group,
                        LIST_COP_CARS)
        controls.update(car, player_bullets, LIST_COP_CARS, police_car_group, cops_bullets)
        states_player = states.StatePlayer(car, background, LIST_COP_CARS, screen)

        info_text()
        clock.tick(30)
        pygame.display.update()


run()
