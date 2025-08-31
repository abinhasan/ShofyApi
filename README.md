# 🚀 ShofyAPI - FastAPI Template

This is a **production-ready FastAPI template** with:

- ✅ FastAPI + Uvicorn  
- ✅ PostgreSQL (via SQLAlchemy ORM)  
- ✅ Alembic for migrations  
- ✅ Pydantic v2 models  
- ✅ Users + Auth (JWT-based)  
- ✅ Orders module (with `services` + `crud` layers)  
- ✅ Config management via `.env`

---

## 📂 Project Structure

shofy/
│── app/
│ ├── init.py
│ ├── main.py # FastAPI entrypoint
│ │
│ ├── core/
│ │ ├── config.py # Settings from .env
│ │ └── security.py # Password hashing & JWT
│ │
│ ├── db/
│ │ ├── base.py # Base class for models
│ │ ├── db.py # Session & engine
│ │ └── init_db.py # Initial data (optional)
│ │
│ ├── models/
│ │ ├── user.py # User model
│ │ └── order.py # Order model
│ │
│ ├── schemas/
│ │ ├── user.py # Pydantic schemas
│ │ └── order.py
│ │
│ ├── crud/
│ │ ├── user_crud.py
│ │ └── order_crud.py
│ │
│ ├── services/
│ │ ├── user_service.py
│ │ └── order_service.py
│ │
│ └── api/
│ ├── deps.py
│ ├── v1/
│ │ ├── auth.py # Login & register
│ │ ├── users.py
│ │ └── orders.py
│ └── router.py # Collects API routes
│
│── alembic/ # Alembic migrations
│── alembic.ini # Alembic config
│── .env # Environment variables
│── requirements.txt
│── README.md

---

## ⚙️ Installation

1️⃣ Clone repo  
```bash
git clone https://github.com/yourusername/shofyapi.git
cd shofyapi

python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows

pip install -r requirements.txt

DATABASE_URL=postgresql+psycopg2://postgres:123456@localhost:5432/shofy
SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

alembic revision --autogenerate -m "init"
alembic upgrade head

uvicorn app.main:app --reload

App will run at:
👉 http://127.0.0.1:8000

👉 API docs: http://127.0.0.1:8000/docs

API Overview
Auth

POST /api/v1/auth/register → Register new user

POST /api/v1/auth/login → Login & get JWT

Users

GET /api/v1/users/me → Get current user

GET /api/v1/users/ → List all users (admin only)

Orders

POST /api/v1/orders/ → Create new order

GET /api/v1/orders/ → List all orders

✅ Tech Stack

FastAPI

SQLAlchemy

Alembic

Pydantic v2

Passlib
 for password hashing

Python-Jose
 for JWT

 🧑‍💻 Author

Developed with ❤️ using FastAPI