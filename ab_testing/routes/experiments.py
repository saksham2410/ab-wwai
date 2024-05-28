from flask import Blueprint, request, jsonify
from ab_testing.services.experiment_service import ExperimentService
from datetime import datetime

experiment_bp = Blueprint('experiments', __name__)

@experiment_bp.route('/experiments', methods=['POST'])
def add_experiment():
    data = request.get_json()
    new_experiment = ExperimentService.create_experiment(
        name=data['name'],
        description=data.get('description'),
        start_date=datetime.strptime(data['start_date'], '%Y-%m-%d %H:%M:%S'),
        end_date=datetime.strptime(data['end_date'], '%Y-%m-%d %H:%M:%S'),
        status=data['status']
    )
    return jsonify({
        'message': 'Experiment created successfully',
        'experiment': {
            'id': new_experiment.id,
            'name': new_experiment.name,
            'description': new_experiment.description,
            'start_date': new_experiment.start_date,
            'end_date': new_experiment.end_date,
            'status': new_experiment.status
        }
    }), 201

@experiment_bp.route('/experiments', methods=['GET'])
def get_experiments():
    experiments = ExperimentService.get_all_experiments()
    return jsonify([{
        'id': exp.id,
        'name': exp.name,
        'description': exp.description,
        'start_date': exp.start_date,
        'end_date': exp.end_date,
        'status': exp.status
    } for exp in experiments]), 200
