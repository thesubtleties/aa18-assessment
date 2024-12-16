from .simple import simple_bp

def register_blueprints(app):
    app.register_blueprint(simple_bp)