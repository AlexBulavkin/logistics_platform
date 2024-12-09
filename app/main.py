from fastapi import FastAPI
from app.routers import logistics

app = FastAPI(
    title="Logistics Optimization API",
    description="Платформа расчета оптимального маршрута для курьеров",
    version="1.0.0",
)

# Подключение роутеров
app.include_router(logistics.router)


@app.get("/")
async def root():
    return {"message": "Добро пожаловать в Logistics Optimization API"}
