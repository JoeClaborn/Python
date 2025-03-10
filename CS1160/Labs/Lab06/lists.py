# Joe Claborn - CS1160 - Lab 06

def append_item(my_list, item) :
    my_list.append(item)

def insert_item(my_list, item, index) :
    if (index >= 0 and index < len(my_list)) :
        my_list.insert(index, item)
        return True
    else :
        print(f"Cannot insert at index {index}!")
        return False

def print_list(my_list) :
    print(my_list)

def remove_item(my_list, item) :
    if item in my_list :
        my_list.remove(item)
    else :
        print(f"{item} was not in the list!")

def sort_list(my_list) :
    my_list.sort()
    print(my_list)

my_list = []
print("Welcome to The List Program\nA - Append Item to End of List\nI - Insert Item into List\nP - Print Entire List\nR - Remove Item from List\nS - Sort List\nQ - Quit")
choice = input("Enter your choice: ")

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
        print(f"{choice} is not a valid choice!")
        print("A - Append Item to End of List\nI - Insert Item into List\nP - Print Entire List\nR - Remove Item from List\nS - Sort List\nQ - Quit")
        choice = input("Enter your choice: ")

print("Thanks for using The List Program")