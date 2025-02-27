def function_a():
    print("Hello World!")

def function_b():
    print("Go away!")

def function_c(x, y):
    z = x ** y
    print(f"{z} = {x} ^ {y}")

def main():

    user_input = 'a'
    
    while user_input != 'Q':
        user_input = input("Please select an option (A, B, C, or Q for quit): ")

        if user_input == 'A':
            function_a()
        elif user_input == 'B':
            function_b()
        elif user_input == 'C':
            user_num_0 = int(input("Please enter a number: "))
            user_num_1 = int(input("Please enter a number: "))
            function_c(user_num_0, user_num_1)
        elif user_input == 'Q':
            print("Goodbye!")
        else:
            print(f"Error: option {user_input} not found!")

if __name__ == "__main__":
    main()
