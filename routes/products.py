from flask import Blueprint, request, jsonify
from models.product import create_product, get_all_products, update_product, delete_product

# Create a blueprint for product routes
product_router = Blueprint('products', __name__)

# Route to update product
@product_router.route('/', methods=['PUT'])
def update_product_route():
    try:
        # Get product data from request body
        data = request.get_json()
        name = data.get('name')
        price = data.get('price')

        if not name or not price:
            return jsonify({"message": "Product name and price are required."}), 400

        # Update product in the database
        filter_ = {"name": name}
        update_data = {"price": price}
        result = update_product(filter_, update_data)

        if result.modified_count > 0:
            return jsonify({"message": "Product updated successfully."}), 200
        else:
            return jsonify({"message": "Product not found or no changes were made."}), 404

    except Exception as error:
        return jsonify({"message": "Error updating product.", "error": str(error)}), 500


# Route to get all products
@product_router.route('/', methods=['GET'])
def get_products():
    try:
        products = get_all_products()
        return jsonify(products), 200
    except Exception as error:
        return jsonify({"message": "Error fetching products", "error": str(error)}), 500


# Route to delete a product
@product_router.route('/', methods=['DELETE'])
def delete_product_route():
    try:
        # Get product data from request body
        data = request.get_json()
        name = data.get('name')

        if not name:
            return jsonify({"message": "Name is required to delete a product."}), 400

        # Delete product from the database
        result = delete_product(name)

        if result.deleted_count > 0:
            return jsonify({"message": "Product deleted successfully."}), 200
        else:
            return jsonify({"message": "Product not found."}), 404

    except Exception as error:
        return jsonify({"message": "Error deleting product.", "error": str(error)}), 500
