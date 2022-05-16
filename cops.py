import random
import pygame


def random_x():
    number = random.randint(100, 900)
    return number


class Cops(pygame.sprite.Sprite):
    def __init__(self, screen, car, group, list_cop_cars, db):
        super(Cops, self).__init__()
        self.db = db
        self.list_cop_cars = list_cop_cars
        self.screen = screen
        self.car = car
        self.image = pygame.image.load("images/cop.png").convert_alpha()
        self.rect = self.image.get_rect(x=random_x(), y=-50)
        self.speed = 5
        self.collision_with_player_car()
        self.group = group
        self.add(self.group)

    def update(self):
        """Рисует и двигает машинку на экране"""
        self.rect.y += self.speed
        self.screen.blit(self.image, self.rect)

        if self.rect.y > 1500:
            self.kill()
            self.list_cop_cars.remove(self)
            self.db.update_hp(-20)

    def collision_with_player_car(self):
        if self.rect.colliderect(self.car.rect):
            player_hp = self.db.get_hp()
            if player_hp >= 100:
                self.db.update_hp(0)

    def __repr__(self):
        return f"Cops({self.screen}, {self.car}, {self.group}, {self.list_cop_cars})"
