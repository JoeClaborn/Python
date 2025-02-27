h = 10

def do_math(x, m, b, maximum):
    #global h
    #h = -5
    x *= h
    y = m * x + b

    if y > maximum:
        y = maximum
    
    print(f"{y} = {m} * {x} + {b}")

    return y


def main():
    print("This is in main()")
    a = 450
    print(f"before function h = {h}")
    
    c = do_math(a, 3, 10, maximum=5000)

    print(f"c = {c}")

    d = do_math(a, 3, c, maximum=100000)

    print(f"d = {d}")

    print(f"after function h = {h}")

if __name__ == "__main__":
    main()
