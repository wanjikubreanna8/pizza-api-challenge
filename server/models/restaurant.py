# server/models/restaurant.py
from server.models import db
from sqlalchemy.orm import relationship

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)

    # Relationships
    restaurant_pizzas = relationship(
        'RestaurantPizza',
        back_populates='restaurant',
        cascade='all, delete-orphan'
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }
