class Stats:
    """Статистика игрока"""
    def __init__(self, db):
        self.db = db
        self.money = db.cursor.execute("SELECT money FROM stats").fetchone()[0]
        self.number_of_liters = db.cursor.execute("SELECT liter FROM stats").fetchone()[0]

    def get_money(self):
        return self.money

    def set_money(self, amount):
        """
        Изменяет кол-во денег, в amount можно передавать отриц. значения,
        работать будет корректно
        """
        new_amount_money = self.db.update_money(amount)
        return new_amount_money

    def get_liters(self):
        return self.number_of_liters

    def set_liters(self, amount):
        """
        Изменяет кол-во литров топлива, принцип работы
        такой же как у set_money
        """
        new_amount_liters = self.db.update_liter(amount)
        return new_amount_liters
