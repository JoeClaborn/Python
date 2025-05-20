

def main():
    filename = "test.txt"
    user_input = ' '
    while user_input != 'q':
        user_input = input("Type r for reading or w for writing: ")
        
        if user_input == 'r':
            file_object = open(filename, 'r')
            line = 'a'
            
            while line != '':
                line = file_object.readline()
                line = line.rstrip('\n')
                print(line)

            file_object.close()
        elif user_input == 'w':
            file_object = open(filename, 'a')

            #file_object.write("This is some text that's being written to the file!\n")
            #file_object.write("here's some more text\n")
            #file_object.write("and more!\n")

            written_text = 'a'

            line_number = 1

            while written_text != '':
                written_text = input("Type something: ")
                file_object.write(f"Line Number {line_number}: ")
                #file_object.write("Line Number ")
                #file_object.write(str(line_number))
                #file_object.write(": ")
                file_object.write(written_text)
                file_object.write("\n")
                line_number += 1

            file_object.close()
        elif user_input == 'q':
            print("Goodbye!")
        else:
            print("Invalid!")

if __name__ == "__main__":
    main()
