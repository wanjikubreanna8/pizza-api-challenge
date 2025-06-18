from server.app import create_app
from server.models import db, Restaurant, Pizza, RestaurantPizza

app = create_app()

with app.app_context():
    # Clear existing data
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()
    db.session.commit()

    # Create some restaurants
    r1 = Restaurant(name="Kiki's Pizza", address="123 Main St")
    r2 = Restaurant(name="Mario's Pizzeria", address="456 Elm St")
    r3 = Restaurant(name="Luigi's Slice", address="789 Oak St")

    db.session.add_all([r1, r2, r3])

    # Create some pizzas
    p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    p3 = Pizza(name="Veggie", ingredients="Dough, Tomato Sauce, Cheese, Peppers, Olives")

    db.session.add_all([p1, p2, p3])
    db.session.commit()

    # Create some restaurant pizzas (join table entries)
    rp1 = RestaurantPizza(price=10, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=15, pizza_id=p2.id, restaurant_id=r1.id)
    rp3 = RestaurantPizza(price=12, pizza_id=p3.id, restaurant_id=r2.id)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("Database seeded!")
