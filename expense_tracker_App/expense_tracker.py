from expense import Expense
import calendar
import datetime


def main():
    print(f"Running expense Tracker")
    expense_file_path = "expense.csv"
    budget = 10000
    
    # Get user input foe expense.
    expense = get_user_expense()
    
    
    # write their expense to a file.
    save_expense_to_file(expense, expense_file_path)
    
    # Read file & summarize expenses.
    summarize_expense(expense_file_path, budget)
    
def get_user_expense():
    print(f"-> Getting user expense:")
    expense_name = input("1. Enter expense Name: ")
    expense_amount = float(input("2. Enter expense Amount: "))    
    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Other",
    ]
    
    while True:
        print("-> Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")
            
        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a categor number {value_range}: ")) - 1
        
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name = expense_name, amount = expense_amount,category = selected_category
            )
            return new_expense
        else:
            print("Invalid category. Please try again!")

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")    
    

def summarize_expense(expense_file_path, budget):
    print(f"-> Summarsing user expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            print(expense_name, expense_amount, expense_category)
            line_expense = Expense(
                name = expense_name, 
                amount = float(expense_amount), 
                category = expense_category
            )
            expenses.append(line_expense)
    
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("-> Expenses By Category :")
    for key, amount in amount_by_category.items():
        print(f"{key}: {amount:.2f} Rs")
        
    total_spent = sum([x.amount for x in expenses])
    print(f"Total Spent: {total_spent:.2f} Rs")
    
    remaining_budget = budget - total_spent
    print(f"Budget Remaining: {remaining_budget:.2f} Rs")
    
    
    remaining_budget = budget - total_spent
    print(f"✅ Budget Remaining: {remaining_budget:.2f} Rs")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(green(f"👉 Budget Per Day: {daily_budget:.2f} Rs"))


def green(text):
    return f"\033[92m{text}\033[0m"

if __name__ =="__main__":
    main()