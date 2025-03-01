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
    print("The customer has ordered" + " " + str(customer_order) + " " + "kits")


def adding_stock():
    global arrival_quantity, customer_order
    current_stock_level = arrival_quantity  # Stock starts with the shipment received
    print(f"The current stock level after shipment arrival: {current_stock_level}")
    if customer_order > current_stock_level:
        print("There is not enough stock to complete this order.")
    else:
        current_stock_level = current_stock_level - customer_order  # Deduct ordered stock
    print(f"The current stock level after a customer has ordered: {current_stock_level}")

    # Low stock notice
    if current_stock_level < 10:
        print("Please reorder more kits.")
# Call function


adding_stock()
