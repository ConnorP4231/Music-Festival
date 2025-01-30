def add_venue(schedule: dict, venues: dict, venue_name: str):
    schedule[venue_name] = {}
    venues[venue_name] = {}
    return True

def remove_venue(schedule: dict, venues: dict, venue_name):
    if venue_name in venues:
        del schedule[venue_name]
        del venues[venue_name]
        print("Venue removed successfully")
    else:
        print("Error: Venue does not exist")

def add_stage(schedule: dict, venues: dict, venue_name: str, stage_name: str, location: str):
    if stage_name in schedule.get(venue_name, {}):
        return False
    else:
        schedule[venue_name][stage_name] = []
        venues[venue_name][stage_name] = {"location": location, "equipment": set()}
        return True
        
def remove_stage(schedule: dict, venues: dict, venue_name: str, stage_name: str):
    if stage_name in schedule.get(venue_name, {}):
        del schedule[venue_name][stage_name]
        del venues[venue_name][stage_name]
        return True
    else:
        return False

def assign_artist_schedule(time_slot_list: tuple, schedule: dict, venue_name: str, stage_name: str, time_slot: str, artist_name: str):
    while True:
        if venue_name in schedule and stage_name in schedule[venue_name]:
            if any(slot == time_slot for slot, _ in schedule[venue_name][stage_name]):
                print("Time slot already taken")
            else:
                schedule[venue_name][stage_name].append((time_slot, artist_name))
        else:
            print("Error: Venue or stage does not exist")
        
        choice = input("Do you want to assign another artist? (y/n): ")
        if choice.lower() != 'y':
            break

def remove_time_slot(schedule: dict):
    venue_name = input("Enter venue name: ")
    stage_name = input("Enter stage name: ")
    time_slot = input("Enter time slot to remove: ")
    
    if venue_name in schedule and stage_name in schedule[venue_name]:
        schedule[venue_name][stage_name] = [(t, a) for t, a in schedule[venue_name][stage_name] if t != time_slot]
    else:
        print("Error: Venue or stage does not exist")

def change_artist(schedule: dict):
    venue_name = input("Enter venue name: ")
    stage_name = input("Enter stage name: ")
    time_slot = input("Enter time slot: ")
    artist_name = input("Enter new artist name: ")
    
    if venue_name in schedule and stage_name in schedule[venue_name]:
        schedule[venue_name][stage_name] = [(t, artist_name if t == time_slot else a) for t, a in schedule[venue_name][stage_name]]
    else:
        print("Error: Venue or stage does not exist")

def display_schedule(schedule: dict):
    if not schedule:
        print("Schedule is empty")
    else:
        print("Festival Schedule:")
        for venue, stages in schedule.items():
            print(f"Venue: {venue}")
            for stage, timeslots in stages.items():
                print(f"  Stage: {stage}")
                for time, artist in timeslots:
                    print(f"    {time}: {artist}")

def assign_equipment_to_stage(venues: dict):
    venue_name = input("Enter venue name: ")
    stage_name = input("Enter stage name: ")
    equipment_item = input("Enter equipment item: ")
    
    if venue_name in venues and stage_name in venues[venue_name]:
        venues[venue_name][stage_name]["equipment"].add(equipment_item)
    else:
        print("Error: Venue or stage does not exist")

def display_venues(venues: dict):
    print("Venues:")
    for venue, stages in venues.items():
        print(f"Venue: {venue}")
        print("  Stages and Equipment:")
        for stage, details in stages.items():
            print(f"    Stage: {stage}")
            print(f"      Location: {details['location']}")
            print(f"      Equipment: {', '.join(details['equipment']) if details['equipment'] else 'None'}")

def main():

    schedule = {}
    venues = {}
    time_slot_list = ("10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00")

    while True:

        print("Welcome to Venue management\nPlease select action")
        print(f"1) Create Venue\n2) Remove Venue\n3) Modified specfic venue")

        choice = input("Choose action to perform\n >>")

        match choice:
            case '1':
                venue_name = input("Enter venue name: ")
                add_venue(schedule, venues, venue_name)
            case '2':
                if not venues:
                    print("You don't have any venue yet\nPlease create venue")
                else:
                    venue_name = input("Enter venue name: ")
                    remove_venue(schedule, venues, venue_name)
            case '3':
                if not venues:
                    print("You don't have any venue yet\nPlease create venue")
                else:

                    display_venues()

                    venue = input("Enter venue to modified\n>>> ")

                    if venue in venues.keys():
                        print(f"You are now modifying {venue}")
                        print("Please selection action")
                        print(f"1) Modify stage\n2) Modify Schedule\n")

                        action = input(">>> ")

                        match action:
                            case '1':
                                print("Modify stage")
                                print(f"1) Add Stage\n2) Remove Stage\n3) Change Stage location\n4) Change Stage equipment")
                                act = input(">>> ")
                                match act:
                                    case '1':
                                        while True:
                                            venue_name = input("Enter venue name: ")
                                            stage_name = input("Enter stage name: ")
                                            location = input("Enter location: ")

                                            if not add_stage(venue_name, stage_name, location):
                                                print("Stage already exists")
                                            else:
                                                print(f"You successfully add {stage_name} into {venue_name} at location {location}!")

                                            choice = input("Do you want to add another stage? (y/n): ")
                                            if choice.lower() != 'y':
                                                break

                                    case '2':
                                        while True:
                                            venue_name = input("Enter venue name: ")
                                            stage_name = input("Enter stage name: ")

                                            if not remove_stage(schedule, venues, venue_name, stage_name):
                                                print("Stage doesn't exists")
                                            else:
                                                print(f"You successfully remove {stage_name} from {venue_name}!")

                                            choice = input("Do you want to add another stage? (y/n): ")
                                            if choice.lower() != 'y':
                                                break
                                    case '3':
                                        #change stage location
                                        pass
                                    case '4':
                                        #change stage equipment
                                        pass
                            case '2':
                                #Modify Schedule
                                print("Modify Schedule")
                                print(f"1) Display schedule\n2) Remove Stage\n3) Change Stage location\n4) Change Stage equipment")

                                act = input(">>> ")

                                match act:
                                    case '1':
                                        display_schedule(schedule)
                                    case '2':
                                        
                                        venue_name = input("Enter venue name: ")
                                        stage_name = input("Enter stage name: ")

                                        for time in time_slot_list:
                                            print(f"| {time}", end="")
                                        time_slot = input("Enter time slot: ")

                                        artist_name = input("Enter artist name: ")

                                        if not assign_artist_schedule(time_slot_list, schedule, venue_name, stage_name, time_slot, artist_name):
                                            pass
                    else:
                        pass