from ultralytics import YOLO

model = YOLO("yolov8s.pt")  # 🔥 change to s (CPU best)

model.train(
    data="dataset/data.yaml",
    epochs=80,
    imgsz=640,
    batch=4,        # 🔥 CPU safe
    patience=20,
    workers=2       # 🔥 avoid lag
)