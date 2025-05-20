def function_1():
    print("This is inside of function_1")
    
def function_2():
    print("This is inside of function_2")
    #print(f"x = {x}")

def function_3():
    y = 20
    print("This is inside of function_3")
    print(f"y = {y}")

def function_4():
    print("This is inside of function_4")

def main():
    x = 10
    print("This is inside of main")
    print(f"x = {x}")
    function_3()
    function_4()
    function_4()
    function_4()
    function_1()
    function_2()
    print(f"y = {y}")

if __name__=="__main__":
    main()
