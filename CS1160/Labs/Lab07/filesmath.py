# Joe Claborn - CS1160 - Lab 07

import os
os.chdir("C:\\Users\\josep\\OneDrive\\Desktop\\Python\\CS1160\\Labs\\Lab07\\")

# Function definitions for each math operation that the user can choose from.
def add_nums(firstNum, secondNum) :
    result = firstNum + secondNum
    print(f"{firstNum:.1f} + {secondNum:.1f} = {result}")
    return result
def subtract_nums(firstNum, secondNum) :
    result = firstNum - secondNum
    print(f"{firstNum:.1f} - {secondNum:.1f} = {result}")
    return result
def mult_nums(firstNum, secondNum) :
    result = firstNum * secondNum
    print(f"{firstNum:.1f} * {secondNum:.1f} = {result}")
    return result
def div_nums(firstNum, secondNum) :
    result = firstNum / secondNum
    print(f"{firstNum:.1f} / {secondNum:.1f} = {result}")
    return result
def mod_nums(firstNum, secondNum) :
    result = firstNum % secondNum
    print(f"{firstNum:.1f} % {secondNum:.1f} = {result}")
    return result
def input_file(filename) :
    try :
        myFile = open(filename, 'r')
        outputFile = open("output.txt",'w')

        while True :
            operation = myFile.readline().strip()
            if not operation :
                break
            firstNum = float(myFile.readline().strip())
            secondNum = float(myFile.readline().strip())

            if operation == 'a' :
                result = add_nums(firstNum, secondNum)
            elif operation == 's' :
                result = subtract_nums(firstNum, secondNum)
            elif operation == 'm' :
                result = mult_nums(firstNum, secondNum)
            elif operation == 'd' :
                result = div_nums(firstNum, secondNum)
            elif operation == 'o' :
                result = mod_nums(firstNum, secondNum)
            else :
                print(f"Invalid operation in file: {operation}")
                continue

            if result is not None :
                outputFile.write(f"{result}\n")

        myFile.close()
        outputFile.close()
    except FileNotFoundError :
        print(f"Error: File '{filename}' not found.")
    except ValueError :
        print("Error: Invalid number format in file.")

# Welcome the user.
print("Welcome to my calculator! Here are the following choices:")
# Print the user's option choices.
print("a - addition\ns - subtraction\nm - multiplication\nd - divison\no - modulo\ni - input from file\nq - quit program")

userInput = input("Enter the mathematical operation [a, s, m, d, o, i, q]: ")

# If the user input is not a "q" keep iterating through the while loop.
while (userInput != "q") :
    if userInput in ['a', 's', 'm', 'd', 'o']:
        firstNum = float(input("Enter the first number in the operation: "))
        secondNum = float(input("Enter the second number in the operation: "))

        if userInput == "a":
            add_nums(firstNum, secondNum)
        elif userInput == "s":
            subtract_nums(firstNum, secondNum)
        elif userInput == "m":
            mult_nums(firstNum, secondNum)
        elif userInput == "d":
            div_nums(firstNum, secondNum)
        elif userInput == "o":
            mod_nums(firstNum, secondNum)
    # If the user input is "i" call the input_file function and do the mathematical calculations based
    # on the contents of the file passed through.
    elif (userInput == "i") :
        filename = input("Enter the name of the file: ")
        input_file(filename)
    # If the user input is anything other than [a, s, m, d, o, q] then print that the input is invalid
    # and ask the user for a mathematical operator again (repeat until valid).
    else :
        print("Invalid input!")
        
    userInput = input("Enter the mathematical operation [a, s, m, d, o, q]: ")