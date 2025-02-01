#main function, when finished and all functions are on the main branch, functions will be placed where they're supposed to be
def main():
    #section for variables


    while True:
        #user input for their choice of what to do with exception handling
        while True:
            try:
                user_input = int(input("""\nWhat would you like to do? type:
 1 to search for things
 2 to manage ticket sales and attendees
 3 to manage artists
 4 to manage the schedule
 5 to manage venues
 6 to exit the program
Your input here: """))
                if user_input >= 1 and user_input <= 6:
                    break
                else:
                    print("\ninvalid input")

            except ValueError:
                print("\ninvalid input")

        #conditional statement to run all other functions, functions will be called in their respective place, will replace the word "pass"
        if user_input == 1:
            #run search function (Alec)
            pass

        elif user_input == 2:
            #run ticket sales/attendee management (Connor)
            pass
            
        elif user_input == 3:
            #run artist management function (Farius)
            pass

        elif user_input == 4:
            #run schedule management (John)
            pass

        elif user_input == 5:
            #run venue management (John)
            pass

        else:
            #exit while loop
            break

    print("\nthank you for using this program")



main()