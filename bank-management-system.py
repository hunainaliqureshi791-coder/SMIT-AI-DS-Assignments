class Account:
    def __init__(self, name, balance, pin):
        self.name = name
        self.__balance = balance   # Private attribute
        self.__pin = pin           # Private PIN

    def check_balance(self):
        print(f"Current Balance: ${self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount, entered_pin):
        if entered_pin != self.__pin:
            print("Incorrect PIN! Withdrawal denied.")
            return

        if amount > self.__balance:
            print("Insufficient balance! Cannot withdraw.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.__balance -= amount
            print(f"${amount} withdrawn successfully.")

# -------- Main Program --------
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))
pin = input("Set your 4-digit PIN: ")

account = Account(name, balance, pin)

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        account.check_balance()

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        entered_pin = input("Enter PIN: ")
        account.withdraw(amount, entered_pin)

    elif choice == "4":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid option. Try again.")
