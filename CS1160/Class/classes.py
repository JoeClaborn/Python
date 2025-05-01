class Car:

    def __init__(self, start_color, start_make, start_model):
        self.color = start_color
        self.make = start_make
        self.model = start_model

    def paint_car(self, new_color):
        self.color = new_color
        

def main():
    my_car_0 = Car("Red", "Ford", "Mustang")
    my_car_1 = Car("Blue", "Toyota", "RAV4")

    my_car_0.paint_car("Black")

    print(f"my_car_0's color = {my_car_0.color}")
    print(f"my_car_0's make = {my_car_0.make}")
    print(f"my_car_0's model = {my_car_0.model}")

    print(f"my_car_1's color = {my_car_1.color}")
    print(f"my_car_1's make = {my_car_1.make}")
    print(f"my_car_1's model = {my_car_1.model}")

if __name__ == "__main__":
    main()
