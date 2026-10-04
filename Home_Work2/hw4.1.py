class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def change_price(self, new_price):
        self.price = new_price


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.product_order = []

    def add_order(self, order):
        self.product_order.append(order)


class Order:
    def __init__(self):
        self.all_products = []

    def add_product(self, product):
        self.all_products.append(product)

    def total_price(self):
        total = 0
        for product in self.all_products:
            total += product.price
        return total


class Warehouse:
    def __init__(self, name):
        self.name = name
        self.products = {}

    def add_product(self, product, quantity):
        self.products[product] = quantity

    def change_quantity(self, product, new_quantity):
        if product in self.products:
            self.products[product] = new_quantity
        else:
            print("Товар отсутсвует на складе")

    def add_quantity(self, product, new_quantity):
        if product in self.products:
            self.products[product] += new_quantity
        else:
            print("Товар отсутствует на складе")


file_product_order = []
file_customer_order = []
file_orders = []
all_warehouse = {}
with open("shop.txt", "r") as file:
    for line in file:
        line = line.strip().split(";")
        if line[0] == "PRODUCT":
            product, name, category, price = line
            price = float(price)
            product4 = Product(name, price, category)
            file_product_order.append(product4)
        if line[0] == "CUSTOMER":
            customer, name, email = line
            customer2 = Customer(name, email)
            file_customer_order.append(customer2)
        if line[0] == "ORDER":
            order, customer, *products = line
            order2 = Order()
            for product in products:
                for prod in file_product_order:
                    if product == prod.name:
                        order2.add_product(prod)
            for cust in file_customer_order:
                if customer == cust.name:
                    cust.add_order(order2)
            file_orders.append(order2)
        if line[0] == "WAREHOUSE":
            warehouse, name, product, quantity = line
            quantity = int(quantity)
            if name not in all_warehouse:
                all_warehouse[name] = Warehouse(name)
            for prod in file_product_order:
                if product == prod.name:
                    all_warehouse[name].add_product(prod, quantity)

for order in file_orders:
    print("Заказ:", order.total_price())
for customer in file_customer_order:
    print(customer.name, customer.email)
for customer in file_customer_order:
    print(customer.name)

    for order in customer.product_order:
        print(order.total_price())

for name, warehouse in all_warehouse.items():
    print("Склад:", name)
    for product, quantity in warehouse.products.items():
        print(f"{product.name} На складе: {quantity}")
