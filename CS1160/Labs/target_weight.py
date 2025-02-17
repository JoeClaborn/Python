# Joe Claborn - CS1160 - Lab 04 - Part 2

startingWeight = float(input("Enter your starting weight (in lbs): "))
weightGoal = float(input("Enter how much weight you want to lose per month (in lbs): "))
print("Month: \t | \t Target Weight: ")
print("-----------------------")
count = 1

for num in range(1, 6, 1) :
    newWeight = startingWeight - weightGoal
    print(f"count = {count}")
    print(f"count \t | \t {newWeight:.1f}")
    count += 1

weightGoalTotal = weightGoal * count
print(f"You're going to lose {weightGoalTotal:.1f} over the next six months! \nYou got this.")