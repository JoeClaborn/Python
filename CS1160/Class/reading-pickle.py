<<<<<<< HEAD
import pickle

def main():
    my_file = open("grades.pkl", "rb")
    grades = pickle.load(my_file)
    my_file.close()

    print("Successfully loaded grades from pickle file")

    for grade in grades.items():
        uid = grade[0]
        value = grade[1]

        print(f"{uid} : {value}")

if __name__ == "__main__":
    main()
=======
import pickle

def main():
    my_file = open("grades.pkl", "rb")
    grades = pickle.load(my_file)
    my_file.close()

    print("Successfully loaded grades from pickle file")

    for grade in grades.items():
        uid = grade[0]
        value = grade[1]

        print(f"{uid} : {value}")

if __name__ == "__main__":
    main()
>>>>>>> 0bbfd1684901d0e83ffcbb9b34c1d45876c2c81b
