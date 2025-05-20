import random as r
import math
import return_function

def main():

    r.seed("hello?")
    
    user_input = input("Do you want to roll the dice (y/n): ")
    while user_input != 'n':
        dice_roll = r.randint(1, 6)
        print(f"The dice roll was a {dice_roll}")
        user_input = input("Do you want to roll the dice (y/n): ")

    num = r.randrange(0, 10)
    print(f"The next number is: {num}")

    if return_function.within_range(num, 0, 3):
        print(f"Yay! we used our custom module to see if the number {num} was between 0 and 3!!!")

    random_num = r.random()
    print(f"The random number is: {random_num}")

    angle = 45
    angle_radians = math.radians(angle)
    x = math.sin(angle_radians)

    print(f"{x} = sin({angle_radians})")

    print
            
if __name__ == "__main__":
    main()
