# Finish the class definitions below
# Delete "pass" after you implement the class

import os
import pickle

class Library:
    checked_in = []
    checked_out = []
    
    def add_item(self, item):
        if isinstance(item, Movie):
            self.checked_in.append(item)
        elif isinstance(item, Book):
            self.checked_in.append(item)
        elif isinstance(item, Album):
            self.checked_in.append(item)
        else:
            print("Invalid item type")

    def check_out_item(self, item_name):
        for item in self.checked_in:
            if item.name == item_name:
                self.checked_out.append(item)
                self.checked_in.remove(item)
                print(f"Checked out {item.name}.")
                return
        print("File not found!")

    def check_in_item(self, item_name):
        for item in self.checked_out:
            if item.name == item_name:
                self.checked_in.append(item)
                self.checked_out.remove(item)
                print(f"Checked in {item.name}.")
                return
        print("File not found!")

    def print_items(self):
        print("Items in the Library:")
        for item in self.checked_in:
            print(f"- {item.name}")
        print("Items Checked Out from the Library:")
        for item in self.checked_out:
            print(f"- {item.name}")

class Item:
    def __init__(self, name):
        self.name = name

class Movie(Item):
    def __init__(self, name, actor):
        self.name = name
        self.actor = actor

class Book(Item):
    def __init__(self, name, author):
        self.name = name
        self.author = author

class Album(Item):
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

def main():
    
    library = Library()

    # Add exception handling here
    user_input = input("Do you want to load the library from a file? (Y/N) ").lower()

    if user_input == "y":
        # Put your pickle load code here (with exception handling)
        if os.path.exists("todo.pickle"):
            with open("todo.pickle", "rb") as f:
                pickle.load(f)
        else:
            print("Error Loading Library")

    else:
        library.add_item(Movie("Shrek", "Mike Myers"))
        library.add_item(Movie("Guardians of the Galaxy", "Chris Pratt"))
        library.add_item(Book("The Cat in the Hat", "Dr. Seuss"))
        library.add_item(Book("The Hobbit", "J.R.R. Tolkien"))
        library.add_item(Album("Astroworld", "Hip-Hop"))
        library.add_item(Album("1989", "Pop"))

        library.check_out_item("Shrek")
        library.check_out_item("The Cat in the Hat")
        library.check_out_item("Astroworld")

    library.print_items()

    # Add exception handling here
    user_input = input("Do you want to save the library to a file? (Y/N) ").lower()

    if user_input == "y":
        # Put your pickle dump code here
        # Save the Library() object to a file
        with open("todo.pickle", "wb") as f:
            pickle.dump(library, f)  

if __name__ == "__main__":
    main()