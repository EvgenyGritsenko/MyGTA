"""Инициализирующий файл игры"""
import pygame
import world_objects
from car import Car
import controls
from fill_car import Fill
import database
import stats_player
import notifications
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
    stats = stats_player.Stats(db)
    car = Car(screen, stats, db, notifications.Notifications)
    fill = Fill(screen, notifications.Notifications, stats)

    while True:
        world_objects.CreateBackground(screen)
        road = world_objects.CreateRoad(screen)
        road.move()
        # world_objects.CreateShop(screen, car)

        controls.events(car, fill.true_pos)

        # fill.output()
        # fill.position_tracker(car.rect)
        # fill.in_place()

        car.output()
        car.start_engine()
        car.update_car()
        car.game_border()
        car.set_distance()

        info_text()
        clock.tick(30)
        pygame.display.update()


run()