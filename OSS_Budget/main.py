from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 연봉 입력")
        print("2. 지출 추가")
        print("3. 지출 목록 보기")
        print("4. 연봉 대비 지출 퍼센트 보기")
        print("5. 종료")
        choice = input("선택 > ")

        if choice == "1":
            try:
                salary = int(input("연봉을 입력하시오(만원): "))
                budget.set_annual_salary(salary)
            except ValueError:
                print("잘못된 입력입니다. 숫자만 입력해주세요.\n")
                continue

        elif choice == "2":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "3":
            budget.list_expenses()

        elif choice == "4":
            budget.salary_percent()

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
