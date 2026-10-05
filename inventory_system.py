
inventory = {
    "PROD_01": {
        "name": "wireless keyboard",
        "price": 45.00,
        "stock": 15
    },
    "PROD_02": {
        "name": "gaming mouse",
        "price": 25.50,
        "stock": 3
    }
}


def process_order(product_code, quantity):

    
    if product_code not in inventory:
        print("Error: Product not found.")
        return 0.0

    product = inventory[product_code]

    
    if quantity <= product["stock"]:

        
        total_cost = product["price"] * quantity

        
        product["stock"] -= quantity

        print("Order processed successfully.")

        return total_cost

    else:
        print("Error: Not enough stock.")
        return 0.0



apply_tax = lambda subtotal: subtotal * 0.075


def generate_receipt(cart_items):

    subtotal = 0

    print("\n----- RECEIPT -----")

    for product_code, quantity in cart_items:

        
        cost = process_order(product_code, quantity)

        if cost > 0:
            product_name = inventory[product_code]["name"]

            print(f"{product_name}: {quantity} x "
                  f"${inventory[product_code]['price']:.2f} = ${cost:.2f}")

            subtotal += cost

    
    tax = apply_tax(subtotal)

    
    total = subtotal + tax

    print("-------------------")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (7.5%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")



cart = [
    ("PROD_01", 2),
    ("PROD_02", 1)
]

generate_receipt(cart)




promotional_items = {
    "PROD_01",
    "PROD_03"
}

warehouse_stock = {
    "PROD_01",
    "PROD_02",
    "PROD_04"
}



both_categories = promotional_items & warehouse_stock

print("\nItems in both categories:")
print(both_categories)



not_on_promotion = warehouse_stock - promotional_items

print("\nWarehouse items not on promotion:")
print(not_on_promotion)