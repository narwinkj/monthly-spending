import csv
import os
import datetime
import matplotlib.pyplot as plt

FILE_NAME = "my_budget.csv"

def setup_file():
    """Creates the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            # Writing the header row as a list
            writer.writerow(["Date", "Category", "Amount"])

def record_expense():
    """Collects expense data and appends it to the CSV file."""
    print("\n--- Add New Expense ---")
    category = input("Enter category (Food/Travel/Study/Misc): ").strip().capitalize()
    amount_str = input("Enter amount spent: ").strip()

    # Standard try-except block for validation (NCERT Exception Handling)
    try:
        amount = float(amount_str)
    except ValueError:
        print("Error: Please enter a valid numerical amount.")
        return

    # Getting today's date using the datetime module
    today = str(datetime.date.today())

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        # Appending data as a list row
        writer.writerow([today, category, amount])
    
    print(f"Successfully recorded: ₹{amount} spent on {category}.")

def show_all_expenses():
    """Reads and displays all records from the CSV file."""
    setup_file()
    
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        header = next(reader) # Skips the header row
        
        records = list(reader)

    if len(records) == 0:
        print("\nNo expenses found to display.")
        return

    print("\n" + "="*40)
    print(f"{header[0]:<12} | {header[1]:<15} | {header[2]}")
    print("="*40)
    
    # Iterating through rows as standard lists
    for row in records:
        print(f"{row[0]:<12} | {row[1]:<15} | ₹{row[2]}")
    print("="*40 + "\n")

def get_category_totals():
    """Helper function to calculate totals per category using standard dictionaries."""
    setup_file()
    totals = {}

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader) # Skip header
        
        for row in reader:
            cat = row[1]
            amt = float(row[2])
            
            # Standard NCERT style dictionary membership check
            if cat in totals:
                totals[cat] = totals[cat] + amt
            else:
                totals[cat] = amt
                
    return totals

def display_summary():
    """Prints the category-wise breakdown and returns the grand total."""
    totals = get_category_totals()
    
    if not totals:
        print("\nNo records available to summarize.")
        return 0

    print("\n--- Category-Wise Breakdown ---")
    for cat in totals:
        print(f" * {cat}: ₹{totals[cat]:.2f}")
    
    grand_total = sum(totals.values())
    print(f"Total Expenditure: ₹{grand_total:.2f}\n")
    return grand_total

def verify_budget():
    """Checks total expenses against a user-defined budget limit."""
    limit_input = input("Enter your monthly budget limit: ").strip()
    try:
        budget_limit = float(limit_input)
    except ValueError:
        print("Invalid budget amount.")
        return

    total_spent = display_summary()
    balance = budget_limit - total_spent

    if balance >= 0:
        print(f"Good job! You are within budget. Remaining balance: ₹{balance:.2f}\n")
    else:
        print(f"Alert! You have exceeded your budget by: ₹{abs(balance):.2f}\n")

def generate_plots():
    """Creates standard Matplotlib visualizations based on the data."""
    totals = get_category_totals()
    
    if not totals:
        print("\nAdd some data before attempting to generate charts.")
        return

    # Extracting keys and values into separate lists for plotting
    categories = list(totals.keys())
    amounts = list(totals.values())

    # Chart 1: Pie Chart
    plt.figure("Expense Distribution")
    plt.pie(amounts, labels=categories, autopct="%1.1f%%")
    plt.title("Expenses by Category")
    
    # Chart 2: Bar Chart
    plt.figure("Expense Bar Graph")
    plt.bar(categories, amounts, color="lightgreen", edgecolor="black")
    plt.xlabel("Categories")
    plt.ylabel("Amount in ₹")
    plt.title("Category-wise Spending")
    
    print("\nDisplaying charts... Close the window to return to the menu.")
    plt.show()

def menu():
    """Main program control loop."""
    setup_file()
    
    while True:
        print("===== TRACKER MENU =====")
        print("1. Log an Expense")
        print("2. View Expense Log")
        print("3. View Summary Breakdown")
        print("4. Check Budget Status")
        print("5. Generate Data Charts")
        print("6. Shutdown Application")
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == "1":
            record_expense()
        elif choice == "2":
            show_all_expenses()
        elif choice == "3":
            display_summary()
        elif choice == "4":
            verify_budget()
        elif choice == choice == "5":
            generate_plots()
        elif choice == "6":
            print("\nApplication closing. Have a great day!")
            break
        else:
            print("Invalid input. Please choose a valid option.\n")

if __name__ == "__main__":
    menu()
