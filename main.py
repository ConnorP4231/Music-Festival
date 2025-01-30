schedule = {}
venues = {}

def add_venue():
    venue_name = input("Enter venue name: ")
    schedule[venue_name] = {}
    venues[venue_name] = {}

def remove_venue(venue_name):
    if venue_name in venues:
        del schedule[venue_name]
        del venues[venue_name]
        print("Venue removed successfully")
    else:
        print("Error: Venue does not exist")

def add_stage():
    while True:
        venue_name = input("Enter venue name: ")
        stage_name = input("Enter stage name: ")
        location = input("Enter location: ")
        
        if stage_name in schedule.get(venue_name, {}):
            print("Stage already exists")
        else:
            schedule[venue_name][stage_name] = []
            venues[venue_name][stage_name] = {"location": location, "equipment": set()}
        
        choice = input("Do you want to add another stage? (y/n): ")
        if choice.lower() != 'y':
            break

def remove_stage():
    venue_name = input("Enter venue name: ")
    stage_name = input("Enter stage name: ")
    
    if stage_name in schedule.get(venue_name, {}):
        del schedule[venue_name][stage_name]
        del venues[venue_name][stage_name]
    else:
        print("Error: Stage does not exist")

def assign_artist_schedule():
    while True:
        venue_name = input("Enter venue name: ")
        stage_name = input("Enter stage name: ")
        time_slot = input("Enter time slot: ")
        artist_name = input("Enter artist name: ")
        
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

def remove_time_slot():
    venue_name = input("Enter venue name: ")
    stage_name = input("Enter stage name: ")
    time_slot = input("Enter time slot to remove: ")
    
    if venue_name in schedule and stage_name in schedule[venue_name]:
        schedule[venue_name][stage_name] = [(t, a) for t, a in schedule[venue_name][stage_name] if t != time_slot]
    else:
        print("Error: Venue or stage does not exist")

def change_artist():
    venue_name = input("Enter venue name: ")
    stage_name = input("Enter stage name: ")
    time_slot = input("Enter time slot: ")
    artist_name = input("Enter new artist name: ")
    
    if venue_name in schedule and stage_name in schedule[venue_name]:
        schedule[venue_name][stage_name] = [(t, artist_name if t == time_slot else a) for t, a in schedule[venue_name][stage_name]]
    else:
        print("Error: Venue or stage does not exist")

def display_schedule():
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

def assign_equipment_to_stage():
    venue_name = input("Enter venue name: ")
    stage_name = input("Enter stage name: ")
    equipment_item = input("Enter equipment item: ")
    
    if venue_name in venues and stage_name in venues[venue_name]:
        venues[venue_name][stage_name]["equipment"].add(equipment_item)
    else:
        print("Error: Venue or stage does not exist")

def display_venues():
    print("Venues:")
    for venue, stages in venues.items():
        print(f"Venue: {venue}")
        print("  Stages and Equipment:")
        for stage, details in stages.items():
            print(f"    Stage: {stage}")
            print(f"      Location: {details['location']}")
            print(f"      Equipment: {', '.join(details['equipment']) if details['equipment'] else 'None'}")
