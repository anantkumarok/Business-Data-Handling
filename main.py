from product_manager import product_menu
from inventory_manager import inventory_menu
from billing_manager import billing_menu
from sales_manager import sales_menu
from reports_manager import reports_menu


def main():
    while True:
        print("\n=================================")
        print("BUSINESS DATA HANDLING SYSTEM ")
        print("=================================")
        print("1. Product Management")
        print("2. Inventory Management")
        print("3. Billing")
        print("4. Sales")
        print("5. Reports")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            product_menu()
            #print("\nProduct Management Selected")

        elif choice == "2":
            inventory_menu()
            #print("\nInventory Management Selected.")

        elif choice == "3":
            billing_menu()
            #print("\nBilling Selected.")

        elif choice == "4":
            sales_menu()
            #print("\nSales Selected.")

        elif choice == "5":
            reports_menu()
            #print("\nReports Selected.")

        elif choice == "6":
            print("\nThank you for using Business Data Handling System. ")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 6. ")

if __name__ == "__main__" :
    main()
