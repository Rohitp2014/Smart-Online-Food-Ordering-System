from menu import view_menu
from customers import add_customer
from orders import place_order
from reports import view_all_customers, view_order_details, view_total_sales

def main():
    while True:
        print("\n--- Online Food Ordering System ---")
        print("1. View Menu")
        print("2. Add Customer")
        print("3. Place Order")
        print("4. View All Customers")    # New feature
        print("5. View Order Details")    # New feature
        print("6. View Total Sales")      # New feature
        print("0. Exit")                  # Changed exit option to 0 for consistency
        choice = input("Enter your choice : ")

        if choice == "1":
            view_menu()
        elif choice == "2":
            add_customer()
        elif choice == "3":
            place_order()
        elif choice == "4":
            view_all_customers()
        elif choice == "5":
            view_order_details()
        elif choice == "6":
            view_total_sales()
        elif choice == "0":
            print("Thank You, Visit Again !!!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
