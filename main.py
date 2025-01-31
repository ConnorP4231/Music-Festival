def management():
    tickets = 0
    profit = 0
    attendees = 0
    one_day = 0
    three_day = 0
    one_day_VIP = 0
    three_day_VIP = 0
    attendee_names = []

    while True:
        choice = input("""
Options:
1. Add tickets to total tickets
2. Remove tickets from total tickets
3. Check attendees
4. Add a name to attendees and what type of ticket they have
5. Check ticket sales
6. Check ticket profits
7. Exit

Answer (1-7): """)

        if choice == '1':  # Adding tickets
            while True:
                try:
                    typetickets = int(input("What type of tickets? (1: 1-day, 2: 3-day, 3: 1-day VIP, 4: 3-day VIP): "))
                    if typetickets not in [1, 2, 3, 4]:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter 1, 2, 3, or 4.")

            while True:
                try:
                    cost = int(input("How much does one ticket cost?: "))
                    num_tickets = int(input("How many tickets did you sell?: "))
                    if cost < 0 or num_tickets < 0:
                        print("Invalid input. Values must be positive.")
                        continue
                    break
                except ValueError:
                    print("Please enter valid numbers.")

            profit += cost * num_tickets
            if typetickets == 1:
                one_day += num_tickets
            elif typetickets == 2:
                three_day += num_tickets
            elif typetickets == 3:
                one_day_VIP += num_tickets
            elif typetickets == 4:
                three_day_VIP += num_tickets

            print(f'Addition Successful! (You made ${cost * num_tickets}).')

        elif choice == '2':  # Removing (refunding) tickets
            while True:
                try:
                    typetickets = int(input("What type of tickets to refund? (1: 1-day, 2: 3-day, 3: 1-day VIP, 4: 3-day VIP): "))
                    if typetickets not in [1, 2, 3, 4]:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter 1, 2, 3, or 4.")

            while True:
                try:
                    cost_remove = int(input("How much does one ticket cost?: "))
                    num_tickets_remove = int(input("How many tickets to refund?: "))
                    if cost_remove < 0 or num_tickets_remove < 0:
                        print("Invalid input. Values must be positive.")
                        continue
                    break
                except ValueError:
                    print("Please enter valid numbers.")

            refund_amount = cost_remove * num_tickets_remove
            if refund_amount > profit:
                print(f"Not enough money to refund ${refund_amount}.")
                continue

            ticket_types = {1: one_day, 2: three_day, 3: one_day_VIP, 4: three_day_VIP}
            if num_tickets_remove > ticket_types[typetickets]:
                print("Not enough tickets to refund.")
                continue

            # Deduct refunded tickets and update profit
            if typetickets == 1:
                one_day -= num_tickets_remove
            elif typetickets == 2:
                three_day -= num_tickets_remove
            elif typetickets == 3:
                one_day_VIP -= num_tickets_remove
            elif typetickets == 4:
                three_day_VIP -= num_tickets_remove

            profit -= refund_amount
            print("Refund Successful!")

        elif choice == '3':  # Check attendees
            print(f"Total attendees: {attendees}")
            if attendee_names:
                print("Attendee List:", ', '.join(attendee_names))
            else:
                print("No attendees yet.")

        elif choice == '4':  # Add attendee
            name = input("Enter attendee name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue

            while True:
                try:
                    ticket_type = int(input("Ticket Type (1: 1-day, 2: 3-day, 3: 1-day VIP, 4: 3-day VIP): "))
                    if ticket_type not in [1, 2, 3, 4]:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Enter 1, 2, 3, or 4.")

            attendee_names.append(name)
            attendees += 1
            print(f"{name} added successfully!")

        elif choice == '5':  # Check ticket sales
            print(f"Ticket Sales Summary:\n1-day: {one_day}\n3-day: {three_day}\n1-day VIP: {one_day_VIP}\n3-day VIP: {three_day_VIP}")

        elif choice == '6':  # Check profits
            print(f"Total Profit: ${profit}")

        elif choice == '7':  # Exit
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid option. Please enter a number between 1 and 7.")

management()
