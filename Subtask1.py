# Name: Nicola
# Surname: Phiri
# Date: 20/02/2025
# Project: Problem-Solving in Programming Subtask 1
# Purpose: Adding stock, Customer order, and low-stock notification

arrival_quantity = int(input("Please enter the shipments that have arrived:" + " "))
if arrival_quantity < 5 or arrival_quantity > 50:
    print("The shipments you have entered are not within the correct shipment order range." + " ")
    exit()
else:
    # ask for customer order
    customer_order = int(input("Please enter how much stock the customer ordered: "))
    #creating a condition for the customer order
    if customer_order in range (0,11):
        print("The customer has ordered" + " " + str(customer_order) + " " + "kits")
    else 
        print("Please enter a number between 1 and 10")


def adding_stock():
    global arrival_quantity, customer_order
    current_stock_level = arrival_quantity  # Stock starts with the shipment received
    print(f"The current stock level after shipment arrival: {current_stock_level}")
    # Insufficient stock alert
    if customer_order > current_stock_level:
        print("This order cannot be processed due to insufficient stock.")
    else:
        current_stock_level = current_stock_level - customer_order  # Deduct ordered stock
    print(f"The current stock level after a customer has ordered: {current_stock_level}")

    # Low stock notice
    if current_stock_level < 10:
        print("Please order more kits.")

# Call function


adding_stock()
