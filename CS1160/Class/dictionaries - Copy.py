import pickle

def main():
    book = {'title':'Moby Dick', 'author':'Herman Melville', 'year_pub': 1851}
    library = dict()
    library['978-0143105985'] = book

    print(library)

    grades = dict()

    grades["U012345678"] = 100
    grades["U987654321"] = 70
    grades["U000000000"] = 95

    grades = {"U012345678":100,
              "U987654321":70,
              "U000000000":95}

    my_file = open("grades.pkl", "wb")
    pickle.dump(grades, my_file)
    my_file.close()

    #print(grades)
    print(grades.keys())
    print(grades.values())

    for item in grades.items():
        key = item[0]
        value = item[1]
        print(f"Key: {key} Value: {value}")

    grades["U987654321"] = 90
    #del grades["U012345678"]

    popped_grade = grades.pop("U012345678", -1)

    print(f"Popped value: {popped_grade}")

    uid = input("Please enter the UID of the grade you want to see: ")

    if uid in grades:
        print("UID is in grades!")
    else:
        print("UID is NOT in grades!")

    try:
        found_grade = grades[uid]
        print(f"We found a grade of {found_grade}")
    except KeyError:
        student_count = len(grades)
        print(f"Sorry! We checked {student_count} students and you were not in the grade book!")

if __name__ == "__main__":
    main()
