import torch
import torch.nn as nn
from torchvision import models, transforms
from torchvision.models import mobilenet_v2, MobileNet_V2_Weights
from flask import Flask, render_template, request
from PIL import Image
import json
import os

app = Flask(__name__)

# Load class names
with open(os.path.join(os.path.dirname(__file__), 'class_names.json')) as f:
    class_names = json.load(f)

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load model
weights = MobileNet_V2_Weights.DEFAULT
model = mobilenet_v2(weights=weights)
model.classifier[1] = nn.Linear(model.last_channel, len(class_names))
model_path = os.path.join(os.path.dirname(__file__), 'rice_model.pth')
model.load_state_dict(torch.load(model_path, map_location=device))
model.eval().to(device)

# Image transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=weights.meta["mean"], std=weights.meta["std"])
])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No file uploaded!", 400

    img_file = request.files['image']
    img = Image.open(img_file).convert('RGB')
    img = transform(img).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(img)
        _, predicted = torch.max(outputs, 1)
        predicted_class = class_names[str(predicted.item())]

    return render_template('results.html', predicted_class=predicted_class)

if __name__ == '__main__':
    app.run(debug=True)
