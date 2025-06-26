# 🌾 Rice Type Detection

An advanced AI-powered web application that classifies different varieties of rice based on their visual characteristics using deep learning.

## 🚀 Features

- **5 Rice Types Supported**: Arborio, Basmati, Ipsala, Jasmine, and Karacadag
- **Drag & Drop Upload**: Modern, intuitive file upload interface
- **Real-time Analysis**: Instant classification with confidence scores
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Detailed Results**: Comprehensive information about each rice type
- **Modern UI**: Beautiful, user-friendly interface

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Machine Learning**: PyTorch with MobileNetV2 architecture
- **Frontend**: HTML5, CSS3, JavaScript
- **Image Processing**: PIL (Pillow), TorchVision
- **Model**: Transfer learning with pre-trained MobileNetV2

## 📋 Prerequisites

- Python 3.8 or higher
- Internet connection (for downloading packages)

## 🚀 Quick Start

### **Option 1: One-Click Start (Windows)**
1. Double-click `start.bat`
2. Wait for the application to start
3. Open your browser to `http://localhost:5000`

### **Option 2: Python Script**
```bash
python run.py
```

### **Option 3: Manual Start**
```bash
python app.py
```

---

## 🎯 How to Use

1. **Start the application** using any method above
2. **Open your browser** and go to `http://localhost:5000`
3. **Click "Start Detection"** on the homepage
4. **Upload a rice image** (drag & drop supported)
5. **View the classification results** with confidence scores

## 📁 Project Structure

```
Rice-Type-Detection/
├── app.py                 # Main Flask application
├── run.py                 # Startup script with auto-setup
├── start.bat              # Windows one-click startup
├── test_app.py            # Application testing script
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── uploads/              # Temporary upload directory
├── Training/             # Model and training files
│   ├── class_names.json  # Rice type labels
│   └── rice_model.pth    # Trained model weights (optional)
├── templates/            # HTML templates
│   ├── index.html       # Homepage
│   ├── upload.html      # Upload page
│   ├── results.html     # Results page
│   └── about.html       # About page
├── static/              # Static assets
│   └── style.css        # CSS styles
└── Data/                # Dataset directory
    └── Rice_Image_Dataset/
```

## 🍚 Supported Rice Types

| Rice Type | Origin | Characteristics | Best Uses |
|-----------|--------|-----------------|-----------|
| **Arborio** | Italy | Short-grain, high starch | Risotto, rice pudding |
| **Basmati** | India/Pakistan | Long-grain, aromatic | Biryani, pilaf, curry |
| **Ipsala** | Turkey | Long-grain, fluffy | Pilaf, stuffed vegetables |
| **Jasmine** | Thailand | Long-grain, fragrant | Thai dishes, stir-fries |
| **Karacadag** | Turkey | Long-grain, premium | Special occasions, pilaf |

## 🔧 Model Information

- **Architecture**: MobileNetV2 (pre-trained)
- **Input Size**: 224x224 pixels
- **Training**: Transfer learning approach
- **Classes**: 5 rice varieties
- **Performance**: High accuracy with confidence scoring

## 📱 How It Works

1. **Image Upload**: Users upload rice images through the web interface
2. **Preprocessing**: Images are resized, normalized, and converted to tensor format
3. **Feature Extraction**: MobileNetV2 extracts visual features from the image
4. **Classification**: The model predicts rice type with confidence scores
5. **Results Display**: Detailed results with rice information are shown

## 🎨 UI Features

- **Modern Design**: Clean, responsive interface with gradient backgrounds
- **Drag & Drop**: Intuitive file upload with visual feedback
- **Loading States**: Progress indicators during analysis
- **Error Handling**: User-friendly error messages
- **Mobile Responsive**: Optimized for all device sizes

## 🔒 Security Features

- **File Validation**: Only image files are accepted
- **Secure Filenames**: Uploaded files are sanitized
- **Temporary Storage**: Files are automatically cleaned up
- **Error Handling**: Graceful handling of invalid inputs

## 🧪 Testing

Run the test script to verify everything works:
```bash
python test_app.py
```

## 🚀 Deployment

### Local Development
```bash
python run.py
```

### Production Deployment
For production deployment, consider using:
- **WSGI Server**: Gunicorn or uWSGI
- **Reverse Proxy**: Nginx
- **Process Manager**: PM2 or Supervisor
- **Environment Variables**: Set `FLASK_ENV=production`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- PyTorch team for the deep learning framework
- Flask team for the web framework
- Rice dataset contributors
- Open source community

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section below
2. Run the test script: `python test_app.py`
3. Open an issue on GitHub

## 🔧 Troubleshooting

### Common Issues

1. **Python not found**
   - Install Python 3.8+ from [python.org](https://python.org)
   - Make sure Python is added to PATH during installation

2. **Model not loading**
   - The app works without a trained model (uses pre-trained MobileNetV2)
   - For better accuracy, add a trained `rice_model.pth` file to the `Training/` folder

3. **Upload errors**
   - Verify file is an image (JPG, PNG, GIF, BMP)
   - Check file size (max 10MB)
   - Ensure uploads directory has write permissions

4. **Import errors**
   - Run `python run.py` to automatically install dependencies
   - Or manually: `pip install -r requirements.txt`

5. **Port already in use**
   - Change port in `app.py`: `app.run(port=5001)`
   - Or kill existing process using port 5000

### Performance Tips

- Use GPU if available for faster inference
- Optimize image size before upload
- Consider model quantization for production

---

**Note**: This application is for educational and research purposes. For critical applications, please consult with rice experts or use additional verification methods. 