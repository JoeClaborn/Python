# Calculate the surface area of all pizza ate at our company's pizza party
import math

slices = int(input("How many slices are in each pizza: "))
diameter = float(input("How large is the pizza in diameter (in inches): "))
number_of_pizzas = int(input("How many pizzas were ordered: "))
slices_ate = int(input("How many slices were ate: "))

slice_degrees = (360 / slices)
radius = diameter / 2

# This is the area of 1 slice as per Google search (???)
slice_area = (slice_degrees / 360) * math.pi * radius ** 2

pizza_area = math.pi * radius ** 2

total_pizza_area = pizza_area * number_of_pizzas
total_ate_pizza_area = slices_ate * slice_area

left_over_pizza_area = total_pizza_area - total_ate_pizza_area

print(f"There was {left_over_pizza_area} sq in. of left over pizza.")

