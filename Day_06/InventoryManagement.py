inventory = [
    {"name": "Apple 🍎", "quantity": 30, "price": 0.50},
    {"name": "Banana 🍌", "quantity": 20, "price": 0.20},
]


def add_product(name, quantity, price):  # Single Responsibility
    inventory.append({"name": name, "quantity": quantity, "price": price})


def update_product(product, quantity, price):  # Single Responsibility
    product["quantity"] += quantity
    product["price"] = price


product_name = input("What is the product name? ")
product_quantity = int(input("What is the quantity? "))
product_price = float(input("What is the price? "))

for product in inventory:
    if product_name == product["name"]:
        update_product(product, product_quantity, product_price)
        break
else:
    add_product(product_name, product_quantity, product_price)
    print(f"Added new product: {product_name}! 🎉")

print(f"Updated Inventory: {inventory}")
