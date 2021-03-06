import time
import pygame


class Notifications:
    def __init__(self, surface, text):
        self.number = 0
        self.surface = surface
        self.font = pygame.font.SysFont("arial", 40)
        self.background_color = (0, 0, 0)
        self.text = text
        self.current_y = 0
        self.render_font = self.font.render(self.text, True, (255, 255, 255), self.background_color)
        self.font_rect = self.render_font.get_rect()
        self.__class__.start_timer = time.time()

    def info(self):
        self.background_color = (0, 64, 138)
        self.render_font = self.font.render(self.text, True, (255, 255, 255), self.background_color)
        self.surface.blit(self.render_font, (self.current_y, 50))
        self.number += 1

    def warning(self):
        self.background_color = (219, 204, 0)
        self.render_font = self.font.render(self.text, True, (255, 255, 255), self.background_color)
        self.surface.blit(self.render_font, (self.current_y, 50))
        self.number += 1

    def error(self):
        self.background_color = (255, 43, 43)
        self.render_font = self.font.render(self.text, True, (255, 255, 255), self.background_color)
        self.surface.blit(self.render_font, (self.current_y, 50))
        self.number += 1

    def __repr__(self):
        return f"Notifications()"
