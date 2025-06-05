
class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"[{self.date}] {self.category} - {self.description}: {self.amount:,}원"


class Investment:
    def __init__(self, date, stock_name, amount):
        self.date = date
        self.stock_name = stock_name
        self.amount = amount

    def __str__(self):
        return f"[{self.date}] 주식: {self.stock_name} - {self.amount:,}원"