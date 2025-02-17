my_numbers = [3, 5, 1, 2, -10, 6, 12, -20, -1, 3]

total = 0
count = 0

for number in my_numbers:

    if number < 0:
        continue
    
    print(f"Adding {number} to the total: {total}")
    total += number
    count += 1

average = total / count

print(f"The average was: {average}")

total = 0
count = 0

while True:
    user_input = int(input("Please enter a number to add to the average (type -1 to stop): "))

    if user_input == -1:
        break

    total += user_input
    count += 1

average = total / count

print(f"The average was: {average}")
    
