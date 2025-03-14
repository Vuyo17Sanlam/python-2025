from datetime import datetime

items = [
    {"name": "Widget A", "quantity": 10, "price": 2.5},
    {"name": "Widget B", "quantity": 5, "price": 15.75},
    {"name": "Gadget", "quantity": 2, "price": 99.99},
]


def print_invoice(invoice_date, items):
    total = sum(item["quantity"] * item["price"] for item in items)
    invoice = f"Invoice Date: {invoice_date: %d %B %Y}\n\n"
    invoice += f"{'product':<20} {'Qty':>6} {'Unit Price':>15} {'Total':>10}\n"
    invoice += "-" * 54 + "\n"
    for item in items:
        name, qty, price = item["name"], item["quantity"], item["price"]
        invoice += f"{name:<20} {qty:>6} {price:>15.2f} {qty * price:>10.2f}\n"
    invoice += "-" * 54 + "\n"
    invoice += f"Grand Total {total:>42.2f}"
    return invoice


print(print_invoice(datetime.now(), items))
