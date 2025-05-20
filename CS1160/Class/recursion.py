<<<<<<< HEAD
call_count = 0

def fib(n):

    global call_count
    call_count += 1
    #print(f"fib({n}) was called...")

    if n < 2:
        #print(f"fib({n}) has returned {n}")
        return n # fib(0) returns 0 and fib(1) returns 1
    else:
        result_0 = fib(n - 1)
        result_1 = fib(n - 2)

        #print(f"fib({n}) has returned {result_0 + result_1} = {result_0} + {result_1}")
        return result_0 + result_1

def main():

    while True:
        global call_count
        value = int(input("Please enter a value for n: "))

        result = fib(value)

        print(f"fib({value}) = {result}")

        print(f"fib() was called {call_count} times!")
    

if __name__ == "__main__":
    main()
=======
call_count = 0

def fib(n):

    global call_count
    call_count += 1
    #print(f"fib({n}) was called...")

    if n < 2:
        #print(f"fib({n}) has returned {n}")
        return n # fib(0) returns 0 and fib(1) returns 1
    else:
        result_0 = fib(n - 1)
        result_1 = fib(n - 2)

        #print(f"fib({n}) has returned {result_0 + result_1} = {result_0} + {result_1}")
        return result_0 + result_1

def main():

    while True:
        global call_count
        value = int(input("Please enter a value for n: "))

        result = fib(value)

        print(f"fib({value}) = {result}")

        print(f"fib() was called {call_count} times!")
    

if __name__ == "__main__":
    main()
>>>>>>> 0bbfd1684901d0e83ffcbb9b34c1d45876c2c81b
