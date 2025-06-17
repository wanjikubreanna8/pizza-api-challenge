from server import db
from sqlalchemy import CheckConstraint

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    
    __table_args__ = (
        CheckConstraint('price >= 1 AND price <= 30', name='check_price_range'),
    )
    
    def __repr__(self):
        return f'<RestaurantPizza ${self.price}>'
    
    def to_dict(self):
        from server.models.pizza import Pizza
        from server.models.restaurant import Restaurant
        
        pizza = Pizza.query.get(self.pizza_id)
        restaurant = Restaurant.query.get(self.restaurant_id)
        
        return {
            'id': self.id,
            'price': self.price,
            'pizza': pizza.to_dict() if pizza else None,
            'restaurant': restaurant.to_dict() if restaurant else None
        }