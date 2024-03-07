from flask import Flask
from flask_migrate import Migrate

from .models import User, Subscription
from .routes.main_routes import main_bp
# from config import DevConfig

migrate = Migrate()

def create_app():
    app = Flask(__name__)
  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

    # app.config.from_object(DevConfig)
    
    from .extensions import db
    db.init_app(app)
    
    migrate.init_app(app, db)

    reg_blueprints(app)

    return app

def reg_blueprints(app):
    app.register_blueprint(main_bp)
