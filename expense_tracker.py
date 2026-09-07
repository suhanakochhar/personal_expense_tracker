expenses = []

while True:
    print("========================")
    print("  PERSONAL EXPENSE TRACKER")
    print("========================")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spent")
    print("4. View Category Summary")
    print("5. Delete Expense")
    print("6. Exit")

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
        print("\nCategory Summary:")

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
        print("\nYour Expenses:")

        for i in range(len(expenses)):
            print(
                str(i + 1) + ".",
                expenses[i]["name"],
                "$" + str(expenses[i]["amount"]),
                expenses[i]["category"]
            )

        number = int(input("Enter the expense number to delete: "))

        if number >= 1 and number <= len(expenses):
            deleted_expense = expenses.pop(number - 1)
            print(deleted_expense["name"] + " deleted successfully!")
        else:
            print("Invalid expense number.")

    elif choice == "6":
        print("Goodbye!")
        break