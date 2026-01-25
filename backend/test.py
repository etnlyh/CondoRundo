import tensorflow as tf
from h5py.h5t import INTEGER
import os
from backend.app.model import predict_price

def test_predict_price(self):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "house_price_model.keras")

    model = tf.keras.models.load_model(MODEL_PATH)
    price = predict_price(50, 2)
    assert type(price) == INTEGER