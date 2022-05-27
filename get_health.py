import pygame
import random
from notifications import Notifications


class GetHealth(pygame.sprite.Sprite):
    def __init__(self, screen, car, group, db):
        super(GetHealth, self).__init__()
        self.image = pygame.image.load("images/get_health.png").convert()
        self.rect = self.image.get_rect(x=self.random_x(), y=-50)
        self.screen = screen
        self.car = car
        self.group = group
        self.add(self.group)
        self.db = db
        self.notification = Notifications
        self.speed = 5

    def update(self):
        self.screen.blit(self.image, self.rect)
        self.rect.y += self.speed

        if self.rect.y > 1000:
            self.kill()

    def collide_with_car(self):
        if self.rect.colliderect(self.car.rect):
            if self.db.get_money() >= 250:
                self.db.update_hp(40)
                self.db.update_money(-250)
                sound = pygame.mixer.Sound("sounds/get_hp.mp3")
                sound.play()
                self.kill()
            else:
                self.notification(self.screen, "У вас недостаточно денег!"
                                               "Цена аптечки: 250$").info()

    @staticmethod
    def random_x():
        return random.randint(50, 850)

    def __repr__(self):
        return "GetHealth()"
