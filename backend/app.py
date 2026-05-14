from fastapi import FastAPI
import joblib
import numpy as np

from pricing_logic import (
    apply_flash_sale_adjustment,
    apply_inventory_adjustment,
    blend_with_competitor_price
)

app = FastAPI()

# Load trained model
model = joblib.load("../models/pricing_model.pkl")


@app.get("/")
def home():
    return {"message": "Dynamic Pricing API Running"}


@app.post("/predict")
def predict_price(
    category: int,
    units_sold: int,
    season: int,
    customer_segment: int,
    stock: int,
    competitor_price: float
):
    # Step 1: ML prediction
    data = np.array([[category, units_sold, season, customer_segment]])
    ml_price = float(model.predict(data)[0])

    # Step 2: Blend with competitor price
    price = blend_with_competitor_price(ml_price, competitor_price)

    # Step 3: Flash sale adjustment
    price = apply_flash_sale_adjustment(price, units_sold)

    # Step 4: Inventory adjustment
    price = apply_inventory_adjustment(price, stock)

    # Round to 2 decimal places
    final_price = round(price, 2)

    return {
        "ml_price": round(ml_price, 2),
        "competitor_price": competitor_price,
        "final_optimized_price": final_price
    }