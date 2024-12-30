import tkinter as tk
from tkinter import messagebox
from menu import view_menu
from customers import add_customer
from orders import place_order
from reports import view_all_customers, view_order_details, view_total_sales

def show_menu():
    view_menu()
    messagebox.showinfo("Info", "Menu displayed in the console.")

def add_new_customer():
    add_customer()
    messagebox.showinfo("Info", "Customer added successfully!")

def place_new_order():
    place_order()
    messagebox.showinfo("Info", "Order placed successfully!")

def show_all_customers():
    view_all_customers()
    messagebox.showinfo("Info", "Customers displayed in the console.")

def show_order_details():
    view_order_details()
    messagebox.showinfo("Info", "Order details displayed in the console.")

def show_total_sales():
    view_total_sales()
    messagebox.showinfo("Info", "Total sales displayed in the console.")

# GUI Layout
root = tk.Tk()
root.title("Online Food Ordering System")
root.geometry("400x400")

tk.Label(root, text="Online Food Ordering System", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="View Menu", command=show_menu, width=20).pack(pady=5)
tk.Button(root, text="Add Customer", command=add_new_customer, width=20).pack(pady=5)
tk.Button(root, text="Place Order", command=place_new_order, width=20).pack(pady=5)
tk.Button(root, text="View All Customers", command=show_all_customers, width=20).pack(pady=5)
tk.Button(root, text="View Order Details", command=show_order_details, width=20).pack(pady=5)
tk.Button(root, text="View Total Sales", command=show_total_sales, width=20).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, width=20).pack(pady=20)

root.mainloop()
