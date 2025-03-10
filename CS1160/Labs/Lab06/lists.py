# Joe Claborn - CS1160 - Lab 06

# This program allows for the user to use different list functions to become familiar with how lists work in Python.
# They have the options of appending, inserting, removing, printing, and sorting a list.

# Function definition for appending an item to a list.
def append_item(my_list, item) :
    my_list.append(item)

# Function definition for inserting an item to a list.
def insert_item(my_list, item, index) :
    if (index >= 0 and index < len(my_list)) :
        my_list.insert(index, item)
        return True
    else :
        # If the index chosen is larger than the length of the list, do not insert the item given and
        # tell the user that they cannot insert at that index.
        print(f"Cannot insert at index {index}!")
        return False

# Function definition for printing the list out.
def print_list(my_list) :
    print(my_list)

# Function definition for removing an item from a list.
def remove_item(my_list, item) :
    if item in my_list :
        my_list.remove(item)
    else :
        # If the item given by the user is not within the list, do not remove any items and
        # tell the user that the item is not in the list.
        print(f"{item} was not in the list!")

# Function definition for sorting the list.
def sort_list(my_list) :
    my_list.sort()

# Create an empty list.
my_list = []
# Welcome the user and show the options of the program.
print("Welcome to The List Program\nA - Append Item to End of List\nI - Insert Item into List\nP - Print Entire List\nR - Remove Item from List\nS - Sort List\nQ - Quit")
# Allow the user to input their choice.
choice = input("Enter your choice: ")

# While the user input is not 'Q', iterate through the options as the user sees fit and based on what they would like to do to
# the list with the given options. Depending on the user's choice, call that function and do what is asked by the user.
while (choice != 'Q') :
    if (choice == 'A' ) :
        item = input("Enter a string to append to the list: ")
        append_item(my_list, item)
        print("A - Append Item to End of List\nI - Insert Item into List\nP - Print Entire List\nR - Remove Item from List\nS - Sort List\nQ - Quit")
        choice = input("Enter your choice: ")
    elif (choice == 'I') :
        item = input("Enter a string to insert into the list: ")
        index = int(input("Enter an index to insert at: "))
        insert_item(my_list, item, index)
        print("A - Append Item to End of List\nI - Insert Item into List\nP - Print Entire List\nR - Remove Item from List\nS - Sort List\nQ - Quit")
        choice = input("Enter your choice: ")
    elif (choice == 'P') :
        print_list(my_list)
        print("A - Append Item to End of List\nI - Insert Item into List\nP - Print Entire List\nR - Remove Item from List\nS - Sort List\nQ - Quit")
        choice = input("Enter your choice: ")
    elif (choice == 'R') :
        item = input("Enter a string to remove from the list: ")
        remove_item(my_list, item)
        print("A - Append Item to End of List\nI - Insert Item into List\nP - Print Entire List\nR - Remove Item from List\nS - Sort List\nQ - Quit")
        choice = input("Enter your choice: ")
    elif (choice == 'S') :
        sort_list(my_list)
        print("The list is now sorted!")
        print("A - Append Item to End of List\nI - Insert Item into List\nP - Print Entire List\nR - Remove Item from List\nS - Sort List\nQ - Quit")
        choice = input("Enter your choice: ")
    else :
        # If the user's choice is not within the valid options, tell the user and allow them to choose a valid option.
        print(f"{choice} is not a valid choice!")
        print("A - Append Item to End of List\nI - Insert Item into List\nP - Print Entire List\nR - Remove Item from List\nS - Sort List\nQ - Quit")
        choice = input("Enter your choice: ")

# Tell the user thank you for their interest in the program.
print("Thanks for using The List Program")