<<<<<<< HEAD
##def main():
##
##    while True:
##        try:
##            num = int(input("Provide a numerator: "))
##            dem = int(input("Provide a demonimator: "))
##
##            break
##        except ValueError:
##            print("Error: You're supposed to enter an integer!!!")
##
##    try:
##        result = num / dem
##        print(f"{result} = {num} / {dem}")
##    except ZeroDivisionError:
##        print("Error: You're not supposed to divide by 0!!!!")
def main():

    while True:
        try:
            num = int(input("Provide a numerator: "))
            dem = int(input("Provide a demonimator: "))

            result = num / dem
            print(f"{result} = {num} / {dem}")

            break
        except ValueError as exception_object:
            print("Error: There was a value error... but I don't know why... hmmm...")
            print(exception_object)
        except ZeroDivisionError:
            print("Error: You're not supposed to divide by 0!!!!")
        except:
            print("Error: I don't know what went wrong!!!")

if __name__ == "__main__":
    main()
=======
##def main():
##
##    while True:
##        try:
##            num = int(input("Provide a numerator: "))
##            dem = int(input("Provide a demonimator: "))
##
##            break
##        except ValueError:
##            print("Error: You're supposed to enter an integer!!!")
##
##    try:
##        result = num / dem
##        print(f"{result} = {num} / {dem}")
##    except ZeroDivisionError:
##        print("Error: You're not supposed to divide by 0!!!!")
def main():

    while True:
        try:
            num = int(input("Provide a numerator: "))
            dem = int(input("Provide a demonimator: "))

            result = num / dem
            print(f"{result} = {num} / {dem}")

            break
        except ValueError as exception_object:
            print("Error: There was a value error... but I don't know why... hmmm...")
            print(exception_object)
        except ZeroDivisionError:
            print("Error: You're not supposed to divide by 0!!!!")
        except:
            print("Error: I don't know what went wrong!!!")

if __name__ == "__main__":
    main()
>>>>>>> 0bbfd1684901d0e83ffcbb9b34c1d45876c2c81b
