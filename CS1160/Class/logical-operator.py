weight = float(input("Enter your dog's weight in pounds: "))
age = float(input("Enter your dog's age in years: "))
years_since_vet = float(input("How many years has it been since your dog was at the vet? "))

if age > 5 and weight > 120:
    print("You have a large breed dog")
elif age < 5 and weight > 80:
    print("You have a young large breed dog")

if age > 10 or weight > 150 and years_since_vet != 0:
    print("Your dog should see the vet soon!")

if not(age > 10 or weight > 150 and years_since_vet != 0):
    print("Your dog is probably ok.")
