import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    # 연봉 정보 추가
    def set_annual_salary(self, salary_in_man):
        self.annual_salary = salary_in_man * 10000  # 만원 단위를 원 단위로 변환
        print(f"연봉이 {self.annual_salary:,}원으로 설정되었습니다.\n")

    def salary_percent(self):
        total = sum(e.amount for e in self.expenses)
        if hasattr(self, 'annual_salary') and self.annual_salary > 0:
            percent = (total / self.annual_salary) * 100
            print(f"연봉 대비 지출 비율: {percent:.2f}%\n")
        else:
            print("연봉이 설정되지 않았습니다.\n")


