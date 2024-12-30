from db_connection import get_connection

def add_customer():
    """Add a new customer."""
    connection = get_connection()
    cursor = connection.cursor()

    name = input("Enter Customer Name : ")
    phone = input("Enter Phone Number : ")
    address = input("Enter Customer Address : ")

    try:
        query = "INSERT INTO customers (name, phone, address) VALUES (%s, %s, %s)"
        values = (name, phone, address)
        cursor.execute(query, values)
        connection.commit()
        print("Customer added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    cursor.close()
    connection.close()
