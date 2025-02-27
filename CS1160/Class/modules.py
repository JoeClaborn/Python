import random

def main():
    user_input = input("Do you want to roll the dice (y/n): ")
    while user_input != 'n':
        dice_roll = random.randint(1, 6)
        print(f"The dice roll was a {dice_roll}")
        user_input = input("Do you want to roll the dice (y/n): ")
        
if __name__ == "__main__":
    main()
