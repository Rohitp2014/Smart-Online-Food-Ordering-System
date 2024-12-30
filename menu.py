from db_connection import get_connection

def view_menu():
    """Display the menu."""
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM food_items"
    cursor.execute(query)
    results = cursor.fetchall()

    print("\n--- Menu ---")
    for item in results:
        availability = "Available" if item[4] else "Not Available"
        print(f"ID: {item[0]} | Name: {item[1]} | Category: {item[2]} | Price: {item[3]} | {availability}")

    cursor.close()
    connection.close()
