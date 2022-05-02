import pygame.font


class StatePlayer:
    """Задает состояния в игре"""
    def __init__(self, car, background, list_cop_cars, screen):
        self.car = car
        self.background = background
        self.list_cop_cars = list_cop_cars
        self.screen = screen
        if not car.status_player():
            self.car.speed = 0
            self.background.speed = 0
            for cop in self.list_cop_cars:
                cop.speed = 0
            black_background = pygame.Surface((1000, 1000))
            black_background.fill((0, 0, 0))
            black_background.set_alpha(100)
            self.screen.blit(black_background, (0, 0))
            self.draw_text()

    def game_over(self):
        """Останавливает все спрайты в игре"""
        self.car.speed = 0
        self.background.speed = 0
        for cop in self.list_cop_cars:
            cop.speed = 0
        self.draw_text()

    def draw_text(self):
        font = pygame.font.SysFont('serif', 100)
        text = font.render("GAME OVER", True, (0, 0, 0), (255, 255, 255))
        text_rect = text.get_rect(center=(500, 300))
        self.screen.blit(text, text_rect)
