#Handles business reports.

from product_manager import products
from billing_manager import sales_record

def sales_report():
    print("\n========== SALES REPORT ==========")

    if not sales_record:
        print("No sales records available")
        return

    total_revenue = 0
    total_items = 0

    for sale in sales_record:
        total_revenue = total_revenue + sale['total_amount']
        total_items = total_items + sale['quantity']


    print("Number of sales :", len(sales_record))
    print("Total Items Sold :", total_items)
    print("Total Revenue :", total_revenue)


def inventory_report():
    print("\n========== INVENTORY REPORT ==========")

    if not products:
        print("No products available")
        return

    
    total_products = len(products)
    total_stock = 0

    for product in products.values():
        total_stock = total_stock + product['stock_availability']

    print("Total Products :", total_products)
    print("Total Stock :", total_stock)

def low_stock_report():
    print("\n========= LOW STOCK REPORT ==========")


    if not products:
        print("No products available.")
        return


    found = False

    for product_id, product in products.items():

        if product["stock_availability"] <=5:
            print(
                "Product ID:",
                product_id,
                "Name :",
                product["name"],
                "Stock :",
                product["stock_availability"]

            )

            found = True



    if not found:
        print("No products have low stock.")


def reports_menu():
    while True:
        print("\n========== REPORTS ==========")
        print("1. Sales Report")
        print("2. Inventory Report")
        print("3. Low Stock Report")
        print('4. Back to main menu')

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            sales_report()

        elif choice =="2":
            inventory_report()

        elif choice =="3":
            low_stock_report()

        elif choice == "4":
            break

        else:
            print("Invalid choice. please select 1-4")



