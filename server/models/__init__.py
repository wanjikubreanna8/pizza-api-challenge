from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import model files to register them with SQLAlchemy
from .restaurant import Restaurant
from .pizza import Pizza
from .restaurant_pizza import RestaurantPizza
