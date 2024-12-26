from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from routes.users import user_router  # Import the users blueprint
from routes.products import product_router  # Import the products blueprint

load_dotenv()

app = Flask(__name__)
CORS(app)

mongo_uri = os.getenv("MONGODB_URI") + os.getenv("MONGODB_LOG_DBNAME")
client = MongoClient(mongo_uri)
db = client.get_database()

app.register_blueprint(user_router, url_prefix='/api/users', strict_slashes=False)  # Prefix for user routes
app.register_blueprint(product_router, url_prefix='/api/products')

@app.route('/')
def home():
    return "E-Commerce with Flask & MongoDB!"

if __name__ == '__main__':
    app.run(port=5000)