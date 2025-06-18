from flask import Blueprint, jsonify, request
from server.models import db, Restaurant

restaurant_bp = Blueprint('restaurant_bp', __name__, url_prefix='/restaurants')


@restaurant_bp.route('/', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants])


@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    restaurant_data = restaurant.to_dict()
    restaurant_data['pizzas'] = [
        {
            "id": rp.pizza.id,
            "name": rp.pizza.name,
            "ingredients": rp.pizza.ingredients,
            "price": rp.price
        }
        for rp in restaurant.restaurant_pizzas
    ]
    return jsonify(restaurant_data)


@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return '', 204
