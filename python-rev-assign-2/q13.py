#Q13

menu = {"burger": 8.99, "pizza": 12.50, "salad": 7.25, "fries": 3.50}

item = input("Enter an item name: ").lower()


if item in menu:
    print(f"{item.capitalize()} costs ${menu[item]}")
else:
    print("Sorry, we don't have that item")