def main():
    incorrect_attempts = 0
    while True:
        my_string = input("Type in something: ")

        if my_string.isdigit():
            print("Your string is a number/digit")
        #else:
        #    continue

        my_string_upper = my_string.upper()

        print(f"The uppercase version of the string you typed is:\n {my_string_upper}")

        for character in my_string:
            print(character)

        searchable = input("Type in something to search for inside the string: ")

        if searchable in my_string:
            print(f"Yes! {searchable} was inside the string all along!")
        else:
            print(f"No! {searchable} was not inside the string!")

        index = int(input("What index do you want from your string: "))

        if index < len(my_string):
            print(f"Here's your character: {my_string[index]}")
        else:
            incorrect_attempts += 1
            print(f"Hey! Index {index} is outside the range of a string with size {len(my_string)}")

            if incorrect_attempts > 1:
                print(f"Hey! Stop that! This is the second time at LEAST! This is mess up #{incorrect_attempts} for you!")

        my_string_1 = input("Enter the first string to concatenate: ")
        my_string_2 = input("Enter the second string to concatenate: ")
        combined = my_string_1 + my_string_2

        print(f"The first string is {my_string_1} the second string is {my_string_2} combined they are {combined}")
        

if __name__ == "__main__":
    main()
