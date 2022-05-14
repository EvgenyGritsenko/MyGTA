"""Инициализирующий файл игры"""
import pygame
import world_objects
from car import Car
import controls
import database
import notifications
import states
from pygame.sprite import Group
from cops import Cops

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grand Theft Auto by Gritsenko")
db = database.DataBase()


def info_text():
    text_field = pygame.Surface((WIDTH, 50))
    text_field.fill((184, 184, 184))

    font = pygame.font.SysFont("arial", text_field.get_height() // 2)
    shell_now = db.get_shells()
    render_shells_now = font.render(f"Кол-во снарядов: {str(shell_now)}", True, (255, 255, 255))
    money_now = db.get_money()
    text_money = f"Деньги: {money_now}$"
    render_text_money = font.render(text_money, True, (255, 255, 255))
    hp_now = db.get_hp()
    render_hp_now = font.render(f"Здоровье: {hp_now}", True, (255, 255, 255))

    text_field.blit(render_text_money, (10, 10))
    text_field.blit(render_shells_now, (render_text_money.get_width() + 30, 10))
    text_field.blit(render_hp_now, (render_text_money.get_width() + 30 + render_shells_now.get_width() + 30,
                                    10))

    screen.blit(text_field, (0, 0))


def run():
    get_reg = db.cursor.execute("SELECT player_registered FROM stats").fetchone()
    if not get_reg:
        db.add_record()
        print("Запись в БД создана")

    car = Car(screen, db, notifications.Notifications)
    background = world_objects.CreateBackground(screen)
    LIST_COP_CARS = []
    cops_bullets = Group()
    player_bullets = Group()
    police_car_group = Group()
    pygame.time.set_timer(pygame.USEREVENT, 3000)
    cop_car = Cops(screen, car, police_car_group, LIST_COP_CARS, db)
    LIST_COP_CARS.append(cop_car)

    while True:
        background.move()
        controls.events(screen, car, player_bullets, cops_bullets, police_car_group,
                        LIST_COP_CARS, db)
        controls.update(car, player_bullets, LIST_COP_CARS, police_car_group, cops_bullets)

        mouse_position = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        states_player = states.StatusPlayer(car, background, LIST_COP_CARS, screen, mouse_position,
                                            pressed, db)

        info_text()
        clock.tick(30)
        pygame.display.update()


run()
