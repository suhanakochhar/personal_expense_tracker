expenses = []

while True:
    print("========================")
    print("PERSONAL EXPENSE TRACKER")
    print("========================")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spent")
    print("4. View Category Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        expense_name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        expense = {
            "name": expense_name,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)

        print("Expense added successfully!")

    elif choice == "2":
        print("\nYour Expenses:")

        for expense in expenses:
            print(
                expense["name"],
                "$" + str(expense["amount"]),
                expense["category"]
            )

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("Total Spent: $" + str(total))

    elif choice == "4":
        print("\nCategory Summary: ")

        categories = {}

        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

        for category in categories:
            print(category + ": $" + str(categories[category]))

    elif choice == "5":
        print("Goodbye!")
        break