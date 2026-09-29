# Handles sales- related operations.

from billing_manager import sales_record


def view_sales():
    print("\n========== SALES RECORDS ==========")

    if not sales_record:
        print("No sales records available.")
        return

    count = 0

    for sale in sales_record:
        count = count + 1

        print("\nSale",count)
        print("--------------------------------")


        print("Buyer Name :" , sale['buyer_name'])
        print("Phone Number :" , sale['phone_number'])
        print("Address :", sale['address'])
        print("Product :",sale['product_name'])
        print("Selling Price :", sale['selling_price'])
        print("Quantity :", sale['quantity'])
        print("total Amount :", sale['Total_Amount'])


def search_sales():
    print("\n ========== SEARCH SALES ==========")

    buyer_name = input("Enter buyer name: ").strip().lower()

    found = False
    count = 0

    for sale in sales_record:
        count = count + 1

        if buyer_name in sale["buyer_name"].lower():

            print("\nSale", count)
            print('--------------------------------')

            print("Buyer Name :", sale['buyer_name'])
            print("Phone Number :", sale['phone_number'])
            print("Address :", sale['address'])
            print("Product :", sale['product_name'])
            print("Quantity :", sale['quantity'])
            print("Total Amount :", sale['total_amount'])

            found = True

    if not found:
            print("No sales found for this buyer.")


def sales_summary():
        print("\n========== SALES SUMMARY ==========")

        if not sales_record:
            print("No sales records available.")
            return

        total_amount = 0
        total_items = 0

        for sale in sales_record:
            total_amount += sale['total_amount']
            total_items += sale['quantity']


        print("Number of sales :", len(sales_record))
        print("Items sold :", total_items)
        print("Total revenue :", total_amount)


def sales_menu():
    while True:
        print("\n========= SALES MANAGEMENT ==========")
        print("1. View Sales")
        print("2. Search Sales")
        print("3. Sales Summary")
        print("4. Back to main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_sales()

        elif choice == "2":
            search_sales()

        elif choice == "3":
            sales_summary()

        elif choice =="4":
            break

        else:
            print("Invalid choice. PLease select 1-4.")




