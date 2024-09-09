import csv

# List of expense categories
categories = ['Food', 'Transport', 'Entertainment', 'Utilities', 'Miscellaneous']

# Function to add an expense
def add_expense(expenses):
    try:
        amount = float(input("Enter the amount spent: "))
        category = input(f"Enter the category ({', '.join(categories)}): ")
        if category not in categories:
            raise ValueError("Invalid category")
        description = input("Enter a brief description: ")
        expenses.append({'amount': amount, 'category': category, 'description': description})
    except ValueError as ve:
        print("Error:", ve)

# Function to save expenses to a file (CSV)
def save_expenses_to_file(expenses):
    with open('expenses.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Amount', 'Category', 'Description'])
        for expense in expenses:
            writer.writerow([expense['amount'], expense['category'], expense['description']])

# Function to analyze and display expense data
def analyze_expenses(expenses):
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: {total}")
    
    category_wise = {}
    for expense in expenses:
        category = expense['category']
        if category in category_wise:
            category_wise[category] += expense['amount']
        else:
            category_wise[category] = expense['amount']
    
    print("\nCategory-wise Expenses:")
    for category, amount in category_wise.items():
        print(f"{category}: {amount}")

# Main function providing a simple console interface
def main():
    expenses = []
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Save and Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            print(expenses)
        elif choice == '3':
            analyze_expenses(expenses)
        elif choice == '4':
            save_expenses_to_file(expenses)
            print("Expenses saved! Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
