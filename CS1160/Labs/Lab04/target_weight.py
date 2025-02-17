# Joe Claborn - CS1160 - Lab 04 - Part 2

# This program allows the user to input a starting weight and desired goal and
# loops through 6 months to show the progress needed for the target weight
# along with printing out the total weight loss at the end of the program.

# Create startingWeight variable for the user to input their starting weight.
startingWeight = float(input("Enter your starting weight (in lbs): "))
# Create weightGoal variable for the user to enter their desired goal.
weightGoal = float(input("Enter how much weight you want to lose per month (in lbs): "))
print("\nMonth: \t | \t Target Weight: ")
print("----------------------")

# Loops between months 1-6, takes the starting weight and subtracts it from the
# weight goal times which month it is to get the new weight for the month.
for month in range(1, 7) :
    newWeight = startingWeight - (weightGoal * month)
    print(f"{month} \t | \t {newWeight:.1f}")

# Gets the total weight loss over the next 6 months.
weightGoalTotal = weightGoal * 6
# Prints the total weight loss and leaves an encouraging message for the user.
print(f"\nYou're going to lose {weightGoalTotal:.1f} pounds over the next six months! \nYou got this!")