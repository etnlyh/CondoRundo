import numpy as np
import tensorflow as tf

# Input: [size (sq ft), rooms]
X = np.array([
    [500, 2],
    [800, 3],
    [1200, 4],
    [600, 2],
    [1500, 5]
], dtype=float)

# Output: price in hundreds of CAD
Y = np.array([
    [500000],
    [790000],
    [1160000],
    [580000],
    [1450000]
], dtype=float)

# Normalize
X = X / np.array([2000, 10])
Y = Y / 2000000

# Build model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(4, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(
    optimizer='adam',
    loss='mse'
)

model.fit(X, Y, epochs=500, verbose=0)

# Save model
model.save("../models/house_price_model.keras")

print("Model trained and saved.")

