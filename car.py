import pygame
pygame.init()
W = 1000
H = 1000


class Car:
    def __init__(self, screen, stats, db, notification):
        self.stats = stats
        self.notification = notification
        self.screen = screen
        self.db = db
        self.image = pygame.image.load("images/car.png").convert_alpha()
        self.rect = self.image.get_rect(x=W//2 - self.image.get_width() // 2, y=H//2)
        self.screen_rect = screen.get_rect()
        self.start_car = False
        self.player_money = stats.money
        self.player_liters = stats.number_of_liters
        self.mleft = False
        self.mright = False
        self.mup = False
        self.mdown = False
        self.distance_traveled = 1
        self.number_of_kilometres = self.distance_traveled // 1000
        self.speed = 3

    def output(self):
        """Отображение машинки"""
        self.screen.blit(self.image, self.rect)

    def update_car(self):
        """Обновление позиции машинки"""
        if self.start_car:
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

    def start_engine(self):
        if self.player_liters > 0:
            self.start_car = True
        else:
            self.start_car = False
            n = self.notification(self.screen, "У вас нет топлива!")
            n.warning()

    def set_distance(self):
        """
        Считает проеханное машиной расстояние
        """
        if self.mleft or self.mright or self.mup or self.mdown:
            self.distance_traveled += self.speed

