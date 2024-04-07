print("Welcome to Cash App!")
print("This app will help you develop better financial habits.")
def money_buckets():
    # Asks user for income amount
    income = float(input("Enter your monthly income amount: "))

    # Calculates bucket amounts
    blow_bucket = income * 0.6
    daily_expense = blow_bucket * 0.6
    splurge = blow_bucket * 0.1
    smile = blow_bucket * 0.1
    fire_extinguisher = blow_bucket * 0.2

    grow_bucket = income * 0.2
    mojo = income * 0.2

    # Displays bucket amounts
    print("\nMoney Buckets:")
    print(f"Blow: ${blow_bucket: }")
    print(f"\tDaily Expense: ${daily_expense: }")
    print(f"\tSplurge: ${splurge: }")
    print(f"\tSmile: ${smile: }")
    print(f"\tFire Extinguisher: ${fire_extinguisher: }")
    print(f"Grow: ${grow_bucket: }")
    print(f"Mojo: ${mojo: }")

def compound_interest():
    # Asks user for inputs
    start_age = int(input("Enter your start age: "))
    annual_interest_rate = float(input("Enter the average annual interest rate (in percentage): ")) / 100
    investment_amount = float(input("Enter the amount you will invest every year: "))

    # Initializes variables
    age = start_age
    savings = 0

    # Prints header
    print("\nCompound Interest Projection:")
    print("Age\tInvestment\tSavings")

    # Calculate and display savings projection until age 60
    while age <= 60:
        savings += investment_amount
        savings *= (1 + annual_interest_rate)
        print(f"{age}\t{investment_amount}\t${round(savings, 2)}")
        age += 1

choice = 0
while choice != "":
    print("\nPlease choose an option:")
    print("\n1. Money Buckets")
    print("Learning this strategy is to help you to live on 60% of your income and grow your wealth.")
    print("\n2. Compound Interest Projection")
    print("This function shows the development of your investment.")
    choice = input("\nEnter your choice (1 or 2): ")
    if choice == '1':
        money_buckets()
    elif choice == '2':
        compound_interest()
    restart = input("\nDo you want to restart? (yes/no): ")
    if restart.lower() != 'yes':
        break
print("\nThank you for using Cash App! Goodbye!")

