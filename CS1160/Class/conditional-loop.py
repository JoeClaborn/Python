low_range = 50
high_range = 100
number = int(input(f"Please enter a number that is between {low_range} and {high_range}: "))
attempts = 0

while (number < low_range or number > high_range) and attempts < 10:
    print("You did not enter a number within the range! Please try again!")
    number = int(input(f"Please enter a number that is between {low_range} and {high_range}: "))
    attempts = attempts + 1

print(f"Congrats you did it!")
