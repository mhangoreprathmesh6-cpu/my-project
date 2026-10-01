import torch
import torchvision.transforms as transforms
from PIL import Image

MODEL_PATH = "food_classifier.pth"

model = torch.load(MODEL_PATH, map_location="cpu", weights_only=False)
model.eval()

classes = ['apple', 'biryani', 'dosa', 'idli', 'salad']

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

def classify_food(img):
    if isinstance(img, Image.Image):
        image = img
    else:
        image = Image.open(img).convert("RGB")

    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(image)
        probs = torch.nn.functional.softmax(outputs, dim=1)

    conf, pred = torch.max(probs, 1)

    return classes[pred.item()], conf.item()