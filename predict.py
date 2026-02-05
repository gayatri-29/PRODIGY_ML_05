import tensorflow as tf
import numpy as np
import cv2
from calories import get_calories

# Load trained model
model = tf.keras.models.load_model("food11_model.h5")

# Class names (same order as training)
class_names = [
    "Bread",
    "Dairy product",
    "Dessert",
    "Egg",
    "Fried food",
    "Meat",
    "Noodles/Pasta",
    "Rice",
    "Seafood",
    "Soup",
    "Vegetable/Fruit"
]

# Load test image
img = cv2.imread("test.jpg")

if img is None:
    raise ValueError("❌ test.jpg not found in project folder")

img = cv2.resize(img, (224, 224))
img = img / 255.0
img = np.expand_dims(img, axis=0)

# Predict
pred = model.predict(img)
food = class_names[np.argmax(pred)]

print("🍽 Detected Food:", food)
print("🔥 Estimated Calories:", get_calories(food))
