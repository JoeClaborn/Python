def within_range(n, minimum, maximum):
    is_within_range = n >= minimum and n < maximum
    return is_within_range

def is_even(n):
    return n % 2 == 0

def square(n):
    result = n ** 2 # n * n
    return result

def get_username_and_password():
    username = input("Username: ")
    password = input("Password: ")

    return username, password

def main():
    x = 3
    y = square(x)

    print(f"{x} squared is {y}")

    if is_even(x):
        print(f"{x} is even!")
    else:
        print(f"{x} is odd!")

    if within_range(y, 0, 100):
        print(f"{y} is within our range")

    if within_range(x, 0, 10):
        print(f"{x} is within our range")

    u, p = get_username_and_password()

    print(f"{u} {p}")

if __name__ == "__main__":
    main()
