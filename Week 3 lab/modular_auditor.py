inventory = 0
deliveries = 0 
failed_entries = 0

def get_valid_input():
    while True:
        stock = input("Enter the stock quantity (or 'quit' to stop): ")

        if stock.lower() == 'quit':
            return 'quit'

        if not stock.isdigit():
            print("Error: Invalid input. Please enter a number.")
            continue

        stock = int(stock)

        if stock < 0:
            print("Error: Stock quantity cannot be negative.")
            continue

        return stock

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10

def generate_report(inventory, failed_entries):
    print("Final inventory:", inventory)
    print("Number of failed entries:", failed_entries)

while True: 
    stock = get_valid_input() 

    if stock == 'quit':
        break

    if stock is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, stock)
    tax = calculate_tax(stock)
    deliveries += 1

    print("Stock accepted")
    print("Current inventory:", inventory)
    print ("Tax for this delivery:", tax)


    if inventory > 500:
        print("ALERT: Overstock! Inventory exceeds 500 units.")
        break 

generate_report(inventory, failed_entries) 

