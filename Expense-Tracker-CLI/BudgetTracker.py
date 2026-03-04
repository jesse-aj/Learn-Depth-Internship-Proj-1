"""
Expense Tracker CLI Application
A simple command-line app to manage daily expenses.
"""

import json
import os
from datetime import datetime


# We store all expenses in a JSON file so data persists between runs.
DATA_FILE = "expenses.json"


def load_expenses():
    """Load expenses from the JSON file. Returns an empty list if file doesn't exist."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_expenses(expenses):
    """Save the current expenses list back to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)



def add_expense(expenses):
    """
    Prompt the user for an expense name and amount,
    then append it to the expenses list with a timestamp.
    """
    print("\n--- Add New Expense ---")
    name = input("Enter Expense: ").strip()

    # Keep asking until the user enters a valid number
    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be greater than zero. Try again.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    expense = {
        "id": len(expenses) + 1,          # simple auto-increment ID
        "name": name,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    expenses.append(expense)
    save_expenses(expenses)

    total = sum(e["amount"] for e in expenses)
    print("\nExpense Added Successfully ✓")
    print(f"Total Expenses: {total:.2f}")


def view_expenses(expenses):
    """
    Display all recorded expenses in a neat table,
    then show the running total at the bottom.
    """
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    # Table header
    print(f"{'ID':<5} {'Expense':<20} {'Amount':>10}  {'Date'}")
    print("-" * 55)

    for e in expenses:
        print(f"{e['id']:<5} {e['name']:<20} {e['amount']:>10.2f}  {e['date']}")

    print("-" * 55)
    total = sum(e["amount"] for e in expenses)
    print(f"{'TOTAL':<26} {total:>10.2f}")


def calculate_total(expenses):
    """Print just the grand total — useful as a quick check."""
    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal Spending: {total:.2f}")


def delete_expense(expenses):
    """
    Show all expenses, ask for an ID to delete,
    remove it, then re-number remaining IDs so there are no gaps.
    """
    print("\n--- Delete an Expense ---")

    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses(expenses)

    while True:
        try:
            expense_id = int(input("\nEnter the ID of the expense to delete: "))
            # Find the expense with the matching ID
            target = next((e for e in expenses if e["id"] == expense_id), None)
            if target is None:
                print("ID not found. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    expenses.remove(target)

    # Re-number IDs after deletion to keep them sequential
    for i, e in enumerate(expenses, start=1):
        e["id"] = i

    save_expenses(expenses)
    print(f"Expense '{target['name']}' deleted successfully ✓")



def show_menu():
    """Print the main menu options."""
    print("\n╔══════════════════════════════╗")
    print("║     DAILY EXPENSE TRACKER    ║")
    print("╠══════════════════════════════╣")
    print("║  1. Add New Expense          ║")
    print("║  2. View All Expenses        ║")
    print("║  3. Calculate Total Spending ║")
    print("║  4. Delete an Expense        ║")
    print("║  5. Exit                     ║")
    print("╚══════════════════════════════╝")


def main():
    """
    Main loop — load expenses once at startup,
    then keep showing the menu until the user exits.
    """
    expenses = load_expenses()

    print("\nWelcome to your Expense Tracker!")

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            calculate_total(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("\nGoodbye! Stay on budget always\n")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")



if __name__ == "__main__":
    main()