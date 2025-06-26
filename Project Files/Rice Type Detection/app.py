import torch
import torch.nn as nn
from torchvision import models, transforms
from flask import Flask, render_template, request, flash, redirect, url_for
from PIL import Image
import json
import os
import uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load class names
try:
    with open('Training/class_names.json') as f:
        class_names = json.load(f)
except FileNotFoundError:
    # Fallback class names if file doesn't exist
    class_names = {
        "0": "Arborio",
        "1": "Basmati", 
        "2": "Ipsala",
        "3": "Jasmine",
        "4": "Karacadag"
    }

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load model
def load_model():
    try:
        # Use the newer way to get MobileNetV2 with weights
        model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)
        model.classifier[1] = nn.Linear(model.last_channel, len(class_names))
        model_path = 'Training/rice_model.pth'
        
        if os.path.exists(model_path) and os.path.getsize(model_path) > 0:
            try:
                model.load_state_dict(torch.load(model_path, map_location=device))
                print("Successfully loaded trained model")
            except Exception as e:
                print(f"Error loading model weights: {e}")
                print("Using pre-trained model without fine-tuning")
        else:
            print("Warning: Model file is empty or doesn't exist. Using pre-trained model.")
        
        model.eval().to(device)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

model = load_model()

# Image transformation with safe fallback
# Use standard ImageNet normalization values
mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=mean, std=std)
])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload_page():
    return render_template('upload.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return redirect(url_for('upload_page'))
    
    if 'image' not in request.files:
        flash('No file selected!', 'error')
        return redirect(url_for('upload_page'))
    
    file = request.files['image']
    
    if file.filename == '':
        flash('No file selected!', 'error')
        return redirect(url_for('upload_page'))
    
    if file and allowed_file(file.filename):
        try:
            # Save uploaded file
            filename = secure_filename(file.filename)
            unique_filename = f"{uuid.uuid4()}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            file.save(filepath)
            
            # Load and preprocess image
            img = Image.open(filepath).convert('RGB')
            img_tensor = transform(img).unsqueeze(0).to(device)
            
            # Make prediction
            if model is not None:
                with torch.no_grad():
                    outputs = model(img_tensor)
                    probabilities = torch.softmax(outputs, dim=1)
                    confidence, predicted = torch.max(probabilities, 1)
                    
                    predicted_class = class_names[str(predicted.item())]
                    confidence_score = confidence.item() * 100
            else:
                # Fallback for when model is not available
                predicted_class = "Model not available"
                confidence_score = 0.0
            
            # Clean up uploaded file
            try:
                os.remove(filepath)
            except:
                pass  # Ignore cleanup errors
            
            return render_template('results.html', 
                                 predicted_class=predicted_class,
                                 confidence_score=f"{confidence_score:.2f}%",
                                 original_filename=filename)
        
        except Exception as e:
            flash(f'Error processing image: {str(e)}', 'error')
            return redirect(url_for('upload_page'))
    
    else:
        flash('Invalid file type! Please upload an image file.', 'error')
        return redirect(url_for('upload_page'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    print("Starting Rice Type Detection Application...")
    print(f"Device: {device}")
    print(f"Model loaded: {model is not None}")
    print(f"Number of classes: {len(class_names)}")
    print("Available classes:", list(class_names.values()))
    print("\nAccess the application at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000) 