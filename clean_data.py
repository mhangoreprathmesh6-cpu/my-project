# clean_data.py

import os
from PIL import Image

# Path where your downloaded images are stored
DATASET_DIR = "simple_images"  # change if needed

def is_image_corrupted(image_path):
    """Check if an image file is corrupted."""
    try:
        with Image.open(image_path) as img:
            img.verify()  # Verify integrity
        return False
    except Exception as e:
        print(f"❌ Corrupted: {image_path}")
        return True

def clean_dataset(directory):
    """Remove all corrupted images from dataset."""
    total_deleted = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                img_path = os.path.join(root, file)
                if is_image_corrupted(img_path):
                    os.remove(img_path)
                    total_deleted += 1
    print(f"\n🧹 Cleaning complete! {total_deleted} corrupted images removed.")

if __name__ == "__main__":
    clean_dataset(DATASET_DIR)
