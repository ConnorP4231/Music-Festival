#Fairus Aritst managment


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
