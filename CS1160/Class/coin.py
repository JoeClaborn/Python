import random

class Coin:

    def __init__(self):
        #self.__side_up = "heads"
        self.__times_flipped = 0

        start_side = random.random()

        if start_side > 0.5:
            self.__side_up = "heads"
        else:
            self.__side_up = "tails"

    def __str__(self):
        return f"This coin is {self.__side_up} and has been flipped {self.__times_flipped} times."

    def flip(self):
        self.__times_flipped += 1

        flip_result = random.random()

        if flip_result > 0.5:
            self.__side_up = "heads"
        else:
            self.__side_up = "tails"
        

def main():

    coin_0 = Coin()
    coin_1 = Coin()
    coin_2 = Coin()

    print(coin_0)
    print(coin_1)
    print(coin_2)

    while True:
        coin_0.flip()
        coin_1.flip()
        coin_2.flip()

        print(coin_0)
        print(coin_1)
        print(coin_2)
        
        input("Hit enter to continue")

if __name__ == "__main__":
    main()
