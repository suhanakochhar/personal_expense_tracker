import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date


st.set_page_config(
    page_title="Personal Expense Tracker",
    page_icon="💰",
    layout="centered"
)


# Store expenses for the current user session
if "expenses" not in st.session_state:
    st.session_state.expenses = []

if "budget" not in st.session_state:
    st.session_state.budget = 0.0


st.title("💰 Personal Expense Tracker")
st.write("Track your personal expenses and manage your monthly budget.")


# -------------------------
# Add Expense
# -------------------------

st.header("Add Expense")

with st.form("expense_form"):
    expense_name = st.text_input("Expense Name")
    amount = st.number_input(
        "Amount ($)",
        min_value=0.0,
        step=0.01
    )
    category = st.selectbox(
        "Category",
        [
            "Food",
            "Transportation",
            "Shopping",
            "Entertainment",
            "Bills",
            "Other"
        ]
    )

    submitted = st.form_submit_button("Add Expense")

    if submitted:
        if expense_name and amount > 0:
            expense = {
                "name": expense_name,
                "amount": amount,
                "category": category,
                "date": str(date.today())
            }

            st.session_state.expenses.append(expense)

            st.success("Expense added successfully!")
        else:
            st.warning("Please enter an expense name and amount.")


# -------------------------
# Expense Summary
# -------------------------

st.header("Expense Summary")

if len(st.session_state.expenses) == 0:

    st.info("No expenses added yet.")

else:

    total = 0

    for expense in st.session_state.expenses:
        total += expense["amount"]

    st.metric("Total Spent", f"${total:.2f}")

    # Create DataFrame
    df = pd.DataFrame(st.session_state.expenses)

    df["amount"] = df["amount"].astype(float)

    st.subheader("Your Expenses")

    st.dataframe(
        df,
        use_container_width=True
    )


    # -------------------------
    # Category Summary
    # -------------------------

    st.subheader("Spending by Category")

    categories = {}

    for expense in st.session_state.expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    for category in categories:
        st.write(
            f"**{category}:** ${categories[category]:.2f}"
        )


    # -------------------------
    # Spending Chart
    # -------------------------

    fig, ax = plt.subplots()

    ax.bar(
        categories.keys(),
        categories.values()
    )

    ax.set_title("Spending by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Amount Spent ($)")

    plt.xticks(rotation=30)

    st.pyplot(fig)


    # -------------------------
    # Monthly Spending
    # -------------------------

    st.subheader("Monthly Spending")

    months = {}

    for expense in st.session_state.expenses:
        month = expense["date"][:7]
        amount = expense["amount"]

        if month in months:
            months[month] += amount
        else:
            months[month] = amount

    for month in months:
        st.write(
            f"**{month}:** ${months[month]:.2f}"
        )


    # -------------------------
    # Delete Expense
    # -------------------------

    st.subheader("Delete Expense")

    expense_options = []

    for i, expense in enumerate(st.session_state.expenses):
        expense_options.append(
            f"{i + 1}. {expense['name']} - "
            f"${expense['amount']:.2f}"
        )

    selected_expense = st.selectbox(
        "Select an expense to delete",
        expense_options
    )

    if st.button("Delete Selected Expense"):

        selected_index = expense_options.index(
            selected_expense
        )

        deleted_expense = st.session_state.expenses.pop(
            selected_index
        )

        st.success(
            f"{deleted_expense['name']} deleted successfully!"
        )

        st.rerun()


# -------------------------
# Monthly Budget
# -------------------------

st.header("Monthly Budget")

budget = st.number_input(
    "Enter your monthly budget ($)",
    min_value=0.0,
    step=10.0,
    value=st.session_state.budget
)

st.session_state.budget = budget

total_spent = 0

for expense in st.session_state.expenses:
    total_spent += expense["amount"]

remaining = budget - total_spent

st.write(f"**Monthly Budget:** ${budget:.2f}")
st.write(f"**Total Spent:** ${total_spent:.2f}")
st.write(f"**Remaining Budget:** ${remaining:.2f}")

if budget > 0:

    if remaining < 0:
        st.error("You have exceeded your budget!")
    else:
        st.success("You are within your budget!")


# -------------------------
# Download Expenses
# -------------------------

if len(st.session_state.expenses) > 0:

    st.header("Download Your Expenses")

    download_df = pd.DataFrame(
        st.session_state.expenses
    )

    csv_data = download_df.to_csv(
        index=False
    )

    st.download_button(
        label="Download Expenses as CSV",
        data=csv_data,
        file_name="my_expenses.csv",
        mime="text/csv"
    )