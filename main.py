#Alec George music festival search function

#will have a search function for setup and a search function for actually searching

#function to search
def search(category, category_name, word):
    output = f"\nitems in {category_name} category with {word} in them:"
    for i in category:
        if word in i:
            output += f"\n{i}"

    return output


#function to gather information for searching
def search_setup(artist_list, schedule, attendee_list):

    #stupid proof while loop and try/except
    while True:
        try:
            #user input for category they are searching in, being artists, songs, song genres, song times, and attendees
            search_category = int(input("""\nwhat category would you like to search in? Type:
  1 to search artists
  2 to search songs
  3 to search song genres
  4 to search for a time
  5 to search for attendees
  6 to search all
  Your input here: """))
            break #only exits loop when a value that works is inputted
        except ValueError:
            print("\ninvalid input")

    #user input for word or phrase to search for
    searched_word = input("\nwhat would you like to search for? (word, phrase, or number) ")

    #actually search
    output = ""
    if search_category == 1:
        output += search(artist_list, "artists", searched_word)
    elif search_category == 2:
        search(artist_list, "songs", searched_word)
    elif search_category == 3:
        search(artist_list, "genres", searched_word)
    elif search_category == 4:
        search(schedule, "schedule", searched_word)
    elif search_category == 5:
        search(attendee_list, "attendees", searched_word)
    elif search_category == 6:
        search(artist_list, "artists", searched_word)
