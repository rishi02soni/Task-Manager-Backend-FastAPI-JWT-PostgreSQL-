# 🚀 Task Manager Backend API | FastAPI + JWT + SQLAlchemy

<p align="center">
  <img src="https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif" width="650"/>
</p>

A **production-ready backend API** built using **FastAPI (Python)** with **JWT Authentication, SQLAlchemy ORM, and Database Integration**.

This project demonstrates **secure API development, clean architecture, and modern backend practices**.

---

## 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-orange)
![JWT](https://img.shields.io/badge/Auth-JWT-red)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey)

---

## 🎬 Technology GIFs

### 🐍 Python Backend

<p align="center">
<img src="https://media.giphy.com/media/kH1DBkPNyZPOk0BxrM/giphy.gif" width="450">
</p>

---

### ⚡ FastAPI

<p align="center">
<img src="https://media.giphy.com/media/f3iwJFOVOwuy7K6FFw/giphy.gif" width="450">
</p>

---

### 🔐 Authentication (JWT)

<p align="center">
<img src="https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif" width="450">
</p>

---

## ⚡ Features

✔ User Registration & Login
✔ JWT Authentication (Secure APIs)
✔ Create / Read / Update / Delete Tasks
✔ Database Integration (SQLAlchemy ORM)
✔ RESTful API Design
✔ Interactive API Docs (Swagger UI)

---

## ⚙ Backend Workflow

```id="g0xk7o"
Client (Frontend / Postman)
            │
            ▼
        FastAPI Router
            │
            ▼
        Service Layer
            │
            ▼
        Database (SQLAlchemy)
            │
            ▼
        Response (JSON)
```

---

## 📂 Project Structure

```id="y4vx3i"
task-manager-fastapi
│
├── app
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   │
│   ├── routers
│   │     ├── user.py
│   │     └── task.py
│   │
│   └── services
│         └── task_service.py
│
├── requirements.txt
└── README.md
```

---

## 🔗 API Endpoints

### 👤 User APIs

* POST `/users/register` → Register user
* POST `/users/login` → Login & get JWT token

### 📋 Task APIs

* GET `/tasks/` → Get all tasks
* POST `/tasks/` → Create task
* PUT `/tasks/{id}` → Update task
* DELETE `/tasks/{id}` → Delete task

---

## ▶ How to Run the Project

### 1️⃣ Clone Repository

```id="8q1yim"
git clone https://github.com/yourusername/task-manager-fastapi.git
```

### 2️⃣ Install Dependencies

```id="rr4v5x"
pip install -r requirements.txt
```

### 3️⃣ Run Server

```id="nl0qk4"
uvicorn app.main:app --reload
```

---

## 🌐 API Documentation

Open in browser:

```id="h5b5fq"
http://127.0.0.1:8000/docs
```

---

## 💡 Future Improvements

* Use **PostgreSQL instead of SQLite**
* Add **Refresh Tokens**
* Add **Role-Based Authentication**
* Add **Docker Support**
* Deploy on **AWS / Render**

---

## 👨‍💻 Author

**Rishi Soni**

---

⭐ If you like this project, consider **starring the repository**.
