<<<<<<< HEAD
def modify_arguments(some_list, some_int):
    some_list.append("Max")
    some_list[1] = "whatever"
    del some_list[2]
    
    some_int = -1000

def main():
    my_list = [5, 10, 0, 30, 50]
    my_int = 123

    print(f"my_list before modify_arguments() function: {my_list}")
    print(f"my_int before modify_arguments() function: {my_int}")

    modify_arguments(my_list, my_int)
    modify_arugments(['a', 'b', 'c'], 99)

    print(f"my_list after modify_arguments() function: {my_list}")
    print(f"my_int after modify_arguments() function: {my_int}")

if __name__ == "__main__":
    main()
=======
def modify_arguments(some_list, some_int):
    some_list.append("Max")
    some_list[1] = "whatever"
    del some_list[2]
    
    some_int = -1000

def main():
    my_list = [5, 10, 0, 30, 50]
    my_int = 123

    print(f"my_list before modify_arguments() function: {my_list}")
    print(f"my_int before modify_arguments() function: {my_int}")

    modify_arguments(my_list, my_int)
    modify_arugments(['a', 'b', 'c'], 99)

    print(f"my_list after modify_arguments() function: {my_list}")
    print(f"my_int after modify_arguments() function: {my_int}")

if __name__ == "__main__":
    main()
>>>>>>> 0bbfd1684901d0e83ffcbb9b34c1d45876c2c81b
