#Business Data
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

PRODUCT_FILE = BASE_DIR / "products.json"
SALES_FILE = BASE_DIR / "sales.json"


def load_products():
    try:
        with open(PRODUCT_FILE, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return{}



def save_products(products):  
        with open(PRODUCT_FILE, "w") as file:
            json.dump(products,file, indent =4)


def load_sales():
    try:
          with open(SALES_FILE, "r") as file:
               return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_sales(sales_record):
     with open(SALES_FILE, "w") as file:
          json.dump(sales_record, file, indent =4)
