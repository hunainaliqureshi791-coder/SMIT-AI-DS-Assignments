total_seats_available = 50  # Global seat counter

while True:
    print("\n--- Bus Ticket Booking Menu ---")
    print("1. Book Ticket")
    print("2. Check Available Seats")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        if total_seats_available == 0:
            print("Sorry! No seats available.")
            continue

        print("\nAvailable Routes:")
        print("1. Karachi - Rs. 1500")
        print("2. Lahore - Rs. 2500")

        route_choice = input("Select route (1-2): ")

        if route_choice == "1":
            destination = "Karachi"
            ticket_price = 1500
        elif route_choice == "2":
            destination = "Lahore"
            ticket_price = 2500
        else:
            print("Invalid route selection.")
            continue

        name = input("Enter passenger name: ")
        seats = int(input("Enter number of seats: "))

        if seats <= total_seats_available:
            total_cost = seats * ticket_price
            total_seats_available -= seats

            print("\n--- Ticket Summary ---")
            print(f"Passenger Name : {name}")
            print(f"Destination    : {destination}")
            print(f"Seats Booked   : {seats}")
            print(f"Total Cost    : Rs. {total_cost}")
            print(f"Seats Left    : {total_seats_available}")
        else:
            print("Booking Failed: Not enough space.")

    elif choice == "2":
        print(f"Total seats available: {total_seats_available}")

    elif choice == "3":
        print("Thank you for using the Bus Ticket Booking System.")
        break

    else:
        print("Invalid choice! Please select 1-3.")