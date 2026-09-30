def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
            total = int(lines[0].strip())
            history = [int(line.strip()) for line in lines[1:]]
            return total, history
    except FileNotFoundError:
        return 0, []
    except ValueError:
        print("Error: Inventory file is corrupted. Starting with 0 inventory.")
        return 0, []

def save_inventory(total, history):
    with open("inventory.txt", "w") as file:
        file.write(str(total) + "\n")

        for transaction in history:
            file.write(str(transaction) + "\n")

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

inventory, transaction_history = load_inventory()
failed_entries = 0
deliveries = 0

print("Previous inventory:", inventory)
print("Previous transactions:", transaction_history)

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

    transaction_history.append(stock)

    print("Stock accepted")
    print("Current inventory:", inventory)
    print ("Tax for this delivery:", tax)


    if inventory > 500:
        print("ALERT: Overstock! Inventory exceeds 500 units.")
        break 

save_inventory(inventory, transaction_history)
print("Inventory saved successfully to inventory.txt.")
generate_report(inventory, deliveries, failed_entries) 

