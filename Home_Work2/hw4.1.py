class Product:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def change_price(self, new_price):
        self.price = new_price

    def change_quantity(self, new_quantity):
        self.quantity = new_quantity


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


file_product_order = []
file_customer_order = []
file_orders = []
with open("shop.txt", "r") as file:
    for line in file:
        line = line.strip().split(";")
        if line[0] == "PRODUCT":
            product, name, category, price, quantity = line
            price = float(price)
            quantity = int(quantity)
            product4 = Product(name, price, quantity, category)
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

for order in file_orders:
    print("Заказ:", order.total_price())
for customer in file_customer_order:
    print(customer.name, customer.email)
for customer in file_customer_order:
    print(customer.name)

    for order in customer.product_order:
        print(order.total_price())
