def function_1():
    print("This is inside of function_1")
    
def function_2():
    print("This is inside of function_2")

def function_3():
    print("This is inside of function_3")

def function_4():
    print("This is inside of function_4")

def main():
    print("This is inside of main")
    function_3()
    function_4()
    function_4()
    function_4()
    function_1()
    function_2()

if __name__=="__main__":
    main()
