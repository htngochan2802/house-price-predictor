from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles

app = FastAPI()

area: float = Query(..., ge=0, description="Diện tích (m²), phải >= 0"),
bedrooms: int = Query(..., ge=0, description="Số phòng ngủ, phải >= 0"),

def predict_price(area: float, bedrooms: int, location: str) -> float:
    price = 500_000_000
    price += 15_000_000 * area
    price += 50_000_000 * bedrooms

    loc = location.strip().lower()
    if loc == "hanoi":
        price *= 1.3
    elif loc == "hcmc":
        price *= 1.25
    price = round(price / 1_000_000) * 1_000_000
    return float(price)

@app.get("/predict")
def predict(area: float, bedrooms: int, location: str = "other"):
    predicted_price = predict_price(area, bedrooms, location)
    return {
        "area": area,
        "bedrooms": bedrooms,
        "location": location,
        "predicted_price": predicted_price,
    }

app.mount("/static", StaticFiles(directory="../frontend"), name="static")
