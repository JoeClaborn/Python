

def main():
    while True:
        my_tuple = (3, 5, 0, 10)
        #my_list = [3, 5, 0, 10]

        some_list = ['aaaaa', 'bbb', 'cc', 'd']

        del some_list[0]
        
        some_tuple = tuple(some_list)

        print(some_tuple)

        

        print(my_tuple)
        #print(my_list)

        #my_tuple[1] = -5
        #my_list[1] = -5

        user_input = int(input("Enter a number: "))
        if user_input in my_tuple:
            print(f"Yes! {user_input} is in your tuple")
    
if __name__ == "__main__":
    main()
