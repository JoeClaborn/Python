class GroceryStore:

    def __init__(self, name):
        self.__name = name
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def value_of_inventory(self):

        total_value = 0
        for product in self.__products:
            total_value += product.get_price()

        return total_value

class Product:

    def __init__(self, name, brand, weight, price):
        self.name = name
        self.__brand = brand
        self.__weight = weight
        self.__price = price

    def __str__(self):
        return f"This product is {self.__brand} branded {self.name} at a price of ${self.__price:.2f}"

    def set_price(self, new_price):

        if new_price <= 0.0:
            print(f"Error: attempted to set the price of {self.__brand} {self.name} to ${new_price:.2f} from a price of ${self.__price:.2f}")
            return
        
        self.__price = new_price

    def get_price(self):
        return self.__price

def main():

    grocery_store = GroceryStore("Walmart")
    #grocery_store_2 = GroceryStore("Walmart - Downtown")
    
    product_0 = Product("Banana", "Chiquita", 0.1, 0.15)
    product_1 = Product("Banana", "Bonita", 0.11, 0.09)
    product_2 = Product("Shampoo", "Dove", 1.2, 6.99)
    product_3 = Product("Eggs", "Eggland", 0.8, 5.99)
    product_4 = Product("Rice", "Minute", 2.0, 2.98)

    print(product_0)
    print(product_1)
    print(product_2)
    print(product_3)
    print(product_4)

    print("Changing prices...")

    product_1.set_price(0.25)
    product_0.set_price(0.30)
    product_2.set_price(-5.99)

    print("Prices have been changed...")

    print(product_0)
    print(product_1)
    print(product_2)
    print(product_3)
    print(product_4)


    grocery_store.add_product(product_0)
    grocery_store.add_product(product_1)
    grocery_store.add_product(product_2)
    grocery_store.add_product(product_3)
    grocery_store.add_product(product_4)

    result = grocery_store.value_of_inventory()

    print(f"The current value of all items on our shelf in our grocery store is ${result:.2f}")
    

if __name__ == "__main__":
    main()

class GroceryStore:

    def __init__(self, name):
        self.__name = name
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def value_of_inventory(self):

        total_value = 0
        for product in self.__products:
            total_value += product.get_price()

        return total_value

class Product:

    def __init__(self, name, brand, weight, price):
        self.name = name
        self.__brand = brand
        self.__weight = weight
        self.__price = price

    def __str__(self):
        return f"This product is {self.__brand} branded {self.name} at a price of ${self.__price:.2f}"

    def set_price(self, new_price):

        if new_price <= 0.0:
            print(f"Error: attempted to set the price of {self.__brand} {self.name} to ${new_price:.2f} from a price of ${self.__price:.2f}")
            return
        
        self.__price = new_price

    def get_price(self):
        return self.__price

def main():

    grocery_store = GroceryStore("Walmart")
    #grocery_store_2 = GroceryStore("Walmart - Downtown")
    
    product_0 = Product("Banana", "Chiquita", 0.1, 0.15)
    product_1 = Product("Banana", "Bonita", 0.11, 0.09)
    product_2 = Product("Shampoo", "Dove", 1.2, 6.99)
    product_3 = Product("Eggs", "Eggland", 0.8, 5.99)
    product_4 = Product("Rice", "Minute", 2.0, 2.98)

    print(product_0)
    print(product_1)
    print(product_2)
    print(product_3)
    print(product_4)

    print("Changing prices...")

    product_1.set_price(0.25)
    product_0.set_price(0.30)
    product_2.set_price(-5.99)

    print("Prices have been changed...")

    print(product_0)
    print(product_1)
    print(product_2)
    print(product_3)
    print(product_4)


    grocery_store.add_product(product_0)
    grocery_store.add_product(product_1)
    grocery_store.add_product(product_2)
    grocery_store.add_product(product_3)
    grocery_store.add_product(product_4)

    result = grocery_store.value_of_inventory()

    print(f"The current value of all items on our shelf in our grocery store is ${result:.2f}")
    

if __name__ == "__main__":
    main()