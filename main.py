# Connor Pavicic, Attendee and Ticket Sales management

tickets = 0
profit = 0
attendees = 0
one_day = 0
three_day = 0
one_day_VIP = 0
three_day_VIP = 0
attendee_names = []

def management(tickets = tickets, profit = profit, attendees = attendees, one_day = one_day, three_day = three_day, one_day_VIP = one_day_VIP, three_day_VIP = three_day_VIP, attendee_names = attendee_names):
    end_function = False
    while end_function == False:
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
            break_loop = False
            while break_loop == False:
                typetickets = input("""What type of tickets did you sell?
1. 1-day
2. 3-day
3. 1-day VIP
4. 3-day VIP

Answer (1, 2, 3, 4): """)
                
                if typetickets == '1':
                    cost = None
                    while cost == None:
                        try:
                            cost = int(input('How much do one of those tickets cost?: '))
                        except ValueError:
                            print('Type a number.')
                    num_tickets = None
                    while num_tickets == None:
                        try:
                            num_tickets = int(input('How many of those tickets did you sell?: '))
                        except:
                            print('Type a number.')
                        
                    money = cost*num_tickets
                    one_day += num_tickets
                    profit += money
                    print(f'Addition Successful! (You made ${money}).')
                    break_loop = True
                    end_function = True
                    break
                elif typetickets == '2':
                    cost = None
                    while cost == None:
                        try:
                            cost = int(input('How much do one of those tickets cost?: '))
                        except ValueError:
                            print('Type a number.')
                    num_tickets = None
                    while num_tickets == None:
                        try:
                            num_tickets = int(input('How many of those tickets did you sell?: '))
                        except:
                            print('Type a number.')
                        
                    money = cost*num_tickets
                    three_day += num_tickets
                    profit += money
                    print(f'Addition Successful! (You made ${money}).')
                    break_loop = True
                    end_function = True
                    break
                elif typetickets == '3':
                    cost = None
                    while cost == None:
                        try:
                            cost = int(input('How much do one of those tickets cost?: '))
                        except ValueError:
                            print('Type a number.')
                    num_tickets = None
                    while num_tickets == None:
                        try:
                            num_tickets = int(input('How many of those tickets did you sell?: '))
                        except:
                            print('Type a number.')
                        
                    money = cost*num_tickets
                    one_day_VIP += num_tickets
                    profit += money
                    print(f'Addition Successful! (You made ${money}).')
                    break_loop = True
                    end_function = True
                    break
                elif typetickets == '4':
                    cost = None
                    while cost == None:
                        try:
                            cost = int(input('How much do one of those tickets cost?: '))
                        except ValueError:
                            print('Type a number.')
                    num_tickets = None
                    while num_tickets == None:
                        try:
                            num_tickets = int(input('How many of those tickets did you sell?: '))
                        except:
                            print('Type a number.')
                        
                    money = cost*num_tickets
                    three_day_VIP += num_tickets
                    profit += money
                    end_function = True
                    break_loop = True
                    break
                else:
                    print('You need to type an option displayed to you.')
                    pass
        
        elif choice == '2': #Stupid proof to make sure they can't subtract tickets from 0 total tickets and fix it to subtract not add
            break_loop = False
            while break_loop == False:
                typetickets = input("""What type of tickets did you want to subtract?
1. 1-day
2. 3-day
3. 1-day VIP
4. 3-day VIP

Answer (1, 2, 3, 4): """)
                
                if typetickets == '1':
                    cost = None
                    while cost == None:
                        try:
                            cost = int(input('How much do one of those tickets cost?: '))
                        except ValueError:
                            print('Type a number.')
                    num_tickets = None
                    while num_tickets == None:
                        try:
                            num_tickets = int(input('How many of those tickets did you want to subtract?: '))
                        except:
                            print('Type a number.')
                        
                    money = cost*num_tickets
                    one_day -= num_tickets
                    profit += money
                    print(f'Addition Successful! (You made ${money}).')
                    break_loop = True
                    end_function = True
                    break
                elif typetickets == '2':
                    cost = None
                    while cost == None:
                        try:
                            cost = int(input('How much do one of those tickets cost?: '))
                        except ValueError:
                            print('Type a number.')
                    num_tickets = None
                    while num_tickets == None:
                        try:
                            num_tickets = int(input('How many of those tickets did you sell?: '))
                        except:
                            print('Type a number.')
                        
                    money = cost*num_tickets
                    three_day += num_tickets
                    profit += money
                    print(f'Addition Successful! (You made ${money}).')
                    break_loop = True
                    end_function = True
                    break
                elif typetickets == '3':
                    cost = None
                    while cost == None:
                        try:
                            cost = int(input('How much do one of those tickets cost?: '))
                        except ValueError:
                            print('Type a number.')
                    num_tickets = None
                    while num_tickets == None:
                        try:
                            num_tickets = int(input('How many of those tickets did you sell?: '))
                        except:
                            print('Type a number.')
                        
                    money = cost*num_tickets
                    one_day_VIP += num_tickets
                    profit += money
                    print(f'Addition Successful! (You made ${money}).')
                    break_loop = True
                    end_function = True
                    break
                elif typetickets == '4':
                    cost = None
                    while cost == None:
                        try:
                            cost = int(input('How much do one of those tickets cost?: '))
                        except ValueError:
                            print('Type a number.')
                    num_tickets = None
                    while num_tickets == None:
                        try:
                            num_tickets = int(input('How many of those tickets did you sell?: '))
                        except:
                            print('Type a number.')
                        
                    money = cost*num_tickets
                    three_day_VIP += num_tickets
                    profit += money
                    end_function = True
                    break_loop = True
                    break
                else:
                    print('You need to type an option displayed to you.')
                    pass
                    

management()