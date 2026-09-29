# Handles billing-related operations.

from product_manager import products
from data_manager import load_sales,save_sales,save_products


#Stores completed sales
#sales_record = []
sales_record = load_sales()

def create_bill():
    print("\n========== CREATE BILL ==========")

    if not products:
        print("No products available.")
        return


    #Buyer_details
    buyer_name = input("Enter buyer name: ").strip()
    phone_number = input("Enter your phone number: ").strip()
    address = input("Enter buyer address: ").strip()

    product_id = input("Enter product ID: ").strip()

    if product_id not in products:
        print("Product not found")
        return

    product = products[product_id]


    print("\nProduct Details")
    print("----------")
    print("Name :", product["name"])
    print("Selling Price :", product["selling_price"])
    print("Available :" , product["stock_availability"])

    quantity = input("Enter quantity: ").strip()

    try:
        quantity = int(quantity)

        if quantity <= 0:
            print("Quantity  must be greater than zero.")
            return

        if quantity > product["stock_availability"]:
            print("Insufficient stock.")
            return

        total = product["selling_price"] * quantity

        #Reduce Stock
        product["stock_availability"] -= quantity
        save_products(products)

        #Create sales record
        sales = {
            "buyer_name": buyer_name,
            "phone_number": phone_number,
            "address": address,
            "product_id": product_id,
            "product_name": product["name"],
            "selling_price": product["selling_price"],
            "quantity": quantity,
            "total_amount": total
        }


        sales_record.append(sales)
        save_sales(sales_record)

        #Display bill
        print("\n========== Bill ==========")

        print("Buyer Name :", buyer_name)
        print("phone Number :", phone_number)
        print("Address :", address)

        print("----------")

        print("Product :", product["name"])
        print("price :", product["selling_price"])
        print("Quantity :",quantity)
        print("Total Amount :", total)

        print("==========")
        print("Stock updated successfully.")
        print("Remaining Stock :",product["stock_availability"])

    except ValueError:
        print("Please enter a valid whole number.")

def view_sales():
    print('\n========== SALES RECORDS ==========')

    if not sales_record:
        print("No sales records available.")
        return

    for number, sale in enumerate(sales_record, start = 1):

        print("\nSale", number)
        print("----------")

        print("Buyer Name :", sale["buyer_name"])
        print("Phone Number :", sale["phone_number"])
        print("address :", sale["address"])

        print("Product :", sale["product_name"])
        print("Selling Price :", sale["selling_price"])
        print("Quantity :" , sale["quantity"])
        print("Total Amount :", sale["total_amount"])


def billing_menu():
    while True:
        print("\n=========== BILLING MANAGEMENT ==========")
        print("1. Create Bill")
        print("2. View Sales Records")
        print("3. Back to main Menu")

        choice = input("Enter your choice:").strip()

        if choice == "1":
            create_bill()

        elif choice == "2":
            view_sales()

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please select 1-3.")

