from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 투자 추가")
        print("3. 총 지출 및 투자 내역 보기")
        print("4. 투자 목록 보기")
        print("5. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
                if amount <= 0:
                    print("금액은 양수여야 합니다.\n")
                    continue
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            stock_name = input("주식명: ")
            try:
                amount = int(input("투자 금액(원): "))
                if amount <= 0:
                    print("금액은 양수여야 합니다.\n")
                    continue
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_investment(stock_name, amount)

        elif choice == "3":
            budget.list_expenses()
            budget.list_investments()
            budget.total_spent_and_invested()

        elif choice == "4":
            budget.list_investments()

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
