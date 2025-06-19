🍕 Pizza Restaurant API Challenge

This is a RESTful API built with *Flask, **SQLAlchemy, and **Flask-Migrate* for managing restaurants, pizzas, and their associations. You can use Postman to test routes — no frontend is required.

---

## 📁 Project Structure (MVC)

.
├── server/
│ ├── app.py # App setup and app factory
│ ├── config.py # Configuration
│ ├── seed.py # Seed script
│ ├── models/
│ │ ├── init.py
│ │ ├── pizza.py
│ │ ├── restaurant.py
│ │ └── restaurant_pizza.py
│ └── controllers/
│ ├── init.py
│ ├── pizza_controller.py
│ ├── restaurant_controller.py
│ └── restaurant_pizza_controller.py
├── migrations/
├── challenge-1-pizzas.postman_collection.json
└── README.md

yaml
Copy
Edit

---

## 🧰 Setup Instructions

### 1. Clone and Install Dependencies

```bash
git clone https://github.com/your-username/pizza-api-challenge.git
cd pizza-api-challenge
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell
2. Set Up Database
bash
Copy
Edit

flask db init
flask db migrate -m "Initial migration"
flask db upgrade
3. Seed the Database
bash
Copy
Edit
python -m server.seed
🚀 Run the Server
bash
Copy
Edit
export FLASK_APP=server.app:create_app
flask run --port=5001
Then visit: http://localhost:5001

📮 API Endpoints
🔹 GET /restaurants
Returns a list of all restaurants.

Example Response:

json
Copy
Edit
[
  {
    "id": 1,
    "name": "Mario's Pizza",
    "address": "123 Main Street"
  },
  ...
]
🔹 GET /restaurants/:id
Returns a single restaurant and its pizzas.

Example Response:

json
Copy
Edit
{
  "id": 1,
  "name": "Mario's Pizza",
  "address": "123 Main Street",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Dough, Tomato Sauce, Cheese",
      "price": 10
    }
  ]
}
If Not Found:

json
Copy
Edit
{
  "error": "Restaurant not found"
}
🔹 DELETE /restaurants/:id
Deletes a restaurant and its related RestaurantPizzas.

If Successful:

Status Code: 204 No Content

If Not Found:

json
Copy
Edit
{
  "error": "Restaurant not found"
}
🔹 GET /pizzas
Returns a list of all pizzas.

Example Response:

json
Copy
Edit
[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  ...
]
🔹 POST /restaurant_pizzas
Creates a new association between a pizza and restaurant.

Request Body:

json
Copy
Edit
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
Success Response:

json
Copy
Edit
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  "restaurant": {
    "id": 3,
    "name": "Kiki's Pizza",
    "address": "456 Side Street"
  }
}
Error Response (400):

json
Copy
Edit
{
  "errors": ["Price must be between 1 and 30"]
}
🧪 Testing with Postman
Open Postman

Click Import

Upload challenge-1-pizzas.postman_collection.json

Test each route (server must be running)

✅ Validation Rules
RestaurantPizza.price must be an integer between 1 and 30

pizza_id and restaurant_id must reference existing Pizza and Restaurant

✅ Submission Checklist
 MVC folder structure

 Models with relationships & validation

 All required routes implemented

 Postman tests included

 This README.md completed

👩🏽‍💻 Built With
Python 3.10+

Flask

SQLAlchemy

Flask-Migrate

SQLite (dev)

