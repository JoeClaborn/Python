def celsiusToFahrenheit(c):
    
    f = c * 9 / 5 + 32
    return f

def fahrenheitToCelsius(f):
    c = (f - 32) * 5 / 9
    return c

def main():

    user_input = ''
    while user_input != 'Q':

        user_input = input("Which unit do you want to convert? (C for Celsius, F for Fahrenheit, Q for quit): ")
        
        if user_input == 'C':
            # do something for Celsius
            celsius = float(input("Enter the temperature in Celsius: "))
            fahrenheit = celsiusToFahrenheit(celsius)
            print(f"{celsius:.1f}C = {fahrenheit:.1f}F")
            
        elif user_input == 'F':
            # do something for Fahrenheit
            fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            celsius = fahrenheitToCelsius(fahrenheit)
            print(f"{fahrenheit:.1f}F = {celsius:.1f}C")
            
        elif user_input == 'Q':
            # do something to quit
            print("Thanks for using our temperature converter!")
        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()
