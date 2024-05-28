import random
from ab_testing.models import UserAssignment, Variant, Experiment, db
from datetime import datetime

class AssignmentService:
    
    @staticmethod
    def get_user_variant(user_attributes, variants):
        for variant in variants:
            if user_attributes.get('device_type') == 'mobile' and variant.name == 'Mobile Variant':
                return variant.id
            if user_attributes.get('location') and variant.name == 'US Variant':
                return variant.id
        return None
    
    @staticmethod
    def assign_user_to_variant(user_id, experiment_id, user_attributes):
        variants = Variant.query.filter_by(experiment_id=experiment_id).all()
        
        assigned_variant_id = AssignmentService.get_user_variant(user_attributes, variants)
        
        if not assigned_variant_id:
            assigned_variant_id = random.choices(
                [variant.id for variant in variants],
                [variant.weight for variant in variants]
            )[0]

        assignment = UserAssignment(
            user_id=user_id,
            experiment_id=experiment_id,
            variant_id=assigned_variant_id,
            timestamp=datetime.utcnow()
        )
        db.session.add(assignment)
        db.session.commit()
        
        return assignment
