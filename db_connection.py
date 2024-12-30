import mysql.connector

def get_connection():
    """Establish a connection to the database."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",  
        database="online_food_ordering"
    )
