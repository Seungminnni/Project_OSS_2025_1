import datetime
from expense import Expense, Investment

class Budget:
    def __init__(self):
        self.expenses = []
        self.investments = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def add_investment(self, stock_name, amount):
        today = datetime.date.today().isoformat()
        investment = Investment(today, stock_name, amount)
        self.investments.append(investment)
        print("투자가 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def list_investments(self):
        if not self.investments:
            print("투자 내역이 없습니다.\n")
            return
        print("\n[투자 목록]")
        for idx, i in enumerate(self.investments, 1):
            print(f"{idx}. {i}")
        print()

    def total_spent_and_invested(self):
        expense_total = sum(e.amount for e in self.expenses)
        investment_total = sum(i.amount for i in self.investments)
        total = expense_total + investment_total
        
        print(f"총 지출: {expense_total:,}원")
        print(f"총 투자: {investment_total:,}원")
        print(f"총 비용: {total:,}원\n")


