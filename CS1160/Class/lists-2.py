<<<<<<< HEAD
def main():

    names = ['Max', 'Xander', 'Jack', 'Sophie', 'Lori', 'Eric']

    del names[1]

    names.clear()

    check_name = input("Enter a name you want to search for: ")

    #print(f"{names.index('Ziggy')}")

    if check_name in names:
        print(f"Yes! {check_name} is in the list of names!")
        found_index = names.index(check_name)
        print(f"{check_name} appears at index {found_index} in the list")
    else:
        print(f"No! {check_name} is NOT in the list of names!")
        insert_at_index = int(input("Type an index to insert this new name at: "))
        names.insert(insert_at_index, check_name)

    names.append('Buddy')
    names.append('Yoshi')
    names.append('Loki')

    names.append('Max')
    names.append('Max')
    names.append('Max')

    names.remove('Max')

    

    names.sort(reverse=True)
    #names.reverse()

    print(names)

    names_copy = []

    #names_copy += names

    for name in names:

        if name == "Ziggy":
            continue
        
        names_copy.append(name)

    names_copy.remove('Loki')
    names_copy.remove('Buddy')

    print(names)
    print(names_copy)

    numbers = [1, 2, 3, 10, 50, 99, 123]

    total = 0

    for number in numbers:
        total += number

    average = total / len(numbers)
    print(f"The average of your list of numbers is {average}")

if __name__ == "__main__":
    main()
=======
def main():

    names = ['Max', 'Xander', 'Jack', 'Sophie', 'Lori', 'Eric']

    del names[1]

    names.clear()

    check_name = input("Enter a name you want to search for: ")

    #print(f"{names.index('Ziggy')}")

    if check_name in names:
        print(f"Yes! {check_name} is in the list of names!")
        found_index = names.index(check_name)
        print(f"{check_name} appears at index {found_index} in the list")
    else:
        print(f"No! {check_name} is NOT in the list of names!")
        insert_at_index = int(input("Type an index to insert this new name at: "))
        names.insert(insert_at_index, check_name)

    names.append('Buddy')
    names.append('Yoshi')
    names.append('Loki')

    names.append('Max')
    names.append('Max')
    names.append('Max')

    names.remove('Max')

    

    names.sort(reverse=True)
    #names.reverse()

    print(names)

    names_copy = []

    #names_copy += names

    for name in names:

        if name == "Ziggy":
            continue
        
        names_copy.append(name)

    names_copy.remove('Loki')
    names_copy.remove('Buddy')

    print(names)
    print(names_copy)

    numbers = [1, 2, 3, 10, 50, 99, 123]

    total = 0

    for number in numbers:
        total += number

    average = total / len(numbers)
    print(f"The average of your list of numbers is {average}")

if __name__ == "__main__":
    main()
>>>>>>> 0bbfd1684901d0e83ffcbb9b34c1d45876c2c81b
