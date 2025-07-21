balance = 0
is_running = True

def current_balance():
    global balance
    print(f"Your current balance is: ${balance:.2f}")

def deposit():
    global balance
    amount = float(input("Enter the amount to deposit: "))
    if amount < 0:
        print("Deposit amount must be positive.")
    else:
        balance += amount
        print(f"You have successfully deposited ${amount:.2f}.")

def withdraw():
    global balance
    amount = float(input("Enter the amount to withdraw: "))
    if amount < 0:
        print("Withdrawal amount must be positive.")
    elif amount > balance:
        print("Insufficient funds for this withdrawal.")
    else:
        balance -= amount
        print(f"You have successfully withdrawn ${amount:.2f}.")

def main():
    global is_running
    while is_running:
        print("\nWelcome to the Banking System")
        print("1. Check Current Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Please select an option (1-4): ")
        if choice == '1':
            current_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            print("Thank you for using the Banking System. Goodbye!")
            is_running = False
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
