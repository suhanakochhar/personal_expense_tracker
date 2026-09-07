import csv
from datetime import date
import matplotlib.pyplot as plt

expenses = []
budget = 0

try:
    with open("expenses.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expenses.append({
                "name": row["name"],
                "amount": float(row["amount"]),
                "category": row["category"],
                "date": row["date"]
            })

except FileNotFoundError:
    pass


while True:
    print("========================")
    print("  PERSONAL EXPENSE TRACKER")
    print("========================")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spent")
    print("4. View Category Summary")
    print("5. Delete Expense")
    print("6. Monthly Spending Summary")
    print("7. Set Monthly Budget")
    print("8. Spending Chart")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        expense_name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        expense = {
            "name": expense_name,
            "amount": amount,
            "category": category,
            "date": str(date.today())
        }

        expenses.append(expense)

        with open("expenses.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["name", "amount", "category", "date"]
            )

            writer.writeheader()
            writer.writerows(expenses)

        print("Expense added successfully!")

    elif choice == "2":
        print("\nYour Expenses:")

        for expense in expenses:
            print(
                expense["name"],
                "$" + str(expense["amount"]),
                expense["category"],
                expense["date"]
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
                expenses[i]["category"],
                expenses[i]["date"]
            )

        number = int(input("Enter the expense number to delete: "))

        if number >= 1 and number <= len(expenses):
            deleted_expense = expenses.pop(number - 1)

            with open("expenses.csv", "w", newline="") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=["name", "amount", "category", "date"]
                )

                writer.writeheader()
                writer.writerows(expenses)

            print(deleted_expense["name"] + " deleted successfully!")

        else:
            print("Invalid expense number.")

    elif choice == "6":
        print("\nMonthly Spending Summary:")

        months = {}

        for expense in expenses:
            month = expense["date"][:7]
            amount = expense["amount"]

            if month in months:
                months[month] += amount
            else:
                months[month] = amount

        for month in months:
            print(month + ": $" + str(months[month]))

    elif choice == "7":
        budget = float(input("Enter your monthly budget: "))

        total = 0

        for expense in expenses:
            total += expense["amount"]

        remaining = budget - total

        print("Monthly Budget: $" + str(budget))
        print("Total Spent: $" + str(total))
        print("Remaining Budget: $" + str(remaining))

        if remaining < 0:
            print("You have exceeded your budget!")
        else:
            print("You are within your budget!")

    elif choice == "8":
        categories = {}

        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

        if len(categories) == 0:
            print("No expenses to display.")
        else:
            plt.bar(categories.keys(), categories.values())
            plt.title("Spending by Category")
            plt.xlabel("Category")
            plt.ylabel("Amount Spent ($)")

            plt.savefig("spending_chart.png")
            plt.close()

            print("Spending chart created successfully!")
            
    elif choice == "9":
        print("Goodbye!")
        break