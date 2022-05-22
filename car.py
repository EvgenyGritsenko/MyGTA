import pygame
import database

pygame.init()
W = 1000
H = 1000


class Car:
    def __init__(self, screen, db, notification):
        self.notification = notification
        self.screen = screen
        self.db = db
        self.image = pygame.image.load("images/car.png").convert_alpha()
        self.rect = self.image.get_rect(x=W // 2 - self.image.get_width() // 2, y=800)
        self.screen_rect = screen.get_rect()
        self.player_money = self.db.get_money()
        self.player_shells = self.db.get_shells()
        self.mleft = False
        self.mright = False
        self.mup = False
        self.mdown = False
        self.distance_traveled = 1
        self.number_of_kilometres = self.distance_traveled // 1000
        self.speed = 8
        self.hp = int(self.db.get_hp())

    def output(self):
        """Отображение машинки"""
        self.screen.blit(self.image, self.rect)

    def update_car(self):
        """Обновление позиции машинки"""
        if self.mleft:
            self.image = pygame.image.load("images/car_left.png")
            self.rect.x -= self.speed

        elif self.mright:
            self.image = pygame.image.load("images/car_right.png")
            self.rect.x += self.speed
        elif self.mup:
            self.image = pygame.image.load("images/car.png")
            self.rect.y -= self.speed
        elif self.mdown:
            self.image = pygame.image.load("images/car_down.png")
            self.rect.y += self.speed

    def game_border(self):
        """
        Следит за положением машинки, если та выезжает за пределы
        экрана, то переносит ее в противоположную сторону экрана
        """
        if self.rect.centerx < 0:
            self.rect.x = W - self.image.get_width() / 2
        elif self.rect.centerx > W:
            self.rect.x = 0
        elif self.rect.centery < 0:
            self.rect.y = H - self.image.get_height() / 2
        elif self.rect.centery > H:
            self.rect.y = 0 - self.image.get_height() / 2

    def __repr__(self):
        return f"Car()"


def status_player():
    hp = database.DataBase().get_hp()
    if hp >= 1:
        return True
    return False
