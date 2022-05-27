import pygame
import world_objects
from car import Car
import controls
import database
import notifications
import states
from pygame.sprite import Group
import time
import constants

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
    text_money = f"Деньги: {str(money_now)}$"
    render_text_money = font.render(text_money, True, (255, 255, 255))
    hp_now = db.get_hp()
    render_hp_now = font.render(f"Здоровье: {str(hp_now)}", True, (255, 255, 255))
    timer_now = constants.SCORE
    render_time_now = font.render(f"ЦЕЛЬ ОЧКОВ: {str(timer_now)}/1800", True, (255, 255, 255))

    text_field.blit(render_text_money, (10, 10))
    text_field.blit(render_shells_now, (render_text_money.get_width() + 30, 10))
    text_field.blit(render_hp_now, (render_text_money.get_width() + 30 + render_shells_now.get_width() + 30,
                                    10))
    text_field.blit(render_time_now, (700, 10))

    screen.blit(text_field, (0, 0))


def run():
    get_reg = db.cursor.execute("SELECT player_registered FROM stats").fetchone()
    if not get_reg:
        db.add_record()

    # car = Car(screen, db, notifications.Notifications)
    background = world_objects.CreateBackground(screen)
    LIST_COP_CARS = []
    cops_bullets = Group()
    player_bullets = Group()
    police_car_group = Group()
    bomb_group = Group()
    bullets_box_group = Group()
    get_health_group = Group()
    pygame.time.set_timer(pygame.USEREVENT, 3000)
    pygame.time.set_timer(pygame.USEREVENT + 1, 5000)
    pygame.time.set_timer(pygame.USEREVENT + 2, 20000)
    pygame.time.set_timer(pygame.USEREVENT + 3, 10000)

    pygame.mixer.music.load("sounds/music.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.3)

    car = Car(screen, db, notifications.Notifications)
    # cop_car = Cops(screen, car, police_car_group, LIST_COP_CARS, db)
    # LIST_COP_CARS.append(cop_car)
    # cop_car.rect.y -= 1000
    while True:
        states.StatusPlayer(car, screen, LIST_COP_CARS, player_bullets, cops_bullets,
                            bullets_box_group, get_health_group, bomb_group, db,
                            police_car_group)

        background.move()
        controls.events(screen, car, player_bullets, cops_bullets, police_car_group,
                        LIST_COP_CARS, db, bomb_group, bullets_box_group,
                        get_health_group)
        controls.update(car, player_bullets, LIST_COP_CARS, police_car_group,
                        cops_bullets, bomb_group, bullets_box_group,
                        get_health_group, screen, db)

        if constants.SCORE > 1800:
            constants.TIMER_START = time.time()
            constants.SCORE = 1
        elif constants.SCORE % 300 == 0:
            db.update_money(200)
            pygame.mixer.Sound("sounds/get_hp.mp3")


        info_text()
        clock.tick(30)
        pygame.display.update()

        if constants.SCORE > time.time() - constants.TIMER_START:
            continue
        else:
            constants.SCORE += 1



run()
