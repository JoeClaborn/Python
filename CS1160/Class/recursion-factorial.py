<<<<<<< HEAD
def factorial(n):
    print(f"factorial({n}) was called...")
    if n == 0:
        print(f"factorial({n}) has returned 1")
        return 1 # 0! = 1
    else:
        result = factorial(n - 1)
        print(f"factorial({n}) has returned {n * result}")
        return n * result # n! = n * (n - 1)!

def main():

    while True:
        value = int(input("Please enter a value for n: "))

        result = factorial(value)

        print(f"{value}! = {result}")
    

if __name__ == "__main__":
    main()
=======
def factorial(n):
    print(f"factorial({n}) was called...")
    if n == 0:
        print(f"factorial({n}) has returned 1")
        return 1 # 0! = 1
    else:
        result = factorial(n - 1)
        print(f"factorial({n}) has returned {n * result}")
        return n * result # n! = n * (n - 1)!

def main():

    while True:
        value = int(input("Please enter a value for n: "))

        result = factorial(value)

        print(f"{value}! = {result}")
    

if __name__ == "__main__":
    main()
>>>>>>> 0bbfd1684901d0e83ffcbb9b34c1d45876c2c81b
