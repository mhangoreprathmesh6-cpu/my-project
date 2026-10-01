from ultralytics import YOLO

# 🔥 trained model load
model = YOLO("runs/detect/train5/weights/best.pt")

# ❌ NON-FOOD BLOCK LIST (IMPORTANT)
NON_FOOD = ["person", "face", "hand", "cell phone", "laptop", "bottle"]

def detect_food(image_path):

    results = model(image_path, conf=0.5, iou=0.5) # 🔥 confidence direct apply

    boxes = []

    for r in results:
        for box in r.boxes:

            conf = float(box.conf[0])

            # 🔥 STRONG CONF FILTER
            if conf < 0.55:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0])
            label = model.names[cls].lower()

            # 🔥 NON-FOOD REMOVE
            if label in NON_FOOD:
                print("❌ Non-food skipped:", label)
                continue

            # 🔥 VERY SMALL BOX IGNORE (noise remove)
            box_area = (x2 - x1) * (y2 - y1)
            if box_area < 1500:
                continue

            boxes.append((x1, y1, x2, y2, label, conf))

    return boxes