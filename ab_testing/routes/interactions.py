from flask import Blueprint, request, jsonify
from ab_testing.models import Interaction, db
from datetime import datetime

interaction_bp = Blueprint('interactions', __name__)

@interaction_bp.route('/interactions', methods=['POST'])
def add_interaction():
    data = request.get_json()
    new_interaction = Interaction(
        user_id=data['user_id'],
        experiment_id=data['experiment_id'],
        variant_id=data['variant_id'],
        event_type=data['event_type'],
        details=data.get('details'),
        timestamp=datetime.utcnow()
    )
    db.session.add(new_interaction)
    db.session.commit()
    return jsonify({'message': 'Interaction recorded successfully'}), 201
