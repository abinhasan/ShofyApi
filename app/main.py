from fastapi import FastAPI
from app.db.session import Base, engine
from app.api.v1 import auth, orders

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ShofyAPI")

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(orders.router, prefix="/api/v1/orders", tags=["Orders"])

@app.get("/")
def root():
    return {"message": "Welcome to ShofyAPI!"}
