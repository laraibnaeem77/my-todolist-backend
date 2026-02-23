My To-Do List Backend ⚡

A FastAPI backend for the My To-Do List application. Handles task management and exposes REST API endpoints for the React frontend.

Features ✨

REST API for managing tasks (create, read, update, delete)

Data handling and business logic for the application

Lightweight and fast backend powered by FastAPI

Installation & Running Locally 💻

Clone the repository

git clone https://github.com/laraibnaeem77/my-todolist-backend.git
cd my-todolist-backend

Install dependencies

pip install -r requirements.txt

Run the backend server

uvicorn main:app --reload

Server will run at http://127.0.0.1:8000

Technologies Used 🛠️

Backend: FastAPI, Python

Tools: pip, Uvicorn

API Endpoints 🧩

GET /tasks – Get all tasks

POST /tasks – Create a new task

PUT /tasks/{id} – Update a task

DELETE /tasks/{id} – Delete a task

Integration

Connects with the React frontend to provide full-stack functionality.

Learn More 📚

FastAPI Documentation

Contribution 🤝

Fork, report issues, or submit pull requests. Contributions are welcome!

License 📄

MIT License
