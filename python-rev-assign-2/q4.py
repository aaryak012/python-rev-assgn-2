#Q4
products = [
    {"name": "Laptop", "price": 800},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 60}
]
for product in products:
        print(f"{product['name']} costs ${product['price']}")