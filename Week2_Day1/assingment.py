from datetime import datetime

# List of invoice items
items = [
    {"name": "Widget A", "quantity": 10, "price": 2.5},
    {"name": "Widget B", "quantity": 5, "price": 15.75},
    {"name": "Gadget", "quantity": 2, "price": 99.99},
]


def print_invoice(invoice_date, items):
    # Print invoice date
    print(f"Invoice Date: {invoice_date}\n")

    # Print header
    print(f"{'Product':<20}{'Qty':<8}{'Unit Price':<15}{'Total':<10}")
    print("-" * 55)

    grand_total = 0  # Initialize grand total

    # Print each item
    for item in items:
        total = item["quantity"] * item["price"]
        grand_total += total
        print(
            f"{item['name']:<20}{item['quantity']:<8}{item['price']:<15.2f}{total:<10.2f}"
        )

    # Print footer
    print("-" * 55)
    print(f"{'Grand Total':>44}  {grand_total:.2f}")


# Call function with the given date
print_invoice(datetime.now(), items)
