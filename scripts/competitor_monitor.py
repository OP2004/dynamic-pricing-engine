from fastapi import FastAPI
import random

app = FastAPI()

# Simulated competitor pricing database
BASE_PRICES = {
    "Shoes": 3000,
    "Watch": 5000,
    "Mobile": 20000,
    "Laptop": 60000,
    "TV": 40000
}

@app.get("/competitor-price")
def get_competitor_price(product: str):

    if product not in BASE_PRICES:
        return {
            "status": "error",
            "message": "Product not found"
        }

    base_price = BASE_PRICES[product]

    # simulate real-time fluctuation (-10% to +10%)
    variation = random.uniform(-0.1, 0.1)
    price = base_price + (base_price * variation)

    return {
        "status": "success",
        "product": product,
        "competitor_price": round(price, 2)
    }