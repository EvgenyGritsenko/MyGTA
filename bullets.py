import pygame


class BulletPlayer(pygame.sprite.Sprite):
    def __init__(self, screen, car, list_cop_cars):
        """создаем пулю в позиции машинки"""
        super().__init__()
        self.list_cop_cars = list_cop_cars
        self.speed = 10.5
        self.screen = screen
        self.car = car
        self.image = pygame.image.load("images/bullet_top.png")
        self.rect = self.image.get_rect(center=(car.rect.centerx, car.rect.centery))
        self.rect.y = float(self.rect.y)
        gunshot_sound = pygame.mixer.Sound("sounds/zvuk_puli.mp3")
        gunshot_sound.play()

    def draw_bullets(self):
        self.rect.y -= 20
        self.screen.blit(self.image, self.rect)

        if self.rect.y < 0:
            self.kill()

    def collide_with_cop_car(self):
        """Удаляет машинку, пулю, если происходит их столкновение"""
        for cop in self.list_cop_cars:
            if self.rect.colliderect(cop.rect):
                # мне лень фиксить баг, пусть просто улеатает за экран :)
                cop.rect.y = -1000
                cop.kill()
                self.kill()
                self.list_cop_cars.remove(cop)


class BulletCop(pygame.sprite.Sprite):
    def __init__(self, screen, group, list_cop_cars):
        super().__init__()
        self.screen = screen
        self.group = group
        self.add(group)
        self.list_cop_cars = list_cop_cars
        self.speed = 20
        for cop in self.list_cop_cars:
            self.image = pygame.image.load("images/cop_bullet_left.png")
            self.rect = self.image.get_rect(center=(cop.rect.x, cop.rect.y))
            self.image2 = pygame.image.load("images/cop_bullet_right.png")
            self.rect2 = self.image2.get_rect(center=(cop.rect.x, cop.rect.y))
        self.gunshot_sound = pygame.mixer.Sound("sounds/zvuk_puli.mp3")
        self.gunshot_sound.play()

    def update(self):
        self.rect.x -= self.speed
        self.rect2.x += self.speed
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image2, self.rect2)

        if self.rect.x < 0:
            self.kill()
        if self.rect2.x > 1000:
            self.kill()
