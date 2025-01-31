def add_venue(schedule: dict, venues: dict, venue_name: str):
    schedule[venue_name] = {}
    venues[venue_name] = {}
    print(f"Successfully add {venue_name} to venues")
    return True

def remove_venue(schedule: dict, venues: dict, venue_name):
    if venue_name in venues:
        del schedule[venue_name]
        del venues[venue_name]
        print("Venue removed successfully")
    else:
        print("Error: Venue does not exist")

def add_stage(schedule: dict, venues: dict, venue_name: str, stage_name: str, location: str):
    if venue_name in venues:
        if stage_name in venues[venue_name]:
            print("Error: Stage already exist")
            return False
        else:
            schedule[venue_name][stage_name] = []
            venues[venue_name][stage_name] = {"location": location, "equipment": set()}
            print(f"Successfully add {stage_name} to {venue_name}")
            return True
    else:
        print("Error: Venue does not exist")
        return False
        
def remove_stage(schedule: dict, venues: dict, venue_name: str, stage_name: str):
    if venue_name in venues and stage_name in venues[venue_name]:
        del schedule[venue_name][stage_name]
        del venues[venue_name][stage_name]
        print(f"Succesfully remove {stage_name} from {venue_name}")
        return True
    else:
        print("Error: Venue or stage does not exist")
        return False
    
def change_location(venues: dict, venue_name: str, stage_name: str, location: str):
    if venue_name in venues and stage_name in venues[venue_name]:
        venues[venue_name][stage_name]["location"] = location
        print(f"Succesfully change location to {location}")
        return True
    else:
        print("Error: Venue or stage does not exist")
        return False

def change_equipment(venues: dict, venue_name: str, stage_name: str, equipment_items: set):
    if venue_name in venues and stage_name in venues[venue_name]:
        venues[venue_name][stage_name]["equipment"] = equipment_items
        print(f"Succesfully set equipment to {equipment_items}")
        return True
    else:
        print("Error: Venue or stage does not exist")
        return False

def assign_artist_schedule(time_slot_list: tuple, schedule: dict, venue_name: str, stage_name: str, time_slot: str, artist_name: str):
    if time_slot not in time_slot_list:
        print("Please select appropiate time slot provided")
        return False
    
    if venue_name in schedule and stage_name in schedule[venue_name]:
        for (time, artist) in schedule[venue_name][stage_name]:
            if time_slot == time:
                print("Time slot already taken")
                return False
            else:
                schedule[venue_name][stage_name].append((time_slot, artist_name))
                return True
    else:
        print("Error: Venue or stage does not exist")
        return False
    
def remove_time_slot(schedule: dict, venue_name: str, stage_name:str, time_slot: str):
    for time, artist in schedule[venue_name][stage_name]: 
        if time != time_slot:
            print("You didn't assign artist in this time slot!")
    if venue_name in schedule and stage_name in schedule[venue_name]:
        schedule[venue_name][stage_name] = [(time, artist) for time, artist in schedule[venue_name][stage_name] if time != time_slot]
        print(f"Successfully remove time slot {time_slot} from {stage_name} in {venue_name}")
        return True
    else:
        print("Error: Venue or stage does not exist")
        return False

def change_artist(schedule: dict, venue_name: str, stage_name: str, time_slot: str, artist_name: str):
    for time, artist in schedule[venue_name][stage_name]: 
        if time != time_slot:
            print("You didn't assign artist in this time slot!")
    if venue_name in schedule and stage_name in schedule[venue_name]:
        schedule[venue_name][stage_name] = [(time, artist) for time, artist in schedule[venue_name][stage_name] if time != time_slot]
        schedule[venue_name][stage_name].append((time_slot, artist_name))
        print(f"Succesfully change artist in slot {time_slot}")
        return True
    else:
        print("Error: Venue or stage does not exist")
        return False

def display_schedule(time_slot_list: tuple, schedule: dict):
    if not schedule:
        print("Schedule is empty")
    else:
        print("Music Festival Schedule:")
        for venue in schedule.keys():
            print(f"Venue | {venue}:")
            for stage in schedule[venue].keys():
                print(f"   Stage | {stage}:")
                for slot in time_slot_list:
                    print(f"{slot} : ", end="")
                    for (time, artist) in schedule[venue][stage]:
                        if time == slot:
                            print(f"{artist}")
                        else:
                            print("NONE")

def display_venues(venues: dict):
    for venue in venues.keys():
        print(f"Venue | {venue}:")
        for stage in venues[venue].keys():
            print(f"   Stage | {stage}:")
            print(f"      Location: {venues[venue][stage]['location']}")
            print(f"      Equipment: {', '.join(venues[venue][stage]['equipment']) if venues[venue][stage]['equipment'] else 'None'}")

def main():

    schedule = {}
    venues = {}
    time_slot_list = ("10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00")

    print("Welcome to Venue management\nPlease select action")
    while True:
        print(f"1) Create Venue\n2) Remove Venue\n3) Modified specfic venue\n4) Exit")

        choice = input("Choose action to perform\n>>> ")

        match choice:
            case '1':
                venue_name = input("Enter venue name: ")
                add_venue(schedule, venues, venue_name)
            case '2':
                if not venues:
                    print("You don't have any venue yet\nPlease create venue")
                else:
                    venue_name = input("Enter venue name: ")
                    if not remove_venue(schedule, venues, venue_name):
                        print("Venue removed successfully")

            case '4':
                break

            case '3':
                while True:
                    if not venues:
                        print("You don't have any venue yet\nPlease create venue")
                        break
                    else:

                        display_venues(venues)

                        venue = input("Enter venue to modified\n>>> ")

                        if venue in venues:
                            while True:

                                print(f"You are now modifying {venue}")
                                print("Please selection action")
                                print(f"1) Modify stage\n2) Modify Schedule\n3) Go Back")

                                action = input(">>> ")

                                match action:
                                    case '1':
                                        while True:
                                            print("Modify stage")
                                            print(f"1) Add Stage\n2) Remove Stage\n3) Change Stage location\n4) Change Stage equipment\n5) Go Back")
                                            act = input(">>> ")
                                            match act:
                                                case '1':
                                                    stage_name = input("Enter stage name: ")
                                                    location = input("Enter location: ")

                                                    add_stage(schedule, venues, venue, stage_name, location)

                                                case '2':
                                                    stage_name = input("Enter stage name: ")
                                                    remove_stage(schedule, venues, venue, stage_name)

                                                case '3':
                                                    #change stage location
                                                    stage_name = input("Enter stage name: ")
                                                    location = input("Enter location: ")
                                                    change_location(venues, venue, stage_name, location)

                                                case '4':
                                                    #change stage equipment
                                                    venue_name = input("Enter venue name: ")
                                                    stage_name = input("Enter stage name: ")
                                                    equipment_item = input("Enter equipment item: ")
                                                    equipment_items = equipment_item.split()
                                                    change_equipment(venues, venue, stage_name, equipment_items)
                                                case '5':
                                                    break

                                    case '2':
                                        #Modify Schedule
                                        while True:
                                            print("Modify Schedule")
                                            print(f"1) Display schedule\n2) Assign Artist\n3) Remove time slot\n4) Change Artist\n5) Go Back")

                                            act = input(">>> ")

                                            match act:
                                                case '1':
                                                    display_schedule(schedule)

                                                case '2':
                                                    #Assign Artist
                                                    stage_name = input("Enter stage name: ")
                                                    for time in time_slot_list:
                                                        print(f"| {time}", end="")
                                                    time_slot = input("Enter time slot: ")
                                                    artist_name = input("Enter artist name: ")

                                                    assign_artist_schedule(time_slot_list, schedule, venue, stage_name, time_slot, artist_name)

                                                case '3':
                                                    #Remove Time Slot
                                                    venue_name = input("Enter venue name: ")
                                                    stage_name = input("Enter stage name: ")
                                                    time_slot = input("Enter time slot to remove: ")

                                                    remove_time_slot(schedule, venue_name, stage_name, time_slot)
                                                    
                                                case '4':
                                                    #Change Artist
                                                    stage_name = input("Enter stage name: ")
                                                    time_slot = input("Enter time slot: ")
                                                    artist_name = input("Enter new artist name: ")      

                                                    change_artist(schedule, venue, stage_name, time_slot, artist_name)                

                                                case '5':
                                                    break    

                                    case '3':
                                        break       
                        else:
                            print("Venue doesn't exist")
                            break

if __name__ == "__main__":
    main()