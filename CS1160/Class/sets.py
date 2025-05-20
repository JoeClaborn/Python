def main():
    my_set = set([1, 2, 3, 3, 3, 3, 4, 5])

    my_set.add(-100)
    my_set.update([2, 5, -100, 30, 45, 60, 85])
    my_set.remove(3)
    my_set.discard(3)
    #my_set.remove(3)

    #print(my_set[2])
    #del my_set[2]

    print(my_set)

    print(f"The set has a length of {len(my_set)}")

    for value in my_set:
        print(value)

if __name__ == "__main__":
    main()
