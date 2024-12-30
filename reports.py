from db_connection import get_connection

def view_all_customers():
    """Display all customers."""
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
        
        if not customers:
            print("No customers found.")
            return

        print("\n--- Customers Report ---")
        for customer in customers:
            print(f"ID: {customer[0]} | Name: {customer[1]} | Phone: {customer[2]} | Address: {customer[3]}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()


def view_order_details():
    """Display all orders with their items."""
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT 
                o.order_id, c.name AS customer_name, o.total_amount, o.order_date
            FROM orders o
            JOIN customers c ON o.customer_id = c.customer_id
        """)
        orders = cursor.fetchall()
        
        if not orders:
            print("No orders found.")
            return

        print("\n--- Orders Report ---")
        for order in orders:
            print(f"\nOrder ID: {order[0]} | Customer: {order[1]} | Total: {order[2]} | Date: {order[3]}")
            
            # Fetch items for this order
            cursor.execute("""
                SELECT fi.name, oi.quantity, (oi.quantity * fi.price) AS total_price
                FROM order_items oi
                JOIN food_items fi ON oi.item_id = fi.item_id
                WHERE oi.order_id = %s
            """, (order[0],))
            items = cursor.fetchall()

            print("  Items:")
            for item in items:
                print(f"    - {item[0]} | Quantity: {item[1]} | Total: {item[2]}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()


def view_total_sales():
    """Display the total sales amount."""
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT SUM(total_amount) FROM orders")
        total_sales = cursor.fetchone()[0] or 0.0
        print(f"\n---- Total Sales ----")
        print(f"Total Sales Amount : {total_sales}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()
