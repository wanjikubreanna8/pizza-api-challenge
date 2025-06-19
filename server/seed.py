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
    r1 = Restaurant()
    r1.name = "Kiki's Pizza"
    r1.address = "123 Main St"
    r2 = Restaurant()
    r2.name = "Mario's Pizzeria"
    r2.address = "456 Elm St"
    r3 = Restaurant()
    r3.name = "Luigi's Slice"
    r3.address = "789 Oak St"

    db.session.add_all([r1, r2, r3])

    # Create some pizzas
    p1 = Pizza()
    p1.name = "Emma"
    p1.ingredients = "Dough, Tomato Sauce, Cheese"
    p2 = Pizza()
    p2.name = "Pepperoni"
    p2.ingredients = "Dough, Tomato Sauce, Cheese, Pepperoni"
    p3 = Pizza()
    p3.name = "Veggie"
    p3.ingredients = "Dough, Tomato Sauce, Cheese, Peppers, Olives"

    db.session.add_all([p1, p2, p3])
    db.session.commit()

    # Create some restaurant pizzas (join table entries)
    rp1 = RestaurantPizza()
    rp1.price = 10
    rp1.pizza = p1
    rp1.restaurant = r1

    rp2 = RestaurantPizza()
    rp2.price = 15
    rp2.pizza = p2
    rp2.restaurant = r1

    rp3 = RestaurantPizza()
    rp3.price = 12
    rp3.pizza = p3
    rp3.restaurant = r2

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("Database seeded!")
