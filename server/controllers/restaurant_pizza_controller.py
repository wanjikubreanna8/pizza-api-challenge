from flask import Blueprint, request, jsonify
from server.models import db, RestaurantPizza, Restaurant, Pizza

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__, url_prefix='/restaurant_pizzas')


@restaurant_pizza_bp.route('/', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    errors = []

    if price is None:
        errors.append("Price is required")
    elif not isinstance(price, int) or price < 1 or price > 30:
        errors.append("Price must be between 1 and 30")

    if pizza_id is None or not Pizza.query.get(pizza_id):
        errors.append("Valid pizza_id is required")

    if restaurant_id is None or not Restaurant.query.get(restaurant_id):
        errors.append("Valid restaurant_id is required")

    if errors:
        return jsonify({"errors": errors}), 400

    new_rp = RestaurantPizza()
    new_rp.price = price
    new_rp.pizza_id = pizza_id
    new_rp.restaurant_id = restaurant_id

    db.session.add(new_rp)
    db.session.commit()

    return jsonify(new_rp.to_dict()), 201
