import pygame
import random
from notifications import Notifications


class BulletsBox(pygame.sprite.Sprite):
    def __init__(self, screen, car, db, group):
        super(BulletsBox, self).__init__()
        self.image = pygame.image.load("images/bullets_box.png").convert()
        self.rect = self.image.get_rect(x=self.random_x(),
                                        y=-100)
        self.screen = screen
        self.speed = 5
        self.car = car
        self.db = db
        self.group = group
        self.add(self.group)
        self.notification = Notifications

    def update(self):
        self.screen.blit(self.image, self.rect)
        self.rect.y += self.speed

        if self.rect.y > 1000:
            self.kill()

    def collide_with_car(self):
        if self.rect.colliderect(self.car.rect):
            if self.db.get_money() >= 400:
                self.db.update_shells(20)
                self.db.update_money(-400)
                get_shells = pygame.mixer.Sound("sounds/get_shells.mp3")
                get_shells.play()
                self.kill()
            else:
                self.notification(self.screen, "У вас недостаточно денег!"
                                               "Цена ящика патронов: 400$")

    @staticmethod
    def random_x():
        return random.randint(50, 850)

    def __repr__(self):
        return f"BulletsBox()"
