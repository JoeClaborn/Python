x = 5 + 2 * 10 + 20 * 3 / 5 * 100 * 2 + 10
x = 5 + 2 * 10 + 20 *\
    3 / 5 * 100 * 2 + 10
y = "Max" + "Gilson"
y = "Max" + \
    "Gilson"
print(x)
print(y)
print("Max", "Gilson",
      "Jack", "Johnson",
      "Bob", "Smith", sep='\t', end='\n')
print("Sophie", "Gilson", "Eric", "Smith", sep='\t')

firstName = "Bob"
lastName = "Smith"
payRate = 20.00
hoursWorkedPerWeek = 40
weeklyPay = payRate * hoursWorkedPerWeek
halfWeekPay = weeklyPay / 2

print(firstName, lastName, "makes $", weeklyPay, "per week by working for $", payRate, "per hour")
print(f"{firstName} {lastName} makes ${weeklyPay:.2f} per week by working for ${payRate:.2f} per hour")
print(f"{firstName} {lastName} makes ${weeklyPay:.2f} per week.\nBy making ${payRate:.2f} per hour")

balance = 1250
taxRate = 0.069
amount = balance * taxRate
print(amount)


