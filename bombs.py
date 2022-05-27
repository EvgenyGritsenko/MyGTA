import time
import pygame
import random


class Bomb(pygame.sprite.Sprite):
    def __init__(self, screen, group, car, cop_cars, bullets, cops_bullets,
                 db):
        super(Bomb, self).__init__()
        self.car = car
        self.cop_cars = cop_cars
        self.bullets = bullets
        self.cops_bullets = cops_bullets
        self.image = pygame.image.load("images/bomb.png")
        self.coordinates_start = self.random_coordinates_start()
        self.rect = self.image.get_rect(x=self.coordinates_start[0],
                                        y=self.coordinates_start[1])
        self.screen = screen
        self.speed = 15
        self.way = "go"
        self.add(group)
        self.image_explosion = pygame.image.load("images/explosion.png")
        self.image_explosion_rect = self.image_explosion.get_rect(center=(self.rect.x,
                                                                          self.rect.y))
        sound_shot = pygame.mixer.Sound("sounds/flight_sound.mp3")
        sound_shot.play()
        self.db = db

    def update(self):
        self.speed = 15
        self.screen.blit(self.image, self.rect)
        range_x = [i for i in range(0, 1000)]
        range_y = [j for j in range(0, 1000)]

        if self.way == "go":
            if self.coordinates_start[2] == 1:
                self.rect.x += self.speed
                self.rect.y += self.speed
            elif self.coordinates_start[2] == 2:
                self.rect.x -= self.speed
                self.rect.y += self.speed
            elif self.coordinates_start[2] == 3:
                self.rect.x -= self.speed
                self.rect.y -= self.speed
            elif self.coordinates_start[2] == 4:
                self.rect.x += self.speed
                self.rect.y -= self.speed
        else:
            self.way_back()

        if self.rect.x not in range_x and self.rect.y not in range_y:
            self.way = "go"
            self.kill()

    def collide_with_all_objects(self):
        list_rects = (self.car, *self.cop_cars, *self.bullets,
                      *self.cops_bullets)
        if self.rect.collidelistall([i.rect for i in list_rects]):
            if self.rect.colliderect(self.car.rect):
                gunshot_sound_player = pygame.mixer.\
                    Sound("sounds/explosion_with_car.mp3")
                gunshot_sound_player.play()
                self.kill()
                self.db.update_hp(0)
                Explosion(self.screen, self)
            else:
                gunshot_sound_other = pygame.mixer.\
                    Sound("sounds/explosion_with_other.mp3")
                gunshot_sound_other.play()
                self.way_back()

    def way_back(self):
        self.way = "back"
        if self.coordinates_start[2] == 1:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
        elif self.coordinates_start[2] == 2:
            self.rect.x += self.speed
            self.rect.y -= self.speed
        elif self.coordinates_start[2] == 3:
            self.rect.x += self.speed
            self.rect.y += self.speed
        elif self.coordinates_start[2] == 4:
            self.rect.x -= self.speed
            self.rect.y += self.speed

    @staticmethod
    def random_coordinates_start():
        # третий аргумент это сторона с которой летит бомба
        coordinate = random.choice([(0, 0, 1), (1000, 0, 2),
                                    (1000, 1000, 3), (0, 1000, 4)])
        return coordinate

    def __repr__(self):
        return f"Bomb()"


class Explosion:
    def __init__(self, screen, bomb):
        self.image = pygame.image.load("images/explosion.png")
        self.rect = self.image.get_rect(x=bomb.rect.x, y=bomb.rect.y)
        self.screen = screen
        self.bomb = bomb
        self.draw()

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def __repr__(self):
        return "Explosion()"
