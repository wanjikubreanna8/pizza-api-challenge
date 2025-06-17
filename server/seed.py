# server/seed.py
from server import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

def seed_data():
    with app.app_context():
        print("Starting seed process...")
        
        # Clear existing data
        print("Dropping all tables...")
        db.drop_all()
        
        print("Creating all tables...")
        db.create_all()
        
        # Create restaurants
        print("Creating restaurants...")
        restaurants = [
            Restaurant(name="Pizza Palace", address="123 Main St"),
            Restaurant(name="Mario's Pizzeria", address="456 Oak Ave"),
            Restaurant(name="Luigi's Pizza", address="789 Pine Rd")
        ]
        db.session.add_all(restaurants)
        db.session.commit()
        print(f"Created {len(restaurants)} restaurants")
        
        # Create pizzas
        print("Creating pizzas...")
        pizzas = [
            Pizza(name="Margherita", ingredients="Tomato sauce, mozzarella, basil"),
            Pizza(name="Pepperoni", ingredients="Tomato sauce, mozzarella, pepperoni"),
            Pizza(name="Vegetarian", ingredients="Tomato sauce, mozzarella, bell peppers, mushrooms, onions")
        ]
        db.session.add_all(pizzas)
        db.session.commit()
        print(f"Created {len(pizzas)} pizzas")
        
        # Create restaurant pizzas
        print("Creating restaurant pizzas...")
        restaurant_pizzas = [
            RestaurantPizza(price=10, pizza_id=1, restaurant_id=1),
            RestaurantPizza(price=12, pizza_id=2, restaurant_id=1),
            RestaurantPizza(price=9, pizza_id=3, restaurant_id=2),
            RestaurantPizza(price=11, pizza_id=1, restaurant_id=3),
            RestaurantPizza(price=13, pizza_id=2, restaurant_id=3)
        ]
        db.session.add_all(restaurant_pizzas)
        db.session.commit()
        print(f"Created {len(restaurant_pizzas)} restaurant pizzas")
        
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()