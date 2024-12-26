from pymongo import MongoClient
import os

# MongoDB connection setup
mongo_uri = os.getenv("MONGODB_URI") + os.getenv("MONGODB_LOG_DBNAME")
client = MongoClient(mongo_uri)
db = client.get_database()

# Define the Products collection
products_collection = db.products

# Helper functions for interacting with the 'products' collection

# Function to create a new product
def create_product(name, price, desc, stock, category_id):
    product_data = {
        "name": name,
        "price": price,  # In Python, we'll store price as a float
        "desc": desc,
        "stock": stock,
        "category_id": category_id  # You would need to handle category_id as an ObjectId if needed
    }
    result = products_collection.insert_one(product_data)
    return str(result.inserted_id)

# Function to get a product by ID
def get_product_by_id(product_id):
    return products_collection.find_one({"_id": product_id})

# Function to get all products
def get_all_products():
    return list(products_collection.find())

# Function to update product information
def update_product(product_id, update_data):
    return products_collection.update_one({"_id": product_id}, {"$set": update_data})

# Function to delete a product by ID
def delete_product(product_id):
    return products_collection.delete_one({"_id": product_id})
