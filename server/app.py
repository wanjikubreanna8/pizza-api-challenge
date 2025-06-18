from flask import Flask
from flask_migrate import Migrate
from server.models import db
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

def create_app():
    app = Flask(__name__)
    
    # Config - using SQLite here, change if you want
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurant.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)

    # Register Blueprints (Controllers)
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)

    return app
