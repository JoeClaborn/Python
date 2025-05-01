import math
import my_script

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

    number = 0
    while True:
        try:
            num = int(input("Provide a numerator: "))
            dem = int(input("Provide a demonimator: "))

            result = num / dem
            print(f"{result} = {num} / {dem}")

            #break
        except ValueError as e:
            print("Error: There was a value error... but I don't know why... hmmm...")
            print(e)
            number = -1
        except ZeroDivisionError as e:
            print("Error: You're not supposed to divide by 0!!!!")
            print(e)
            number = -1
        except:
            print("Error: I don't know what went wrong!!!")
            number = -1
        else:
            print("Program completed successfully!")
            break
        finally:
            print("This section always executes no matter what!")
            print(f"main() is returning {number}")
            return number

        

if __name__ == "__main__":
    main()
