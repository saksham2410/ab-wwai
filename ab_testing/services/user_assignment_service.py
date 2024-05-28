import random
from ab_testing.models import UserAssignment, Variant, Experiment, db
from datetime import datetime

class AssignmentService:
    
    @staticmethod
    def get_user_variant(user_attributes):
        if user_attributes.get('device_type') == 'mobile':
            return 'Mobile Variant'
        elif user_attributes.get('location') == 'US':
            return 'US Variant'
        else:
            return 'Default Variant'
    
    @staticmethod
    def assign_user_to_variant(user_id, experiment_id, user_attributes):
        variants = Variant.query.filter_by(experiment_id=experiment_id).all()
        
        assigned_variant = AssignmentService.get_user_variant(user_attributes)
        
        if not assigned_variant:
            assigned_variant = random.choices(
                [variant.id for variant in variants],
                [variant.weight for variant in variants]
            )[0]

        assignment = UserAssignment(
            user_id=user_id,
            experiment_id=experiment_id,
            variant_id=assigned_variant,
            timestamp=datetime.utcnow()
        )
        db.session.add(assignment)
        db.session.commit()
        
        return assignment
