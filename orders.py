from db_connection import get_connection
from menu import view_menu

def place_order():
    """Place an order."""
    connection = get_connection()
    cursor = connection.cursor()

    view_menu()
    customer_id = int(input("Enter Customer ID: "))
    total_amount = 0
    order_items = []

    while True:
        item_id = int(input("Enter Item ID to add to order othrwise enter 0 : "))
        if item_id == 0:
            break
        quantity = int(input("Enter Quantity : "))
        query = "SELECT price FROM food_items WHERE item_id = %s"
        cursor.execute(query, (item_id,))
        price = cursor.fetchone()[0]
        total_amount += price * quantity
        order_items.append((item_id, quantity))

    # Insert Order
    query = "INSERT INTO orders (customer_id, total_amount) VALUES (%s, %s)"
    cursor.execute(query, (customer_id, total_amount))
    order_id = cursor.lastrowid

    # Insert Order Items
    for item_id, quantity in order_items:
        query = "INSERT INTO order_items (order_id, item_id, quantity) VALUES (%s, %s, %s)"
        cursor.execute(query, (order_id, item_id, quantity))
    
    connection.commit()
    print(f"Order placed successfully!!! Order ID: {order_id}")

    cursor.close()
    connection.close()
