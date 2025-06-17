from flask import Flask, jsonify
from server import create_app
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

app = create_app()

# Register blueprints with URL prefixes
app.register_blueprint(restaurant_bp, url_prefix='/api')
app.register_blueprint(pizza_bp, url_prefix='/api')
app.register_blueprint(restaurant_pizza_bp, url_prefix='/api')

@app.route('/')
def home():
    return "Welcome to the Pizza Restaurant API!"

@app.route('/api')
def api_home():
    return jsonify({
        "message": "Welcome to the Pizza Restaurant API!",
        "endpoints": {
            "restaurants": "/api/restaurants",
            "pizzas": "/api/pizzas",
            "restaurant_pizzas": "/api/restaurant_pizzas"
        }
    })

if __name__ == '__main__':
    app.run(port=5555, debug=True)