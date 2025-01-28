# Connor Pavicic, Attendee and Ticket Sales management

def management():
    tickets = 0
    profit = 0
    attendees = 0
    one_day = 0
    three_day = 0
    one_day_VIP = 0
    three_day_VIP = 0

    choice = input("""
Options:

1. Add tickets to total tickets
2. Remove tickets from total tickets
3. Check attendees
4. Check ticket sales
5. Check ticket profits

Answer (1, 2, 3, 4, 5): """)
    
    if choice == '1':
            typetickets = input("""What type of tickets did you sell?
1. 1-day
2. 3-day
3. 1-day VIP
4. 3-day VIP

Answer (1, 2, 3, 4): """)
            
            if typetickets == '1':
                cost = input('How much do one of those tickets cost?: ')
                num_tickets = input('How many of those tickets did you sell?: ')
                money = int(cost)*int(num_tickets)
                print(f'Addition Successfull! (You made ${money}).')

management()