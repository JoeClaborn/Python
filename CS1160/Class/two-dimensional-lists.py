<<<<<<< HEAD


def main():
    #bills = [50.35, 100.00, 250.00]
    bills = [["Gilson", 200.00, 120],
             ["Johnson", 45.30, 30],
             ["Smith", 301.05, 10]]

    print(bills)

    for row in bills:
        name = row[0]
        tab = row[1]
        time = row[2]
        print(f"Reservation Name: {name} Bill: ${tab:.2f}")

        if time > 60:
            print(f"{name}'s party has been here for over an hour. Kick them out!!!")

if __name__ == "__main__":
    main()
=======


def main():
    #bills = [50.35, 100.00, 250.00]
    bills = [["Gilson", 200.00, 120],
             ["Johnson", 45.30, 30],
             ["Smith", 301.05, 10]]

    print(bills)

    for row in bills:
        name = row[0]
        tab = row[1]
        time = row[2]
        print(f"Reservation Name: {name} Bill: ${tab:.2f}")

        if time > 60:
            print(f"{name}'s party has been here for over an hour. Kick them out!!!")

if __name__ == "__main__":
    main()
>>>>>>> 0bbfd1684901d0e83ffcbb9b34c1d45876c2c81b
