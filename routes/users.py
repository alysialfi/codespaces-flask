from flask import Blueprint, request, jsonify
from models.user import create_user, get_all_users, update_user, delete_user, get_user_by_email

# Create a blueprint for user routes
user_router = Blueprint('users', __name__)

# Route to update user
@user_router.route('/', methods=['PUT'])
def update_user_route():
    try:
        # Get user data from request body
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            return jsonify({"message": "Name and email are required."}), 400

        # Update user in the database
        filter_ = {"name": name}
        update_data = {"email": email}
        result = update_user(filter_, update_data)

        if result.modified_count > 0:
            return jsonify({"message": "User updated successfully."}), 200
        else:
            return jsonify({"message": "User not found or no changes were made."}), 404

    except Exception as error:
        return jsonify({"message": "Error updating user.", "error": str(error)}), 500


# Route to get all users
@user_router.route('/', methods=['GET'])
@user_router.route('/<path:subpath>', methods=['GET']) 
def get_users():
    try:
        users = get_all_users()
        return jsonify(users), 200
    except Exception as error:
        return jsonify({"message": "Error fetching users", "error": str(error)}), 500


# Route to delete a user
@user_router.route('/', methods=['DELETE'])
def delete_user_route():
    try:
        # Get user data from request body
        data = request.get_json()
        name = data.get('name')

        if not name:
            return jsonify({"message": "Name is required to delete a user."}), 400

        # Delete user from the database
        result = delete_user(name)

        if result.deleted_count > 0:
            return jsonify({"message": "User deleted successfully."}), 200
        else:
            return jsonify({"message": "User not found."}), 404

    except Exception as error:
        return jsonify({"message": "Error deleting user.", "error": str(error)}), 500
