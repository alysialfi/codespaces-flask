from pymongo import MongoClient
import os

# MongoDB connection setup
mongo_uri = os.getenv("MONGODB_URI") + os.getenv("MONGODB_LOG_DBNAME")
client = MongoClient(mongo_uri)
db = client.get_database()

# Define the Users collection
users_collection = db.users

# Helper functions for interacting with the 'users' collection

# Function to create a new user
def create_user(name, email, password):
    user_data = {
        "name": name,
        "email": email,
        "password": password
    }
    result = users_collection.insert_one(user_data)
    return str(result.inserted_id)

# Function to find a user by email
def get_user_by_email(email):
    return users_collection.find_one({"email": email})

# Function to get all users
def get_all_users():
    users = list(users_collection.find())
    for user in users:
        user['_id'] = str(user['_id'])  # Convert ObjectId to string
    return users

# Function to update user information
def update_user(user_id, update_data):
    return users_collection.update_one({"_id": user_id}, {"$set": update_data})

# Function to delete a user by ID
def delete_user(user_id):
    return users_collection.delete_one({"_id": user_id})
