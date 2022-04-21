"""Состояния игры (жизнь, смерть)"""


class StatePlayer:
    def __init__(self, car, background):
        if not car.status_player():
            car.speed = 0
            background.speed = 0
