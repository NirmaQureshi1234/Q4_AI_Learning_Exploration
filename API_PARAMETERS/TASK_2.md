FastAPI Parameters Demo
This project demonstrates the use of parameters in FastAPI with multiple routes, including path parameters, query parameters, and request bodies. It also features a fun Batman route.

🚀 How to Run
Run the app using one of the following commands:

fastapi dev main.py
Or:

uvicorn main:app --reload
🌐 Visit:

http://localhost:8000/items/{item_id} — Get Item with a path parameter

http://localhost:8000/items — List Items with query parameters

http://localhost:8000/items/validated/{item_id} — Update Item with path and query parameters

http://localhost:8000/batman — Batman-themed route 🦇 (GET Method)

✨ Features

GET method to retrieve an item with a path parameter

GET method to list items with query parameters (q, skip, limit)

PUT method to update an item with both path and query parameters

Error handling with validation

Interactive API documentation at /docs

Batman route for a fun, dark-themed HTML response at /batman

BY: NIRMA QURESHI

