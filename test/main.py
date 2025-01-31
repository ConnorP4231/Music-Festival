def management(tickets, profit, attendees, one_day, three_day, one_day_VIP, three_day_VIP, attendee_names):
    end_function = False
    while not end_function:
        choice = input("""
Options:
1. Add tickets to total tickets
2. Remove tickets from total tickets
3. View current ticket stats
4. Exit

Answer (1, 2, 3, 4): """)

        if choice == '1':
            typetickets = input("What type of tickets did you sell? (1: 1-day, 2: 3-day, 3: 1-day VIP, 4: 3-day VIP): ")
            try:
                cost = int(input('How much does one ticket cost?: '))
                num_tickets = int(input('How many did you sell?: '))

                if num_tickets < 0 or cost < 0:
                    print('Invalid input. Numbers must be positive.')
                    continue

                money = cost * num_tickets
                profit += money

                if typetickets == '1':
                    one_day += num_tickets
                elif typetickets == '2':
                    three_day += num_tickets
                elif typetickets == '3':
                    one_day_VIP += num_tickets
                elif typetickets == '4':
                    three_day_VIP += num_tickets
                else:
                    print('Invalid ticket type.')
                    continue

                print(f'Addition Successful! (You made ${money}).')

            except ValueError:
                print('Type a valid number.')

        elif choice == '2':
            typetickets = input("What type of tickets do you want to subtract? (1: 1-day, 2: 3-day, 3: 1-day VIP, 4: 3-day VIP): ")
            try:
                cost_remove = int(input('How much does one ticket cost?: '))
                num_tickets_remove = int(input('How many do you want to refund?: '))

                if num_tickets_remove < 0 or cost_remove < 0:
                    print('Invalid input. Numbers must be positive.')
                    continue

                refund_amount = cost_remove * num_tickets_remove
                if refund_amount > profit:
                    print(f'Not enough money to refund ${refund_amount}.')
                    continue

                if typetickets == '1' and num_tickets_remove <= one_day:
                    one_day -= num_tickets_remove
                elif typetickets == '2' and num_tickets_remove <= three_day:
                    three_day -= num_tickets_remove
                elif typetickets == '3' and num_tickets_remove <= one_day_VIP:
                    one_day_VIP -= num_tickets_remove
                elif typetickets == '4' and num_tickets_remove <= three_day_VIP:
                    three_day_VIP -= num_tickets_remove
                else:
                    print('Not enough tickets to refund or invalid ticket type.')
                    continue

                profit -= refund_amount
                print('Subtraction Successful!')

            except ValueError:
                print('Type a valid number.')

        elif choice == '3':
            print("\nCurrent Ticket Stats:")
            print(f"Total Tickets Sold: {one_day + three_day + one_day_VIP + three_day_VIP}")
            print(f"1-day Tickets: {one_day}")
            print(f"3-day Tickets: {three_day}")
            print(f"1-day VIP Tickets: {one_day_VIP}")
            print(f"3-day VIP Tickets: {three_day_VIP}")
            print(f"Total Profit: ${profit}\n")

        elif choice == '4':
            print("Exiting...\nFinal Stats:")
            print(f"Total Tickets Sold: {one_day + three_day + one_day_VIP + three_day_VIP}")
            print(f"1-day Tickets: {one_day}")
            print(f"3-day Tickets: {three_day}")
            print(f"1-day VIP Tickets: {one_day_VIP}")
            print(f"3-day VIP Tickets: {three_day_VIP}")
            print(f"Total Profit: ${profit}")
            end_function = True
        else:
            print('Invalid option, try again.')

    return tickets, profit, attendees, one_day, three_day, one_day_VIP, three_day_VIP, attendee_names


# Initialize values
tickets = 0
profit = 0
attendees = 0
one_day = 0
three_day = 0
one_day_VIP = 0
three_day_VIP = 0
attendee_names = []

# Run the function
tickets, profit, attendees, one_day, three_day, one_day_VIP, three_day_VIP, attendee_names = management(
    tickets, profit, attendees, one_day, three_day, one_day_VIP, three_day_VIP, attendee_names
)
