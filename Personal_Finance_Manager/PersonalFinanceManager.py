finances = {'income': [], 'expenses': []}

def addIncome(amount: float, source: str):
    """Add income to the finance manager."""
    finances['income'].append({'amount': amount, 'source': source})
    print(f"\tAdded income: Rs.{amount:.2f} from {source}")

def addExpense(amount: float, description: str):
    """Add an expense to the finance manager."""
    finances['expenses'].append({'amount': amount, 'description': description})
    print(f"\tAdded expense: Rs.{amount:.2f} for {description}")

def calculateSavings() -> float:
    """Calculate the total savings."""
    totalIncome = sum(i['amount'] for i in finances['income'])
    totalExpenses = sum(e['amount'] for e in finances['expenses'])
    return totalIncome - totalExpenses

def get_float_input(prompt: str) -> float:
    """Helper function to get and validate float input from the user."""
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def show_incomes():
    """Display all recorded incomes."""
    if finances['income']:
        print("\nRecorded Incomes:")
        for income in finances['income']:
            print(f"\tRs.{income['amount']:.2f} from {income['source']}")
    else:
        print("No incomes recorded.")

def show_expenses():
    """Display all recorded expenses."""
    if finances['expenses']:
        print("\nRecorded Expenses:")
        for expense in finances['expenses']:
            print(f"\tRs.{expense['amount']:.2f} for {expense['description']}")
    else:
        print("No expenses recorded.")

def main():
    """Run the personal finance manager application."""
    while True:
        print("\nPersonal Finance Manager")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Incomes")
        print("4. View Expenses")
        print("5. Calculate Savings")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            amount = get_float_input("\tEnter income amount: Rs.")
            source = input("\tEnter income source: ").strip()
            addIncome(amount, source)
        
        elif choice == '2':
            amount = get_float_input("\tEnter expense amount: Rs.")
            description = input("\tEnter expense description: ").strip()
            addExpense(amount, description)
        
        elif choice == '3':
            show_incomes()
        
        elif choice == '4':
            show_expenses()
        
        elif choice == '5':
            savings = calculateSavings()
            print(f"Total Savings: Rs.{savings:.2f}")
        
        elif choice == '6':
            print("Exiting Personal Finance Manager.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()