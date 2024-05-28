from ab_testing.models import Variant, db

class VariantService:
    
    @staticmethod
    def create_variant(experiment_id, name, description, weight):
        new_variant = Variant(
            experiment_id=experiment_id,
            name=name,
            description=description,
            weight=weight
        )
        db.session.add(new_variant)
        db.session.commit()
        return new_variant

    @staticmethod
    def get_variants_by_experiment(experiment_id):
        return Variant.query.filter_by(experiment_id=experiment_id).all()

    @staticmethod
    def update_variant_weights(experiment_id, weights):
        variants = Variant.query.filter_by(experiment_id=experiment_id).all()
        for variant in variants:
            if variant.id in weights:
                variant.weight = weights[variant.id]
        db.session.commit()
        return variants
