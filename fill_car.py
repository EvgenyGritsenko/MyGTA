"""Отвечает за систему заправки авто"""
import pygame
W = 1000
H = 1000


class Fill:
    """Заправляет машинку"""
    def __init__(self, screen, notification, stats):
        self.stats = stats
        self.notification = notification
        self.screen = screen
        self.image = pygame.image.load("images/zapravka.png")
        self.rect = self.image.get_rect(center=(100, H // 2 - self.image.get_height() // 1.3))
        self.true_pos = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def in_place(self):
        if self.true_pos:
            n = self.notification(self.screen, f"Стоимость 1 литра - 11$, у вас {self.stats.number_of_liters}/100 литров")
            n.info()

    def position_tracker(self, car_rect):
        """Определяет пересечение машинки и заправки, если соприкасаются, то
           включаются все функции заправки"""
        if self.rect.colliderect(car_rect):
            self.true_pos = True
        else:
            self.true_pos = False
