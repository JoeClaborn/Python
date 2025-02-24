# Joe Claborn - CS1160 - Lab 05

# This program is a calculator that based on the operation that the user wants to do, it will call the required
# function and do the operation within it that is wanted based on the two arguments passed as parameters to the
# requested function. Then, the function will print out the result and will ask the user again what operation they
# wish to do until they enter a "q" which then stop the program. It also checks for user input and any invaid input
# will be handled accordingly.

# Function definitions for each math operation that the user can choose from.
def add_nums(firstNum, secondNum) :
    result = firstNum + secondNum
    print(f"{firstNum:.1f} + {secondNum:.1f} = {result}")
def subtract_nums(firstNum, secondNum) :
    result = firstNum - secondNum
    print(f"{firstNum:.1f} - {secondNum:.1f} = {result}")
def multiply_nums(firstNum, secondNum) :
    result = firstNum * secondNum
    print(f"{firstNum:.1f} x {secondNum:.1f} = {result}")
def divide_nums(firstNum, secondNum) :
    result = firstNum / secondNum
    print(f"{firstNum:.1f} / {secondNum:.1f} = {result}")
def modulo_nums(firstNum, secondNum) :
    result = firstNum % secondNum
    print(f"{firstNum:.1f} % {secondNum:.1f} = {result}")

userInput = ""

# Welcome the user.
print("Welcome to my calculator! Here are the following choices:")
# Print the user's option choices.
print("a - addition\ns - subtraction\nm - multiplication\nd - divison\no - modulo\nq - quit program")

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
        multiply_nums(firstNum, secondNum)
        userInput = input("Enter the mathematical operation [a, s, m, d, o, q]: ")
    # If the user input is "d" call the division function based on the two numbers given as parameters.
    elif (userInput == "d") :
        firstNum = float(input("Enter the first number in the operation: "))
        secondNum = float(input("Enter the second number in the operation: "))
        divide_nums(firstNum, secondNum)
        userInput = input("Enter the mathematical operation [a, s, m, d, o, q]: ")
    # If the user input is "o" call the modulo function based on the two numbers given as parameters.
    elif (userInput == "o") :
        firstNum = float(input("Enter the first number in the operation: "))
        secondNum = float(input("Enter the second number in the operation: "))
        modulo_nums(firstNum, secondNum)
        userInput = input("Enter the mathematical operation [a, s, m, d, o, q]: ")
    # If the user input is anything other than [a, s, m, d, o, q] then print that the input is invalid
    # and ask the user for a mathematical operator again (repeat until valid).
    else :
        print("Invalid input!")
        userInput = input("Enter the mathematical operation [a, s, m, d, o, q]: ")