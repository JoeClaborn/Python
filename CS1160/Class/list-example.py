def main():
    list_of_numbers = [1, 2, 5, 20, -3]

    list_of_data = [1, "Max", 'z', -0.005]

    print(list_of_numbers)
    print(list_of_data)

    for thing in list_of_data:
        print(f"The next thing is {thing}")

    first = list_of_numbers[0]
    last = list_of_numbers[-1]
    print(f"The first element in the list is {first}")
    print(f"The last element in the list is {last}")

    for index in range(0, 5):
        number = list_of_numbers[index]
        print(f"{number}")

if __name__ == "__main__":
    main()
