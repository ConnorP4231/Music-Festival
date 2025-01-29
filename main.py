# Connor Pavicic, Attendee and Ticket Sales management

def management():
    tickets = 0
    profit = 0
    attendees = 0
    one_day = 0
    three_day = 0
    one_day_VIP = 0
    three_day_VIP = 0
    attendee_names = []

    choice = input("""
Options:

1. Add tickets to total tickets
2. Remove tickets from total tickets
3. Check attendees
4. Add a name to attendees and what type of ticket they have
5. Check ticket sales
6. Check ticket profits

Answer (1, 2, 3, 4, 5): """)
    
    if choice == '1':
            typetickets = input("""What type of tickets did you sell?
1. 1-day
2. 3-day
3. 1-day VIP
4. 3-day VIP

Answer (1, 2, 3, 4): """)
            
            if typetickets == '1':
                while True:
                    try:
                        cost = input('How much do one of those tickets cost?: ')
                        num_tickets = input('How many of those tickets did you sell?: ')
                        break
                    except ValueError:
                        print('Type a number.')
                    money = int(cost)*int(num_tickets)
                    print(f'Addition Successful! (You made ${money}).')
            elif typetickets == '2':
                while True:
                    try:
                        cost = input('How much do one of those tickets cost?: ')
                        num_tickets = input('How many of those tickets did you sell?: ')
                        break
                    except ValueError:
                        print('Type a number.')
                    money = int(cost)*int(num_tickets)
                    print(f'Addition Successful! (You made ${money}).')
            elif typetickets == '3':
                while True:
                    try:
                        cost = input('How much do one of those tickets cost?: ')
                        num_tickets = input('How many of those tickets did you sell?: ')
                        break
                    except ValueError:
                        print('Type a number.')
                    money = int(cost)*int(num_tickets)
                    print(f'Addition Successful! (You made ${money}).')


management()