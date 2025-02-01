

def add_venue(schedule: dict, venues: dict, venue_name: str):
    schedule[venue_name] = {}
    venues[venue_name] = {}
    print(f"\nSuccessfully add {venue_name} to venues")
    return True

def remove_venue(schedule: dict, venues: dict, venue_name):
    if venue_name in venues:
        del schedule[venue_name]
        del venues[venue_name]
        print("\nVenue removed successfully")
    else:
        print("\nError: Venue does not exist")

def add_stage(schedule: dict, venues: dict, venue_name: str, stage_name: str, location: str):
    if venue_name in venues:
        if stage_name in venues[venue_name]:
            print("\nError: Stage already exist")
            return False
        else:
            schedule[venue_name][stage_name] = []
            venues[venue_name][stage_name] = {"location": location, "equipment": set()}
            print(f"\nSuccessfully add {stage_name} to {venue_name}")
            return True
    else:
        print("\nError: Venue does not exist")
        return False
        
def remove_stage(schedule: dict, venues: dict, venue_name: str, stage_name: str):
    if venue_name in venues and stage_name in venues[venue_name]:
        del schedule[venue_name][stage_name]
        del venues[venue_name][stage_name]
        print(f"\nSuccesfully remove {stage_name} from {venue_name}")
        return True
    else:
        print("\nError: Venue or stage does not exist")
        return False
    
def change_location(venues: dict, venue_name: str, stage_name: str, location: str):
    if venue_name in venues and stage_name in venues[venue_name]:
        venues[venue_name][stage_name]["location"] = location
        print(f"\nSuccesfully change location to {location}")
        return True
    else:
        print("\nError: Venue or stage does not exist")
        return False

def change_equipment(venues: dict, venue_name: str, stage_name: str, equipment_items: set):
    if venue_name in venues and stage_name in venues[venue_name]:
        venues[venue_name][stage_name]["equipment"] = equipment_items
        print(f"\nSuccesfully set equipment to {equipment_items}")
        return True
    else:
        print("\nError: Venue or stage does not exist")
        return False

def assign_artist_schedule(time_slot_list: tuple, schedule: dict, venue_name: str, stage_name: str, time_slot: str, artist_name: str):
    if time_slot not in time_slot_list:
        print("\nPlease select appropiate time slot provided")
        return False
    
    if venue_name in schedule and stage_name in schedule[venue_name]:
        for (time, artist) in schedule[venue_name][stage_name]:
            if time_slot == time:
                print("\nTime slot already taken")
                return False
            else:
                schedule[venue_name][stage_name].append((time_slot, artist_name))
                print(f"\nSuccessfully add artiist {artist_name} in time {time_slot}")
                return True
    else:
        print("\nError: Venue or stage does not exist")
        return False
    
def remove_time_slot(schedule: dict, venue_name: str, stage_name:str, time_slot: str):
    for time, artist in schedule[venue_name][stage_name]: 
        if time != time_slot:
            print("You didn't assign artist in this time slot!")
    if venue_name in schedule and stage_name in schedule[venue_name]:
        schedule[venue_name][stage_name] = [(time, artist) for time, artist in schedule[venue_name][stage_name] if time != time_slot]
        print(f"\nSuccessfully remove time slot {time_slot} from {stage_name} in {venue_name}")
        return True
    else:
        print("\nError: Venue or stage does not exist")
        return False

def change_artist(schedule: dict, venue_name: str, stage_name: str, time_slot: str, artist_name: str):
    for time, artist in schedule[venue_name][stage_name]: 
        if time != time_slot:
            print("You didn't assign artist in this time slot!")
    if venue_name in schedule and stage_name in schedule[venue_name]:
        schedule[venue_name][stage_name] = [(time, artist) for time, artist in schedule[venue_name][stage_name] if time != time_slot]
        schedule[venue_name][stage_name].append((time_slot, artist_name))
        print(f"\nSuccesfully change artist in slot {time_slot}")
        return True
    else:
        print("\nError: Venue or stage does not exist")
        return False

def display_schedule(time_slot_list: tuple, schedule: dict):
    print("")
    if not schedule:
        print("Schedule is empty")
    else:
        print("Music Festival Schedule:")
        for venue in schedule.keys():
            print(f"Venue | {venue}:")
            for stage in schedule[venue].keys():
                print(f"   Stage | {stage}:")
                for slot in time_slot_list:
                    print(f"      {slot} : ", end="")
                    for (time, artist) in schedule[venue][stage]:
                        if time == slot:
                            print(f"{artist}")
                        else:
                            print("NONE")
                    print("")

def display_stage_schedule(time_slot_list: tuple, schedule: dict, venue: str):
    print("")
    if not schedule:
        print("Schedule is empty")
    else:
        for stage in schedule[venue].keys():
            print(f"   Stage | {stage}:")
            for slot in time_slot_list:
                print(f"      {slot} : ", end="")
                for (time, artist) in schedule[venue][stage]:
                    if time == slot:
                        print(f"{artist}")
                    else:
                        print("NONE")
                print("")

def display_stage(venues: dict, venue: str):
    print("")
    for stage in venues[venue].keys():
        print(f"Stage | {stage}:")
        print(f"   Location: {venues[venue][stage]['location']}")
        print(f"   Equipment: {', '.join(venues[venue][stage]['equipment']) if venues[venue][stage]['equipment'] else 'None'}")

def display_venues(venues: dict):
    print("")
    for venue in venues.keys():
        print(f"Venue | {venue}:")
        for stage in venues[venue].keys():
            print(f"   Stage | {stage}:")
            print(f"      Location: {venues[venue][stage]['location']}")
            print(f"      Equipment: {', '.join(venues[venue][stage]['equipment']) if venues[venue][stage]['equipment'] else 'None'}")

def show_venues(venues: dict):
    print("")
    if not venues:
        print("You don't have any venue yet")
        return False
    else:
        for venue in venues.keys():
            print(f"{venue}")
        return True

def main():

    schedule = {}
    venues = {}
    time_slot_list = ("10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00")

    print("Welcome to Venue management\nPlease select action")
    while True:
        print(f"\n1) Create Venue\n2) Remove Venue\n3) Modified specfic venue\n4) Display venues\n5) Display schedule \n6) Exit")

        choice = input("Choose action to perform\n>>> ")

        match choice:
            case '1':
                # Add venue
                venue_name = input("Enter venue name: ")
                add_venue(schedule, venues, venue_name)
            case '2':
                # Remove venue
                if not venues:
                    print("\nYou don't have any venue yet\nPlease create venue")
                else:
                    venue_name = input("Enter venue name: ")
                    remove_venue(schedule, venues, venue_name)

            case '4':
                # Show venue
                show_venues(venues)

            case '5':
                #Display schedule
                display_schedule(time_slot_list, schedule)

            case '6':
                # Exit
                break

            case '3':
                #Modify specific venue
                while True:
                    if not venues:
                        print("\nYou don't have any venue yet\nPlease create venue")
                        break
                    else:

                        show_venues(venues)

                        venue = input("\nEnter venue to modified\n>>> ")

                        if venue in venues:
                            while True:

                                print(f"\nYou are now modifying {venue}")
                                print("Please selection action")
                                print(f"1) Modify stage\n2) Modify Schedule\n3) Go Back")

                                action = input(">>> ")

                                match action:
                                    case '1':
                                        while True:
                                            print("\nModify stage")
                                            print(f"1) Add Stage\n2) Remove Stage\n3) Change Stage location\n4) Change Stage equipment\n5) display venue + stage\n6) Go Back")
                                            act = input(">>> ")
                                            match act:
                                                case '1':
                                                    stage_name = input("Enter stage name: ")
                                                    location = input("Enter location: ")

                                                    add_stage(schedule, venues, venue, stage_name, location)

                                                case '2':
                                                    display_stage(venues, venue)
                                                    stage_name = input("Enter stage name: ")
                                                    remove_stage(schedule, venues, venue, stage_name)

                                                case '3':
                                                    #change stage location
                                                    display_stage(venues, venue)
                                                    stage_name = input("Enter stage name: ")
                                                    location = input("Enter location: ")
                                                    change_location(venues, venue, stage_name, location)

                                                case '4':
                                                    #change stage equipment
                                                    display_stage(venues, venue)
                                                    stage_name = input("Enter stage name: ")
                                                    equipment_item = input("Enter equipment item: ")
                                                    equipment_items = equipment_item.split()
                                                    change_equipment(venues, venue, stage_name, equipment_items)

                                                case '5':
                                                    #display venues
                                                    display_venues(venues)

                                                case '6':
                                                    break

                                                case _:
                                                    print("Invalid Choice") 

                                    case '2':
                                        #Modify Schedule
                                        while True:
                                            print("\nModify Schedule")
                                            print(f"1) Display schedule\n2) Assign Artist\n3) Remove time slot\n4) Change Artist\n5) Go Back")

                                            act = input(">>> ")

                                            match act:
                                                case '1':
                                                    display_schedule(time_slot_list, schedule)

                                                case '2':
                                                    #Assign Artist
                                                    display_stage_schedule(time_slot_list, schedule, venue)
                                                    stage_name = input("Enter stage name: ")
                                                    for time in time_slot_list:
                                                        print(f"| {time} ", end="")
                                                    time_slot = input("\nEnter time slot: ")
                                                    artist_name = input("Enter artist name: ")

                                                    assign_artist_schedule(time_slot_list, schedule, venue, stage_name, time_slot, artist_name)

                                                case '3':
                                                    #Remove Time Slot
                                                    display_stage_schedule(time_slot_list, schedule, venue)
                                                    stage_name = input("Enter stage name: ")
                                                    time_slot = input("Enter time slot to remove: ")

                                                    remove_time_slot(schedule, venue, stage_name, time_slot)
                                                    
                                                case '4':
                                                    #Change Artist
                                                    display_stage_schedule(time_slot_list, schedule, venue)
                                                    stage_name = input("Enter stage name: ")
                                                    time_slot = input("Enter time slot: ")
                                                    artist_name = input("Enter new artist name: ")      

                                                    change_artist(schedule, venue, stage_name, time_slot, artist_name)                

                                                case '5':
                                                    break   
                                                case _:
                                                    print("Invalid Choice") 

                                    case '3':
                                        break   
                                    case _:
                                        print("Invalid Choice")
                                        continue    
                        else:
                            print("\nVenue doesn't exist")
                            break
            case _:
                print("\nInvalid Choice")
                continue

if __name__ == "__main__":
    main()

class Artist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def __str__(self):
        return f"Artist Name: {self.name}, Genre: {self.genre}"

class ArtistManager:
    def __init__(self):
        self.artists = []

    #function to add artists
    def add_artist(self):
        name = input("Enter artist's name: ")
        genre = input("Enter artist's genre: ")
        self.artists.append(Artist(name, genre))
        print(f"Artist {name} added successfully!")

    #function to remove artists
    def remove_artist(self):
        name = input("Enter the artist's name to remove: ")
        for artist in self.artists:
            if artist.name.lower() == name.lower():
                self.artists.remove(artist)
                print(f"Artist {name} removed successfully!")
                return
        print(f"No artist found with the name {name}.")

#function to edit the artists
    def edit_artist(self):
        name = input("Enter the artist's name to edit: ")
        for artist in self.artists:
            if artist.name.lower() == name.lower():
                new_name = input(f"Enter new name for {name} (leave empty to keep current): ")
                new_genre = input(f"Enter new genre for {name} (leave empty to keep current): ")
                if new_name:
                    artist.name = new_name
                if new_genre:
                    artist.genre = new_genre
                print(f"Artist {name} updated successfully!")
                return
        print(f"No artist found with the name {name}.")

    #function to view artists
    def view_artists(self):
        if not self.artists:
            print("No artists to display.")
        else:
            print("Artists in the system:")
            for artist in self.artists:
                print(artist)

#main function to run the code
def main():
    manager = ArtistManager()

    while True:
        print("\nArtist Management System")
        print("1. Add Artist")
        print("2. Remove Artist")
        print("3. Edit Artist")
        print("4. View Artists")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_artist()
        elif choice == "2":
            manager.remove_artist()
        elif choice == "3":
            manager.edit_artist()
        elif choice == "4":
            manager.view_artists()
        elif choice == "5":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

profit = 0 #All the variables
attendees = 0
one_day = 0
three_day = 0
one_day_VIP = 0
three_day_VIP = 0
attendee_names = []

def management(profit = profit, attendees = attendees, one_day = one_day, three_day = three_day, one_day_VIP = one_day_VIP, three_day_VIP = three_day_VIP, attendee_names = attendee_names):
    while True:
        # The users first inital choice
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

        if choice == '1':  # Adds tickets
            while True:
                try: # Idiot proof number 1
                    typetickets = int(input("What type of tickets? (1: 1-day, 2: 3-day, 3: 1-day VIP, 4: 3-day VIP): "))
                    if typetickets not in [1, 2, 3, 4]:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter 1, 2, 3, or 4.")

            while True:
                try: #Idiot proof number 2
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

            print(f'Addition Successful! (You made ${cost * num_tickets}).') #Prints the the addition was good and prints the money made.

        elif choice == '2':  # Removing (refunding) tickets
            while True:
                try: #Idiot proof number 3
                    typetickets = int(input("What type of tickets to refund? (1: 1-day, 2: 3-day, 3: 1-day VIP, 4: 3-day VIP): "))
                    if typetickets not in [1, 2, 3, 4]:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter 1, 2, 3, or 4.")

            while True:
                try: #Idiot proof number 4
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

            # Subtracts the tickets
            if typetickets == 1:
                one_day -= num_tickets_remove
            elif typetickets == 2:
                three_day -= num_tickets_remove
            elif typetickets == 3:
                one_day_VIP -= num_tickets_remove
            elif typetickets == 4:
                three_day_VIP -= num_tickets_remove

            profit -= refund_amount
            print("Refund Successful!") #Prints that the refund was successful.

        elif choice == '3':  # Check attendees
            print(f"Total attendees: {attendees}")
            if attendee_names:
                print("Attendee List:", ', '.join(attendee_names))
            else:
                print("No attendees yet.") #makes sure the attendees are in the list.

        elif choice == '4':  # Add attendee
            name = input("Enter attendee name: ").strip()
            if not name:
                print("Name cannot be empty.") #makes sure the name isn't nothing.
                continue

            while True:
                try: #Idiot proof
                    ticket_type = int(input("Ticket Type (1: 1-day, 2: 3-day, 3: 1-day VIP, 4: 3-day VIP): ")) #Pairs the attendees ticket with their name
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
            return profit, attendees, one_day, three_day, one_day_VIP, three_day_VIP, attendee_names

        else: # Idiot proof
            print("Invalid option. Please enter a number between 1 and 7.")


profit, attendees, one_day, three_day, one_day_VIP, three_day_VIP, attendee_names = management(profit, attendees, one_day, three_day, one_day_VIP, three_day_VIP, attendee_names)

#Alec George music festival search function

#will have a search function for setup and a search function for actually searching

#function to search
def search(category, category_name, word):
    output = f"\nitems in {category_name} category with {word} in them:"
    for i in category:
        if word.strip().lower() in i.lower():
            output += f"\n{i}"

    return output


#function to gather information for searching
def search_setup(venues, attendee_list):

    #clear the screen
    print("\033c",end="")
    #stupid proof while loop and try/except
    while True:
        try:
            #user input for category they are searching in, being artists, songs, song genres, song times, and attendees
            search_category = int(input("""\nwhat category would you like to search in? Type:
  1 to search venues
  2 to search for attendees
  3 to search all
  (other things will be added once I know how to add them)
  Your input here (number from one to three): """))
            #possible inputs list for small bug solve
            possible_inputs = [1,2,3]
            #conditional to only let the user input valid inputs
            if search_category in possible_inputs:
                break #only exits loop when a value that works is inputted
            
        except ValueError:
            print("\ninvalid input")


    #user input for word or phrase to search for
    searched_word = input("\nwhat would you like to search for? (type a word, phrase, letter, or number, will display everything with that in it) ")

    #actually search
    output = ""
    if search_category == 1:
#        output += search(artist_list, "artists", searched_word)
#    elif search_category == 2:
#        output += search(artist_list, "songs", searched_word)
#    elif search_category == 3:
#        output += search(artist_list, "genres", searched_word)
#    elif search_category == 4:
        output += search(venues, "venues", searched_word)
    elif search_category == 2:
        output += search(attendee_list, "attendees", searched_word)
    elif search_category == 3:
#        output += search(artist_list, "artists", searched_word)
#        output += f"\n{search(artist_list, "songs", searched_word)}"
#        output += f"\n{search(artist_list, "genres", searched_word)}"
        output += f"\n{search(venues, "venues", searched_word)}"
        output += f"\n{search(attendee_list, "attendees", searched_word)}"
    else:
        output += "\ninvalid input"

    return output

#temporary stuff for testing
venues = {"place AA", "place BB", "place CC", "food", "pqfjaifhoalkjfhkjalfh"}
attendee_names = ["person AA", "person BB", "person CC", "banana", "afoiphvoiafn"]
while True:
    #when run:
    print(search_setup(venues, attendee_names))
    input()

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