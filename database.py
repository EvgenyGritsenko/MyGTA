import sqlite3
import pygame

class DataBase:
    """Инициализирует БД, таблицу. Имеет методы получения,изменения данных"""
    def __init__(self):
        self.base = sqlite3.connect("game.db")
        self.cursor = self.base.cursor()
        self.base.execute("""CREATE TABLE IF NOT EXISTS stats (money, liter, player_registered)""")

    def add_record(self):
        self.cursor.execute("INSERT INTO stats(money, liter, player_registered) VALUES (?, ?, ?)", (0, 30, True))
        self.base.commit()

    def get_money(self):
        return self.cursor.execute("SELECT money FROM stats").fetchone()[0]

    def update_money(self, amount):
        old_money = self.cursor.execute("SELECT money FROM stats").fetchone()[0]
        new_money = int(old_money) + amount
        if new_money >= 0:
            self.cursor.execute("UPDATE stats SET money = ?", (new_money,))
            self.base.commit()
            return new_money

    def get_liter(self):
        return self.cursor.execute("SELECT liter FROM stats").fetchone()[0]

    def update_liter(self, amount):
        old_liter = self.cursor.execute("SELECT liter FROM stats").fetchone()[0]
        new_liter = int(old_liter) + amount
        if new_liter >= 0:
            self.cursor.execute(f"UPDATE stats SET liter = ?", (new_liter,))
            self.base.commit()
            return new_liter

