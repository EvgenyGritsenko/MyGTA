import pygame
import time
import controls
import constants
import car


class StatusPlayer:
    def __init__(self, car, screen, list_cop_cars, bullets, bullets_cops,
                 bullets_box, get_health_group, bombs, db, police_car_group):
        self.db = db
        self.car = car
        self.screen = screen
        self.list_cop_cars = list_cop_cars
        self.bullets = bullets
        self.bullets_cops = bullets_cops
        self.bullets_box = bullets_box
        self.get_gealth_group = get_health_group
        self.bombs = bombs
        self.police_car_group = police_car_group
        self.check_status()

    def check_status(self):
        if not car.status_player():
            StatusPlayerDeath(self.screen, self.list_cop_cars, self.bullets,
                              self.bullets_cops, self.bullets_box, self.get_gealth_group,
                              self.bombs, self.db, self.police_car_group)

    def __repr__(self):
        return "StatusPLayer()"


class StatusPlayerDeath:
    def __init__(self, screen, list_cop_cars, bullets, bullets_cops,
                 bullets_box, get_health_group, bombs, db,
                 police_car_group):
        self.screen = screen
        self.list_cop_cars = list_cop_cars
        self.police_car_group = police_car_group
        self.bullets = bullets
        self.bullets_cops = bullets_cops
        self.bullets_box = bullets_box
        self.get_heath_group = get_health_group
        self.bombs = bombs
        self.db = db
        self.game_over()

    def game_over(self):
        self.list_cop_cars.clear()
        self.bullets.empty()
        self.bullets_cops.empty()
        self.bullets_box.empty()
        self.get_heath_group.empty()
        self.bombs.empty()
        self.police_car_group.empty()
        controls.STATE_OF_EVENTS = False
        pygame.mixer.music.stop()
        sound_game_over = pygame.mixer.Sound("sounds/game_over.mp3")
        sound_game_over.play()
        time.sleep(4)
        constants.TIMER_START = time.time()
        constants.SCORE = 1
        StatusPlayerRestart(self.screen, self.db)

    def __repr__(self):
        return "StatusPlayerDeath()"


class StatusPlayerRestart:
    def __init__(self, background, db):
        self.background = background
        self.db = db
        self.restart_game()

    def restart_game(self):
        controls.STATE_OF_EVENTS = True
        set_full_hp(self.db)
        pygame.mixer.music.load("sounds/music.mp3")
        pygame.mixer.music.play()


class StatusPlayerWin:
    def __init__(self, screen, db):
        print(constants.SCORE)
        self.screen = screen
        self.db = db
        self.image = pygame.image.load("images/win.png").convert_alpha()
        self.image_rect = self.image.get_rect(center=(1000/2, 200))
        if constants.SCORE >= 10:
            self.win()

    def win(self):
        controls.STATE_OF_EVENTS = False
        sound = pygame.mixer.Sound("sounds/WIN.mp3")
        pygame.mixer.music.stop()
        sound.play()
        self.db.update_money(1000000000)
        constants.WIN_PLAYER = False
        StatusPlayerRestart(self.screen, self.db)
        constants.SCORE = 10
        self.screen.blit(self.image, self.image_rect)

    def __repr__(self):
        return "StatusPlayerWin()"


def set_null_hp(db):
    db.update_hp(0)


def set_full_hp(db):
    db.update_hp(100)
