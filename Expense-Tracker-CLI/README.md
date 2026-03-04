# Expense Tracker CLI

A simple command-line application to track daily expenses, built with Python.

---

## Features

- Add a new expense with a name and amount
- View all recorded expenses in a table
- Calculate total spending
- Delete an expense by ID
- Data is saved automatically to a JSON file

---

## How to Run

Make sure you have Python installed, then run:

```bash
python expense_tracker.py
```

No external libraries needed — uses only Python's built-in modules.

---

## How to Use

When the program starts, you'll see a menu:

```
1. Add New Expense
2. View All Expenses
3. Calculate Total Spending
4. Delete an Expense
5. Exit
```

Just enter the number of the option you want.

---

## Example

```
Enter Expense: Food
Amount: 200

Expense Added Successfully ✓
Total Expenses: 200.00
```

---

## File Structure

```
expense_tracker.py   # Main program
expenses.json        # Auto-created when you add your first expense
```

---

## Built With

- Python 3
- `json` module — for saving/loading data
- `os` module — for checking if the data file exists
- `datetime` module — for timestamping each expense

---

## Author

Built as part of a Learn Depth internship assignment.