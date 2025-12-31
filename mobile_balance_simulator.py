current_balance = 10.0  # Initial balance (can be any value)

while True:
    print("\n--- Mobile Menu ---")
    print("1. Check Balance")
    print("2. Recharge Balance")
    print("3. Subscribe Package")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is: ${current_balance}")

    elif choice == "2":
        recharge = float(input("Enter recharge amount: "))
        if recharge > 0:
            current_balance += recharge
            print(f"Recharge successful! New balance: ${current_balance}")
        else:
            print("Invalid recharge amount.")

    elif choice == "3":
        print("\nAvailable Packages:")
        print("1. Daily Package - $2")
        print("2. Weekly Package - $5")
        print("3. Monthly Package - $10")

        pkg = input("Select package (1-3): ")

        if pkg == "1":
            price = 2
            pkg_name = "Daily Package"
        elif pkg == "2":
            price = 5
            pkg_name = "Weekly Package"
            
        elif pkg == "3":  
            price = 10
            pkg_name = "Monthly Package"
        else:
            print("Invalid package choice.")
            continue

        if current_balance >= price:
            current_balance -= price
            print(f"{pkg_name} subscribed successfully!")
            print(f"Remaining balance: ${current_balance}")
        else:
            print("Insufficient balance to subscribe this package.")

    elif choice == "4":
        print("Thank you for using the Mobile Simulator. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1-4.")