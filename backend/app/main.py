from fastapi import FastAPI
import uvicorn
from model import estimate_price
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/price")
def get_price(size: int, rooms: int):
    price = estimatet_price(size, rooms)
    return {
        "size": size,
        "rooms": rooms,
        "estimated_price_cad": price
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)