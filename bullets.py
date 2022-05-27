import pygame
import constants


class BulletPlayer(pygame.sprite.Sprite):
    def __init__(self, screen, car, list_cop_cars, db):
        """создаем пулю в позиции машинки"""
        super().__init__()
        self.list_cop_cars = list_cop_cars
        self.db = db
        self.speed = 30.5
        self.screen = screen
        self.car = car
        self.image = pygame.image.load("images/bullet_top.png")
        self.rect = self.image.get_rect(center=(car.rect.centerx, car.rect.centery))
        self.rect.y = float(self.rect.y)
        self.amount_shells = self.db.get_shells()
        self.db.update_shells(-1)
        if self.amount_shells > 0:
            self.__class__.play_sound()

    def draw_bullets(self):
        if self.amount_shells > 0:
            self.rect.y -= self.speed
            self.screen.blit(self.image, self.rect)

            if self.rect.y < 0:
                self.kill()
        else:
            self.kill()

    def collide_with_cop_car(self):
        """Удаляет машинку, пулю, если происходит их столкновение,
        добавляет по 20 монет игроку за уничтожение противника"""
        for cop in self.list_cop_cars:
            if self.rect.colliderect(cop.rect):
                self.db.update_money(20)
                cop.kill()
                self.kill()
                self.list_cop_cars.remove(cop)

    @staticmethod
    def play_sound():
        gunshot_sound = pygame.mixer.Sound("sounds/zvuk_puli.mp3")
        gunshot_sound.play()

    def __repr__(self):
        return f"BulletPlayer()"


class BulletCop(pygame.sprite.Sprite):
    def __init__(self, screen, car, group, list_cop_cars, db):
        super(BulletCop, self).__init__()
        self.screen = screen
        self.car = car
        self.group = group
        self.db = db
        self.add(group)
        # self.list_cop_bullets = list_cop_bullets
        self.image = pygame.image.load("images/cop_bullet.png")
        # c = list_cop_cars[-1]
        for c in list_cop_cars:
            self.rect = self.image.get_rect(center=(c.rect.centerx, c.rect.centery))
        self.rect.y = float(self.rect.y)
        self.speed = 20.5
        self.collide_with_player_car()
        gunshot_sound = pygame.mixer.Sound("sounds/zvuk_puli.mp3")
        gunshot_sound.play()

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 1000:
            self.kill()
        self.screen.blit(self.image, self.rect)

    def collide_with_player_car(self):
        if self.rect.colliderect(self.car.rect):
            self.db.update_hp(0)
            # print("death")

    def __repr__(self):
        return f"BulletCop()"
