import random
import pygame


def random_x():
    number = random.randint(100, 900)
    return number


class Cops(pygame.sprite.Sprite):
    def __init__(self, screen, car, group, list_cop_cars):
        super().__init__()
        self.list_cop_cars = list_cop_cars
        self.screen = screen
        self.car = car
        self.image = pygame.image.load("images/cop.png")
        self.rect = self.image.get_rect(x=random_x(), y=-50)
        self.speed = 5
        self.collision_with_player_car()
        self.add(group)

    def update(self):
        """Рисует и двигает машинку на экране"""
        self.rect.y += self.speed
        self.screen.blit(self.image, self.rect)

        if self.rect.y > 1000:
            self.kill()
            self.list_cop_cars.remove(self)

    def collision_with_player_car(self):
        if self.rect.colliderect(self.car.rect):
            self.car.hp = 0

