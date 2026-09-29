#Handling
from data_manager import load_products, save_products

#products ={}
products = load_products()


def add_product():
    print("\n========== Add Product ==========")

    
    product_id = input("Enter product ID: ").strip()

    if product_id in products:
        print("Product ID already exists.")
        return



    name = input("Enter product name: ").strip()
    category = input("Enter product category: ").strip()

    cost_price = float(input("Enter cost price: "))
    selling_price = float(input("Enter selling price: "))
    marked_price = float(input("Enter marked price: "))

    stock_availability = int(input("Enter stock quantity: "))

    products[product_id] = {
    "name": name,
    "category": category,
    "cost_price": cost_price,
    "selling_price": selling_price,
    "marked_price": marked_price,
    "stock_availability": stock_availability
}
    save_products(products)

    print("product added successfully.")

def view_products():
    print("\n========== Product List ==========")

    if not products:
        print("No products available.")
        return
    print(
        f"{'ID' :<10}"
        f"{'Name' :<20}"
        f"{'Category' :<15}"
        f"{'Cost Price':>12}"
        f"{'Sell Price':>12}"
        f"{'Marked Price':>14}"
        f"{'Stock' :>8}"
    )

    print("_" *77)

    for product_id, product in products.items():
        print(
            f"{product_id :<10}"
            f"{product['name']:<20}"
            f"{product['category']:<15}"
            f"{product['cost_price']:>12.2f}"
            f"{product['selling_price']:>12.2f}"
            f"{product['marked_price']:>14.2f}"
            f"{product['stock_availability']:>8}"

        )


def search_product():
    print("\n========== SEARCH PRODUCT ==========")

    product_id = input("Enter product_ID: ").strip()

    if product_id in products:
        product = products[product_id]

        print("\nProduct Found")
        print("----------")
        print("Product ID  :", product_id)
        print("Name  :" , product["name"])
        print("Category :" ,product["category"])
        print("Cost Price :" ,product["cost_price"])
        print("Selling Price :" , product["selling_price"])
        print("Marked Price :", product["marked_price"])
        print("Stock :", product["stock_availability"])


    else:
        print("Product not found.")


def update_product():
    print("\n ========== UPDATE PRODUCT ==========")

    product_id = input("Enter product ID: ").strip()

    if product_id not in products:
        print("Product not Found.")
        return

    product = products[product_id]

    print("\nCurrent Product Details")
    print("Name :" , product["name"])
    print("Category :" , product["category"])
    print("Cost Price :" , product["cost_price"])
    print("Selling Price :" , product["selling_price"])
    print("Marked Price :" , product["marked_price"])
    print("Stock :" , product["stock_availability"])

    print("\nLeave input blank to keep the current value.")

    new_name = input("New name: ").strip()

    if new_name:
        product["name"] = new_name

    new_category = input("New category: ").strip()

    if new_category:
        product["category"] = new_category

    new_cost_price = input("New Cost Price: ").strip()

    if new_cost_price:
        product["cost_price"] = float(new_cost_price)

    new_selling_price = input("New Selling Price : ").strip()

    if new_selling_price:
        product["selling_price"] = float(new_selling_price)

    new_marked_price = input("New Marked Price : ").strip()

    if new_marked_price:
        product["marked_price"] = float(new_marked_price)

    new_stock = input("New stock quantity: ").strip()   

    if new_stock:
        product["stock_availability"] =  int(new_stock)

    save_products(products)

    print("Product updated successfully.")

def delete_product():
    print("\n ========== DELETE PRODUCT ==========")

    product_id = input("Enter product ID: ").strip()

    if product_id in products:
        del products[product_id]

        save_products(products)

        print("Product deleted successfully.")

    else:
        print("Product not Found")



def product_menu():
    while True:
        print("\n ========== PRODUCT MANAGEMENT ==========")
        print("1. Add Product")
        print("2. View Product")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please select 1-6.")