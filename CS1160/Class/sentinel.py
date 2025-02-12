total_bill = 0
bill = 0
bill_count = 0

while bill != -1:
    bill = float(input("Enter in monthly bill (type -1 to quit): "))

    if bill > 0:
        total_bill += bill
        bill_count += 1
    elif bill != -1:
        print(f"{bill} is an invalid number!")

print(f"In total, you spent ${total_bill:.2f} in bills!")

bill_avg = total_bill / bill_count

print(f"On average, you spent ${bill_avg:.2f} over {bill_count} months!")


divisor = float(input("Please enter a divisor that is not 0: "))

while divisor == 0:
    print("You typed in 0!!!!")
    divisor = float(input("Please enter a divisor that is not 0: "))

dividend = float(input("Please enter a dividend: "))
result = dividend / divisor

print(f"{result} = {dividend} / {divisor}")
