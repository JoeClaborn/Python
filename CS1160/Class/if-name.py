print("Welcome to CS 1160 at WSU!!!")
name = input("Please enter your name: ")

if name == "Max Gilson":
    print(f"Hello {name}! You are the instructor for this course!")
    
else:
    print(f"Hello {name}! You must be a student in this course.")

    days = int(input(f"How many days have you attended class?"))

    if days > 5:
        print("Good job you are doing great!")

    elif days > 3:
        print("Ok not bad...")

    elif days > 0:
        print("At least 1 class")

    else:
        print("Wow lot of recordings to watch!")
    

print("Please find your seat... lecture will continue shortly.")
