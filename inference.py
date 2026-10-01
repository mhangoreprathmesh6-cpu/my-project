# inference.py

import torch
from torchvision import transforms
from PIL import Image
import os
from map_nutrition import get_nutrition  # 👈 import our nutrition function

# Model and class setup
MODEL_PATH = "food_classifier.pth"
CLASS_NAMES = ["apple", "biryani", "dosa", "idli", "salad"]

# Image transformation (must match training settings)
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
])

# Load trained model
model = torch.load(MODEL_PATH, map_location=torch.device('cpu'), weights_only=False)
model.eval()

# --- Prediction function ---
def predict_image(image_path):
    if not os.path.exists(image_path):
        print(f"❌ File not found: {image_path}")
        return

    # Load and preprocess image
    image = Image.open(image_path).convert('RGB')
    image_tensor = transform(image).unsqueeze(0)

    # Run through model
    with torch.no_grad():
        outputs = model(image_tensor)
        _, predicted = torch.max(outputs, 1)
        predicted_class = CLASS_NAMES[predicted.item()]

    print(f"\n🍽️ Predicted Food: {predicted_class.capitalize()}")

    # Fetch nutrition info
    nutrition_info = get_nutrition(predicted_class)
    if "error" not in nutrition_info:
        print("\n🥗 Nutrition Information (per serving):")
        for k, v in nutrition_info.items():
            print(f"   {k.capitalize()}: {v}")
    else:
        print(nutrition_info["error"])


# --- Run manually ---
if __name__ == "__main__":
    image_path = input("Enter path to image for prediction: ").strip()
    predict_image(image_path)
