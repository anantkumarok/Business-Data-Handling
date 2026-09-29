# Handles inventory_ related operations.

from product_manager import products
from data_manager import save_products

def view_stocks():
    print("\n ========== INVENTORY ==========")

    if not products:
        print("No products available.")
        return

    print(
        f"{'ID' :<10}"
        f"{'Name' :<20}"
        f"{'Category' :<15}"
        f"{'Stock' :>10}"
    )

    print("_" *55)

    for product_id, product in products.items():
        print(
            f"{product_id:<10}"
            f"{product['name']:<15}"
            f"{product['category']:<15}"
            f"{product['stock_availability'] :>10}"
        )


def add_stock():
    print("\n========== ADD STOCK ==========")

    product_id = input("Enter product ID: ").strip()

    if product_id not in products:
        print("Product not found.")
        return

    quantity = input ("Enter quantity to add: ").strip()

    try:
        quantity = int(quantity)

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        products[product_id]["stock_availability"] += quantity

        save_products(products)

        print("Stock added successfully.")
        print(
            "New Stock:",
            products[product_id]["stock_availability"]
        )


    except ValueError:
        print("Please enter a valid whole number.")


def remove_stock():
    print("\n========== REMOVE STOCK ==========")

    product_id = input("Enter product ID : ").strip()

    if product_id not in products:
        print("Product not found.")
        return

    quantity = input("Enter quantity to remove: ").strip()

    try:
        quantity = int(quantity)

        if quantity <= 0:
            print("Quantity must be grater than zero.")
            return

        current_stock = products[product_id]["stock_availability"]

        if quantity > current_stock:
            print("Insufficient stock.")
            return

        products[product_id]["stock_availability"] -=quantity

        save_products(products)

        print("stock removed successfully.")
        print(
            "Remaining stock: ",
            products[product_id]["stock_availability"]
        )


    except ValueError:
        print("Please enter a valid whole number.")


def low_stock():
    print("\n ========== LOW STOCK ==========")

    if not products:
        print("No products available.")
        return

    found = False

    for product_id, product in products.items():

        if product["stock_availability"] <=5:
            print(
       
                product_id,
                product["name"],
                "- Stocks:",
                product["stock_availability"]
            )
            found = True   


    if not found:
        print("No products have low stock.")


def inventory_menu():
    while True:
        print("\n========== INVENTORY MANAGEMENT ==========")
        print("1. View Stock")
        print("2. Add Stock")
        print("3. Remove Stock")
        print("4. Check Low Stock")
        print("5. Back to Main Menu")


        choice = input("Enter your choice: ").strip()

        if choice == "1" :
            view_stocks()

        elif choice == "2" :
            add_stock()

        elif choice == "3" :
            remove_stock()

        elif choice == "4" :
            low_stock()

        elif choice =="5" :
            break


        else:
            print("Invalid choice. Please select 1-5")
            
                                  