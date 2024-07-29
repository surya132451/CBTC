
def print_receipt(items):
    print("\n" + "=" * 40)
    print("         MARS SHOWROOM PAYMENT RECEIPT")
    print("=" * 40)
    print("{:<20} {:>10} {:>5}".format("Item", "Price", "Qty"))
    print("-" * 40)

    total = 0
    for item, details in items.items():
        price, qty = details
        total += price * qty
        print("{:<20} {:>10.2f} {:>5}".format(item, price, qty))

    print("-" * 40)
    print("{:<20} {:>10} {:>5}".format("Total", "", total))
    print("=" * 40)

def get_items():
    items = {}
    while True:
        item_name = input("Enter item name (or 'done' to finish): ").strip()
        if item_name.lower() == 'done':
            break
        try:
            price = float(input(f"Enter price for {item_name}: "))
            qty = int(input(f"Enter quantity for {item_name}: "))
            items[item_name] = (price, qty)
        except ValueError:
            print("Invalid input. Please enter numeric values for price and quantity.")

    return items

def main():
    print("BILLING PAGE!")
    date = input("Enter the date (DD/MM/YYYY): ")
    items = get_items()

    if items:
        print(f"\nDate: {date}")
        print_receipt(items)
    else:
        print("No items to generate a receipt.")

if __name__ == "__main__":
    main()
