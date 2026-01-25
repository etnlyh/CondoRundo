import numpy as np
import tensorflow as tf
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "house_price_model.keras")

model = tf.keras.models.load_model(MODEL_PATH)

# model = tf.keras.models.load_model("../models/house_price_model.keras")

def estimate_price(size: int, rooms: int):
    X = np.array([[size, rooms]], dtype=float)

    # Same normalization
    X = X / np.array([2000, 10])

    prediction = model.predict(X)

    # Reverse normalization
    price = prediction[0][0] * 2000000

    # Convert to float
    prediction_value = float(price)

    # Inside Dictionary format
    return round(prediction_value, 2) # CAD dollars

    # return round(price * 100, 2)  # CAD dollars
