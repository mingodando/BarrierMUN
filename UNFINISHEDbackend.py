import os

file_name = "data.txt"

def create_file():
    """Create a text file with a unique name in the current directory."""
    with open(file_name, 'w') as file:
        file.write("Date / Month / Year                     Amount                             Details")

def insert_data():
    """Insert data into the text file."""
    date, money, details, month, year = input_data()
    with open(file_name, 'a') as file:
        file.write(f"\n{date} / {month} / {year}                          {money}                                 {details}")

def input_data():
    """Prompt users for transaction details and return them."""
    while True:
        # Date
        try:
            date_input = int(input("Enter the transaction date (1-31): "))
        except ValueError:
            print("Invalid date. Please enter a number between 1 and 31.")
            continue
        if not (1 <= date_input <= 31):
            print("Invalid date. Please enter a number between 1 and 31.")
            continue

        # Month
        try:
            month_input = int(input("Enter the transaction month (1-12): "))
        except ValueError:
            print("Invalid month. Please enter a number between 1 and 12.")
            continue
        if not (1 <= month_input <= 12):
            print("Invalid month. Please enter a number between 1 and 12.")
            continue

        # Year
        try:
            year_input = int(input("Enter the transaction year (<= 2026): "))
        except ValueError:
            print("Invalid year. Please enter a valid year (number).")
            continue
        if year_input > 2026:
            print("Invalid year. Please enter a year less than or equal to 2026.")
            continue

        # Amount
        try:
            money_input = int(input("Enter the transaction amount (>= 0): "))
        except ValueError:
            print("Invalid amount. Please enter a non-negative number.")
            continue
        if money_input < 0:
            print("Invalid amount. Please enter a non-negative number.")
            continue

        # Details
        details_input = input("Enter the transaction details: ")

        # If we reach here, all inputs are valid
        return date_input, money_input, details_input, month_input, year_input

if os.path.exists(file_name):
    print("File already exists.")
    insert_data()
else:
    create_file()
    insert_data()