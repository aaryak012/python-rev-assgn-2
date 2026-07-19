#Q20
def process_data(items):
    total = 0
    for item in items:
                print(f"{item['name']}: {item['quantity']}")
    total += item['quantity']

    print(f"Total items in stock: {total}")


items = [
    {"name": "Widget", "quantity": 5},
    {"name": "Gadget", "quantity": 8},
    {"name": "Doohickey", "quantity": 12}
]

process_data(items)