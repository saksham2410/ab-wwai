from flask import Blueprint, request, jsonify
from ab_testing.services.variant_service import VariantService

variant_bp = Blueprint('variants', __name__)

@variant_bp.route('/variants', methods=['POST'])
def add_variant():
    data = request.get_json()
    new_variant = VariantService.create_variant(
        experiment_id=data['experiment_id'],
        name=data['name'],
        description=data.get('description'),
        weight=data['weight']
    )
    return jsonify({
        'message': 'Variant created successfully',
        'variant': {
            'id': new_variant.id,
            'experiment_id': new_variant.experiment_id,
            'name': new_variant.name,
            'description': new_variant.description,
            'weight': new_variant.weight
        }
    }), 201

@variant_bp.route('/variants/<int:experiment_id>', methods=['GET'])
def get_variants(experiment_id):
    variants = VariantService.get_variants_by_experiment(experiment_id)
    return jsonify([{
        'id': var.id,
        'name': var.name,
        'description': var.description,
        'weight': var.weight
    } for var in variants]), 200

@variant_bp.route('/variants/weights', methods=['PUT'])
def update_variant_weights():
    data = request.get_json()
    experiment_id = data['experiment_id']
    weights = data['weights']
    updated_variants = VariantService.update_variant_weights(experiment_id, weights)
    return jsonify([{
        'id': var.id,
        'name': var.name,
        'description': var.description,
        'weight': var.weight
    } for var in updated_variants]), 200
