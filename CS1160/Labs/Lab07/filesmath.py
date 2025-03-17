# Joe Claborn - CS1160 - Lab 07

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
    myFile = open(filename, 'r')
    while line != '':
        line = myFile.readline()
        line = line.rstrip('\n')
        print(line)

    myFile.close()

userInput = ""

# Welcome the user.
print("Welcome to my calculator! Here are the following choices:")
# Print the user's option choices.
print("a - addition\ns - subtraction\nm - multiplication\nd - divison\no - modulo\ni - input from file\nq - quit program")

# If the user input is not a "q" keep iterating through the while loop.
while (userInput != "q") :
    # If the user input is "a" call the addition function based on the two numbers given as parameters.
    if (userInput == "a") :
        firstNum = float(input("Enter the first number in the operation: "))
        secondNum = float(input("Enter the second number in the operation: "))
        add_nums(firstNum, secondNum)
        userInput = input("Enter the mathematical operation [a, s, m, d, o, q]: ")
    # If the user input is "s" call the subtraction function based on the two numbers given as parameters.
    elif (userInput == "s") :
        firstNum = float(input("Enter the first number in the operation: "))
        secondNum = float(input("Enter the second number in the operation: "))
        subtract_nums(firstNum, secondNum)
        userInput = input("Enter the mathematical operation [a, s, m, d, o, q]: ")
    # If the user input is "m" call the multiplication function based on the two numbers given as parameters.
    elif (userInput == "m") :
        firstNum = float(input("Enter the first number in the operation: "))
        secondNum = float(input("Enter the second number in the operation: "))
        mult_nums(firstNum, secondNum)
        userInput = input("Enter the mathematical operation [a, s, m, d, o, q]: ")
    # If the user input is "d" call the division function based on the two numbers given as parameters.
    elif (userInput == "d") :
        firstNum = float(input("Enter the first number in the operation: "))
        secondNum = float(input("Enter the second number in the operation: "))
        div_nums(firstNum, secondNum)
        userInput = input("Enter the mathematical operation [a, s, m, d, o, q]: ")
    # If the user input is "o" call the modulo function based on the two numbers given as parameters.
    elif (userInput == "o") :
        firstNum = float(input("Enter the first number in the operation: "))
        secondNum = float(input("Enter the second number in the operation: "))
        mod_nums(firstNum, secondNum)
        userInput = input("Enter the mathematical operation [a, s, m, d, o, q]: ")
    # If the user input is "i" call the input_file function and do the mathematical calculations based
    # on the contents of the file passed through.
    elif (userInput == 'i') :
        filename = input("Enter the name of the file: ")
        input_file(filename)
    # If the user input is anything other than [a, s, m, d, o, q] then print that the input is invalid
    # and ask the user for a mathematical operator again (repeat until valid).
    else :
        print("Invalid input!")
        userInput = input("Enter the mathematical operation [a, s, m, d, o, q]: ")