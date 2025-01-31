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

