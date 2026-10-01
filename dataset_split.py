import os
import shutil
import random

# Paths
DATASET_DIR = "simple_images"   # simple_image_download ka output folder
OUTPUT_DIR = "data"             # final dataset folder
TRAIN_SPLIT = 0.8               # 80% train, 20% validation

# Create output folders
train_dir = os.path.join(OUTPUT_DIR, "train")
val_dir = os.path.join(OUTPUT_DIR, "val")

os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# List all food categories
categories = os.listdir(DATASET_DIR)

for category in categories:
    cat_path = os.path.join(DATASET_DIR, category)
    if not os.path.isdir(cat_path):
        continue

    images = [f for f in os.listdir(cat_path) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    random.shuffle(images)

    split_point = int(len(images) * TRAIN_SPLIT)
    train_images = images[:split_point]
    val_images = images[split_point:]

    # Create category folders
    os.makedirs(os.path.join(train_dir, category), exist_ok=True)
    os.makedirs(os.path.join(val_dir, category), exist_ok=True)

    # Copy images
    for img in train_images:
        shutil.copy(os.path.join(cat_path, img), os.path.join(train_dir, category, img))
    for img in val_images:
        shutil.copy(os.path.join(cat_path, img), os.path.join(val_dir, category, img))

    print(f"✅ {category}: {len(train_images)} train, {len(val_images)} val")

print("\n🎯 Dataset splitting complete! Files saved in 'data/' folder.")
