calories = {
    "Bread": 265,
    "Dairy product": 150,
    "Dessert": 300,
    "Egg": 155,
    "Fried food": 320,
    "Meat": 250,
    "Noodles/Pasta": 190,
    "Rice": 130,
    "Seafood": 200,
    "Soup": 90,
    "Vegetable/Fruit": 60
}

def get_calories(food_name):
    return calories.get(food_name, "Calories not available")
