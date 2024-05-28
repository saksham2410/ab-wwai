from flask import Blueprint, request, jsonify
from ab_testing.services.user_assignment_service import AssignmentService
from ab_testing.services.user_service import UserService

user_assignment_bp = Blueprint('user_assignments', __name__)

@user_assignment_bp.route('/assign', methods=['POST'])
def assign_user():
    data = request.get_json()
    hashed_id = data['hashed_id']
    experiment_id = data['experiment_id']
    user_attributes = data['attributes']
    
    user = UserService.get_user_by_hashed_id(hashed_id)
    if not user:
        user = UserService.create_user(hashed_id, user_attributes)
    
    assignment = AssignmentService.assign_user_to_variant(user.id, experiment_id, user_attributes)
    
    return jsonify({
        'message': 'User assigned to variant successfully',
        'assignment': {
            'user_id': assignment.user_id,
            'experiment_id': assignment.experiment_id,
            'variant_id': assignment.variant_id,
            'timestamp': assignment.timestamp
        }
    }), 201
