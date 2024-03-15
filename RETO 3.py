class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def total(self, quantity):
        return self.price * quantity


class Beverage(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size


class Appetizer(MenuItem):
    pass


class MainCourse(MenuItem):
    pass


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self.items.append((item, quantity))

    def bill(self):
        bill = 0
        for item, quantity in self.items:
            bill += item.total(quantity)
        return bill
    def print_order(self):
        print("Order:")
        for item, quantity in self.items:
            print(f"{item.name} x {quantity}")


menu = {
    "Vino": Beverage("Vino", 65000, "botella"),
    "Agua": Beverage("Agua", 3000, "botella"),
    "Cerveza": Beverage("Cerveza", 10000, "botella"),
    "Papas": Appetizer("Papas", 13000),
    "Alitas": Appetizer("Alitas", 25000),
    "Churazco": MainCourse("Churazco", 45000),
    "Reve eye": MainCourse("Reve eye", 65000),
    "Salmon": MainCourse("Salmon", 55000),
    "Pasta Carbonara": MainCourse("Pasta Carbonara", 35000),
    "Pasta Bolognesa": MainCourse("Pasta Bolognesa", 35000),
}

order = Order()
order.add_item(menu["Vino"], 1)
order.add_item(menu["Alitas"], 1)
order.add_item(menu["Churazco"], 1)
order.add_item(menu["Reve eye"], 1)

order.print_order()
print("Total a pagar:", order.bill())