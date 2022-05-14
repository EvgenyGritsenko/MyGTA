import pygame.font
import controls


class StatusPlayer:
    def __init__(self, car, background, list_cop_cars, screen, pos, pressed, db):
        self.car = car
        self.background = background
        self.list_cop_cars = list_cop_cars
        self.screen = screen
        self.pos = pos
        self.pressed = pressed
        self.db = db
        # self.check_status()

    def check_status(self):
        if not self.car.status_player():
            StatusPlayerDeath()
        else:
            StatusPlayerRestart()


class StatusPlayerDeath(StatusPlayer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game_over()

    def game_over(self):
        self.background.speed = 0
        self.car.speed = 0
        for cop in self.list_cop_cars:
            self.list_cop_cars.remove(cop)
            cop.kill()
            controls.CAR_MOVE = False
        black_background = pygame.Surface((1000, 1000))
        black_background.fill((0, 0, 0))
        black_background.set_alpha(100)
        self.screen.blit(black_background, (0, 0))
        self.draw_text_game_over()
        # self.draw_button_game_over()
        # self.mouse_over()

    def draw_text_game_over(self):
        font = pygame.font.SysFont('serif', 100)
        text = font.render("GAME OVER", True, (0, 0, 0), (255, 255, 255))
        text_rect = text.get_rect(center=(500, 300))
        self.screen.blit(text, text_rect)

    # def draw_button_game_over(self):
    #     """Создается кнопка для возвращения в игру.
    #        Ну как кнопка, поверхность и текст на ней 😊 """
    #     button = pygame.Surface((400, 80))
    #     button.fill((150, 150, 150))
    #     button_rect = button.get_rect(center=(500, 420))
    #     font = pygame.font.SysFont('serif', 70)
    #     text_on_button = font.render("Возродиться", True, (255, 255, 255))
    #     button.blit(text_on_button, (10, 0))
    #     self.screen.blit(button, button_rect)
    #
    # def mouse_over(self):
    #     # (300, 380) (700, 380) (300, 460) (700, 460) - координаты поверхности кнопки
    #     range_x = [i for i in range(300, 700)]
    #     range_y = [j for j in range(380, 460)]
    #     if self.pos[0] in range_x and self.pos[1] in range_y:
    #         if self.pressed[0]:
    #             StatusPlayerRestart()

    def __repr__(self):
        return f"StatePlayer({self.car}, {self.background}, {self.list_cop_cars})" \
               f"{self.screen}"


class StatusPlayerRestart(StatusPlayer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def restart_game(self):
        self.background.speed = 3
        self.car.speed = 3
        self.db.update_hp(100)


class StatusPlayerPause(StatusPlayer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
