inventory = 0
failed_entries = 0

while True: 
    stock = input("Enter the stock quantity (or 'quit' to stop): ")

    if stock.lower() == 'quit':
        break

    if not stock.isdigit():
        print("Error:Invalid input. Please enter a number.")
        failed_entries += 1
        continue

    stock =int(stock)

    if stock < 0:
        print("Error: Stock quantity cannot be negative.")
        failed_entries += 1
        continue

    inventory += stock
    print("Stock accepted")
    print("Current inventory:", inventory)

    if inventory > 500:
        print("ALERT: Overstock! Inventory exceeds 500 units.")
        break 

print ("Final inventory:", inventory)
print("Number of failed entries:", failed_entries)
