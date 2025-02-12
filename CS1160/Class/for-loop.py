grade_sum = 0

for grade in [95, 80, 72, 30, 89, 91]:
    print(f"grade = {grade}")
    grade_sum = grade_sum + grade
    print(f"grade_sum = {grade_sum}")

grade_avg = grade_sum / 6

print(f"grade_avg = {grade_avg:.1f}")

grade_sum = 0
#for index in range(6):
for index in [0, 1, 2, 3, 4, 5]:
    grade = float(input(f"Enter grade #{index + 1}: "))
    print(f"grade = {grade}")
    #grade_sum = grade_sum + grade
    grade_sum += grade
    print(f"grade_sum = {grade_sum}")

grade_avg = grade_sum / 6

print(f"grade_avg = {grade_avg:.1f}")

for num in range(1000, 2000, 1):
    print(f"The next decade is {num}")


my_items = [40, 20, 30, 12, 9000, -1]

for item in my_items:
    print(item)

product = 1
# Calculate the factorial
# 5! = 5 * 4 * 3 * 2 * 1
for value in range(5, 0, -1):
    print(value)
    product *= value
    #product = product * value

print(f"5! = {product}")
