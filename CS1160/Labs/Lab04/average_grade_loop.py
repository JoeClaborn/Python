# Joe Claborn - CS1160 - Lab 04 - Part 1

# This program is a grade estimator that loops through the grades that the user inputs
# until a 'n' is entered. Once an 'n' is entered by the user, the program gets the
# average grade of all the grades entered, outputs it for the user and informs the
# user of what letter grade they will obtain in their class.

# Print welcome statement
print("Welcome to the grade estimator.")

# Create checkInput variable for checking if the user wants to continue entering grades.
# Create totalGrade variable to keep check of the running total of the grades entered.
# Create count variable to keep track of the total number of grades entered to use to
# find the average grade.
checkInput = ""
totalGrade = 0
count = 0

# While the user's input is not 'n', ask for the grade for the assignment, take the grade
# given and add it to the total grade, increment count by 1, then find the average grade
# for each iteration of the while loop. Then, check if the user wants to input more grades,
# if the input is 'n', exit the loop, if it is 'y', repeat the steps.
while (checkInput != 'n') :
    grade = float(input("Please enter your grade for the assignment: "))
    totalGrade += grade
    count += 1
    averageGrade = totalGrade / count
    checkInput = input("Would you like to enter another grade? (y/n): " )
    print("\n")

# Print out the average grade to the terminal.
print(f"Your average grade is {averageGrade:.2f}.")

# If-ElseIf-Else statements to check the user's grade that they will get
# in the class based on the averageGrade variable.
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
