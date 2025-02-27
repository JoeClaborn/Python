import  math

innerRadius = float(input("Enter the inner radius of the straw (mm): "))
outerRadius = float(input("Enter the outer radius of the straw (mm): "))
height = float(input("Enter the height of the straw (mm): "))
num = int(input("Enter the number of straws manufactured: "))
cost = int(input("Enter the cost of the material ($USD/m^3): "))
volume = (math.pi * ((outerRadius ** 2.0) - (innerRadius ** 2.0)) * height) / 1000
cost = volume * cost
averageCost = cost / num
print(f"The total cost to manufacture {num} straws is ${cost:.2f} which is an average cost of ${averageCost:.2f} per straw.")