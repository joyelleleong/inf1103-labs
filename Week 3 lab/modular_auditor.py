inventory = 0
deliveries = 0 
failed_entries = 0

def get_valid_input():
    while True:
        stock = input("Enter the stock quantity (or 'quit' to stop): ")

        if stock.lower() == 'quit':
            return 'quit' , False

        if not stock.isdigit():
            print("Error: Invalid input. Please enter a number.")
            return None, True

        stock = int(stock)

        if stock < 0:
            print("Error: Stock quantity cannot be negative.")
            failed_entries += 1
            return None, True

        return stock, False

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10

def generate_report(inventory, deliveries, failed_entries):
    print("Final inventory:", inventory)
    print("Number of deliveries:", deliveries)
    print("Number of failed entries:", failed_entries)

while True: 
    stock , failed = get_valid_input() 

    if stock == 'quit':
        break

    if failed:
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

generate_report(inventory, deliveries, failed_entries) 

