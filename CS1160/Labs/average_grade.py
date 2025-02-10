# Joe Claborn - CS1160 - Lab 03

# This program takes 5 grades from the user's input and
# takes the average of the grade to 2 decimal places then
# uses it to check the average grade to determine what letter
# grade that the user will get in their class

# Print welcome statement
print("Welcome to the grade estimator.")

# User inputs for each assignment (1-5) and create a tracking variable for the user input amount
# and add 1 to its total after each user input is given
userInputTotal = 0
grade1 = float(input("Please enter your grade for assignment 1: "))
userInputTotal = userInputTotal + 1
grade2 = float(input("Please enter your grade for assignment 2: "))
userInputTotal = userInputTotal + 1
grade3 = float(input("Please enter your grade for assignment 3: "))
userInputTotal = userInputTotal + 1
grade4 = float(input("Please enter your grade for assignment 4: "))
userInputTotal = userInputTotal + 1
grade5 = float(input("Please enter your grade for assignment 5: "))
userInputTotal = userInputTotal + 1

# Set averageGrade variable to the user inputs above divided by the amount of inputs
averageGrade = ((grade1 + grade2 + grade3 + grade4 + grade5) / userInputTotal)

# Print out the average grade to the terminal
print(f"Your average grade is {averageGrade:.2f}.")

# If-ElseIf-Else statements to check the user's grade that they will get
# in the class based on the averageGrade variable
if (averageGrade >= 90.00) :
    print("You will get a A in this class.")
elif (averageGrade < 90.00 and averageGrade >= 80.00) :
    print("You will get a B in this class.")
elif (averageGrade < 80.00 and averageGrade >= 70.00) :
    print("You will get a C in this class.")
elif (averageGrade < 70.00 and averageGrade >= 60.00) :
    print("You will get a D in this class.")
else :
    print("You will get a F in this class.")