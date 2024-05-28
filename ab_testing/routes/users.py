from flask import Blueprint, request, jsonify
from ab_testing.services.user_service import UserService

user_bp = Blueprint('users', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_id = data['hashed_id']
    attributes = data['attributes']
    
    user = UserService.create_user(hashed_id, attributes)
    
    return jsonify({
        'message': 'User created successfully',
        'user': {
            'id': user.id,
            'hashed_id': user.hashed_id,
            'attributes': user.attributes
        }
    }), 201

@user_bp.route('/users/<hashed_id>', methods=['GET'])
def get_user(hashed_id):
    user = UserService.get_user_by_hashed_id(hashed_id)
    if user:
        return jsonify({
            'id': user.id,
            'hashed_id': user.hashed_id,
            'attributes': user.attributes
        }), 200
    else:
        return jsonify({'message': 'User not found'}), 404
