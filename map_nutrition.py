# map_nutrition.py

# Dictionary mapping each food to its nutritional values per serving
nutrition_data = {
    "apple": {
        "calories": 52,
        "protein": 0.3,
        "fat": 0.2,
        "carbohydrates": 14,
        "fiber": 2.4,
        "sugar": 10
    },
    "biryani": {
        "calories": 290,
        "protein": 12,
        "fat": 9,
        "carbohydrates": 38,
        "fiber": 2,
        "sugar": 3
    },
    "dosa": {
        "calories": 168,
        "protein": 4,
        "fat": 6,
        "carbohydrates": 25,
        "fiber": 1.2,
        "sugar": 0.5
    },
    "idli": {
        "calories": 58,
        "protein": 2,
        "fat": 0.4,
        "carbohydrates": 12,
        "fiber": 0.9,
        "sugar": 0.1
    },
    "salad": {
        "calories": 33,
        "protein": 1.8,
        "fat": 0.2,
        "carbohydrates": 6,
        "fiber": 2.5,
        "sugar": 3
    }
}

def get_nutrition(food_name):
    """Return nutrition info for a given food."""
    food_name = food_name.lower()
    if food_name in nutrition_data:
        return nutrition_data[food_name]
    else:
        return {"error": f"No nutrition data found for '{food_name}'."}


# For direct testing
if __name__ == "__main__":
    food = input("Enter food name: ")
    info = get_nutrition(food)
    print(f"\nNutrition for {food.capitalize()}:\n", info)
