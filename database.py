import sqlite3


class DataBase:
    """Инициализирует БД, таблицу. Имеет методы получения,изменения данных"""

    def __init__(self):
        self.base = sqlite3.connect("game.db")
        self.cursor = self.base.cursor()
        self.base.execute("""CREATE TABLE IF NOT EXISTS stats (money, shell, hp, player_registered)""")

    def add_record(self):
        self.cursor.execute("INSERT INTO stats(money, shell, hp, player_registered) VALUES (?, ?, ?, ?)",
                            (0, 100, 100, True))
        self.base.commit()

    def get_money(self):
        return int(self.cursor.execute("SELECT money FROM stats").fetchone()[0])

    def update_money(self, amount):
        old_money = self.cursor.execute("SELECT money FROM stats").fetchone()[0]
        new_money = int(old_money) + amount
        if amount == 0:
            self.cursor.execute("UPDATE stats SET money = ?", (0,))
        else:
            self.cursor.execute("UPDATE stats SET money = ?", (new_money,))
        self.base.commit()
        new_money_from_db = self.cursor.execute("SELECT money FROM stats").fetchone()[0]
        return int(new_money_from_db)

    def get_shells(self):
        return int(self.cursor.execute("SELECT shell FROM stats").fetchone()[0])

    def update_shells(self, amount):
        old_shells = self.cursor.execute("SELECT shell FROM stats").fetchone()[0]
        new_shells = int(old_shells) + amount
        if amount == 0:
            self.cursor.execute("UPDATE stats SET shell = ?", (0,))
        else:
            self.cursor.execute("UPDATE stats SET shell = ?", (new_shells,))
        self.base.commit()
        new_shells_from_db = self.cursor.execute("SELECT shell FROM stats").fetchone()[0]
        return int(new_shells_from_db)

    def get_hp(self):
        return int(self.cursor.execute("SELECT hp FROM stats").fetchone()[0])

    def update_hp(self, amount):
        old_hp = self.cursor.execute("SELECT hp FROM stats").fetchone()[0]
        new_hp = int(old_hp) + amount
        if amount == 0:
            self.cursor.execute("UPDATE stats SET hp = ?", (0,))
        else:
            self.cursor.execute("UPDATE stats SET hp = ?", (new_hp,))
        self.base.commit()
        new_hp_from_db = self.cursor.execute("SELECT hp FROM stats").fetchone()[0]
        return int(new_hp_from_db)

    def __repr__(self):
        return f"DataBase()"
