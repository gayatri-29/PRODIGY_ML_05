# PRODIGY_Task5
# 🍽️ Food Image Classification & Calorie Estimation

A deep learning project that classifies food images using a **CNN** and estimates their **calorie value** based on the predicted food category.

---

## 📌 Overview
- Food images classified into multiple categories
- CNN model trained using TensorFlow/Keras
- Calorie values mapped to each food class
- Predicts food type and estimated calories from an image

---

## 🛠 Tech Stack
- Python
- TensorFlow / Keras
- OpenCV
- NumPy

---

## 📂 Food Categories
Includes classes such as:
Bread, Dairy product, Dessert, Egg, Fried food, Meat, Noodles/Pasta, Rice, Seafood, Soup, Vegetable/Fruit

---

## ⚙️ How It Works
1. Train CNN model using food image dataset  
2. Save trained model (`food11_model.h5`)  
3. Load image and predict food category  
4. Fetch calorie estimate for predicted food  


python train.py    # Train model
python predict.py  # Predict food & calories
