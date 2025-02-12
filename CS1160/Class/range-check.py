grocery_bill = float(input("How much did you spend on groceries: "))

bill_is_in_budget = grocery_bill / 2 > 100 and grocery_bill / 2 < 250

if bill_is_in_budget:
    print("Great! Your grocery bill was in budget...")
elif not bill_is_in_budget and grocery_bill < 50:
    print("Well, the grocery bill was not in budget but I guess you saved some money...")
else:
    print("Uh-oh! Your grocery bill was not in budget...")
