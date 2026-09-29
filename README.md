# Business Data Handling System

## 1. Project Description

Business Data Handling System is a command-line program Python application designed to manage basic business operations

The system allows users to manage products, inventory, billing, sales records, and business reports

The application uses Json files to store product and sales information.

---

## 2. Features

### Product Management

- Add new products 
- View all products
- Search for products
- update product information 
- Delete products

### Inventory Management

- View available stock
- Add stock
- Remove stock
- Check low-stock products

### Billing

- Create customer bills
- knowing Buyer information
- Total Bill Amount
- automatic reduce stock after sold out
- store completed sales records

### Sales Managememt

- View Sales Records 
- Search Sales by buyer name
- calculate sale summary
- Display total revenue

### Reports
- Generate sales , inventory, low-stock, reports

### Data Storage

- About Product , sales , data_managememt

# How the data is saved

whenever a product is added , updated , deleted  or sold, the program writes the whole list back to the json file.

##### Project Structure

BusinessDataHandling
├──main.py
├──product_manager.py
├──inventory_manager.py
├──billing_manager.py
├──sales_manager.py
├──reports_manager.py
├──data_manager.py
├──products.json
├──sales.json
├──README.md
└── .gitignore
