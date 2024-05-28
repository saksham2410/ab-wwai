def initialize_routes(app):
    from .experiments import experiment_bp
    from .variants import variant_bp
    from .user_assignments import user_assignment_bp
    from .interactions import interaction_bp
    from .users import user_bp
    
    app.register_blueprint(experiment_bp)
    app.register_blueprint(variant_bp)
    app.register_blueprint(user_assignment_bp)
    app.register_blueprint(interaction_bp)
    app.register_blueprint(user_bp)
