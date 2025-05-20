<<<<<<< HEAD


def main():
    filename = "missing.txt"
    user_input = ' '
    while user_input != 'q':
        user_input = input("Type r for reading or w for writing: ")
        
        if user_input == 'r':
            try:
                file_object = open(filename, 'r')
            except FileNotFoundError:
                print("Error: File was not found!!!!")
                continue
            
            while True:
                first_name = file_object.readline().rstrip('\n')

                if first_name == '':
                    break
                
                middle_name = file_object.readline().rstrip('\n')

                if middle_name == '':
                    break
                
                last_name = file_object.readline().rstrip('\n')

                if last_name == '':
                    break

                print(f"Greetings, {last_name}, {first_name} {middle_name}")

            file_object.close()
        elif user_input == 'w':
            file_object = open(filename, 'a')

            #file_object.write("This is some text that's being written to the file!\n")
            #file_object.write("here's some more text\n")
            #file_object.write("and more!\n")

            while True:
                first_name = input("Enter in a first name: ")

                if first_name == '':
                    break
                
                middle_name = input("Enter in a middle name: ")

                if middle_name == '':
                    break
                
                last_name = input("Enter in a last name: ")

                if last_name == '':
                    break

                file_object.write(first_name + "\n")
                file_object.write(middle_name + "\n")
                file_object.write(last_name + "\n")
                

            file_object.close()
        elif user_input == 'q':
            print("Goodbye!")
        else:
            print("Invalid!")

if __name__ == "__main__":
    main()
=======


def main():
    filename = "missing.txt"
    user_input = ' '
    while user_input != 'q':
        user_input = input("Type r for reading or w for writing: ")
        
        if user_input == 'r':
            try:
                file_object = open(filename, 'r')
            except FileNotFoundError:
                print("Error: File was not found!!!!")
                continue
            
            while True:
                first_name = file_object.readline().rstrip('\n')

                if first_name == '':
                    break
                
                middle_name = file_object.readline().rstrip('\n')

                if middle_name == '':
                    break
                
                last_name = file_object.readline().rstrip('\n')

                if last_name == '':
                    break

                print(f"Greetings, {last_name}, {first_name} {middle_name}")

            file_object.close()
        elif user_input == 'w':
            file_object = open(filename, 'a')

            #file_object.write("This is some text that's being written to the file!\n")
            #file_object.write("here's some more text\n")
            #file_object.write("and more!\n")

            while True:
                first_name = input("Enter in a first name: ")

                if first_name == '':
                    break
                
                middle_name = input("Enter in a middle name: ")

                if middle_name == '':
                    break
                
                last_name = input("Enter in a last name: ")

                if last_name == '':
                    break

                file_object.write(first_name + "\n")
                file_object.write(middle_name + "\n")
                file_object.write(last_name + "\n")
                

            file_object.close()
        elif user_input == 'q':
            print("Goodbye!")
        else:
            print("Invalid!")

if __name__ == "__main__":
    main()
>>>>>>> 0bbfd1684901d0e83ffcbb9b34c1d45876c2c81b
