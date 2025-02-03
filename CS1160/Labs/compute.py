# Joe Claborn - CS1160 - Lab 02

# import math library for using pi
import math

# define inches to feet conversion
def inchesToFeet(inches):
    return inches / 12.0

# define rectangle area calculation
def rectangleArea(length, width):
    return length * width

# define circle area calculation
def circleArea(circumference):
    radius = ((circumference / (2.0 * math.pi)) / 12)
    return math.pi * (radius ** 2.0)

# user inputs for the floor's total length and width
floorLength = float(input("Enter floor length (feet): "))
floorWidth = float(input("Enter floor width (feet): "))

# user inputs for the furnace's total length and width
furnaceLength = float(input("Enter the furnace length (inches): "))
furnaceWidth = float(input("Enter the furnace width (inches): "))

# user input for the heater's circumference
heaterCircumference = float(input("Enter the water heater circumference (inches): "))

# convert the furnance's length and width to feet
furnaceLength = inchesToFeet(furnaceLength)
furnaceWidth = inchesToFeet(furnaceWidth)

# calculate the areas of the floor, furnance, and heater
floorArea = rectangleArea(floorLength, floorWidth)
furnaceArea = rectangleArea(furnaceLength, furnaceWidth)
heaterArea = circleArea(heaterCircumference)

# calculate the total paintable area
paintableArea = floorArea - (furnaceArea + heaterArea)

# print the total paintable area in square feet and round to 3 decimals
print(f"Paintable floor area (square feet): {paintableArea:.3f}")