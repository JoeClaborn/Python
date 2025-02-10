# Joe Claborn - CS1160 - Lab 03

print("Welcome to the grade estimator.")

grade1 = float(input("Please enter your grade for assignment 1: "))
grade2 = float(input("Please enter your grade for assignment 2: "))
grade3 = float(input("Please enter your grade for assignment 3: "))
grade4 = float(input("Please enter your grade for assignment 4: "))
grade5 = float(input("Please enter your grade for assignment 5: "))

averageGrade = ((grade1 + grade2 + grade3 + grade4 + grade5) / 5)

print(f"Your average grade is {averageGrade:.2f}")

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