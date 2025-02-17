def my_function():
    print("Hello World")

def main():
    print("Not inside of my_function()... yet!")

    my_function()
    my_function()
    my_function()
    my_function()
    my_function()

    print("This is not inside of my_function()...")

if __name__=="__main__":
    main()
