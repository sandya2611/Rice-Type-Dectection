#!/usr/bin/env python3
"""
Rice Type Detection - Startup Script
This script helps you start the application easily.
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
    return True

def install_requirements():
    """Install required packages"""
    print("\n📦 Installing required packages...")
    try:
        # First try to upgrade pip
        print("Upgrading pip...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], 
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Install packages one by one to handle errors better
        packages = [
            "Flask>=2.3.0",
            "torch>=2.6.0", 
            "torchvision>=0.17.0",
            "Pillow>=10.0.0",
            "Werkzeug>=2.3.0",
            "numpy>=1.24.0",
            "requests>=2.31.0"
        ]
        
        for package in packages:
            print(f"Installing {package}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package],
                                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError as e:
                print(f"⚠️  Warning: Could not install {package}: {e}")
                # Continue with other packages
        
        print("✅ Package installation completed")
        return True
        
    except Exception as e:
        print(f"❌ Failed to install packages: {e}")
        print("\n💡 Try installing packages manually:")
        print("pip install Flask torch torchvision Pillow Werkzeug numpy requests")
        return False

def create_uploads_directory():
    """Create uploads directory if it doesn't exist"""
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
        print("✅ Created uploads directory")
    else:
        print("✅ Uploads directory exists")

def check_model_file():
    """Check if model file exists"""
    model_path = 'Training/rice_model.pth'
    if os.path.exists(model_path) and os.path.getsize(model_path) > 0:
        print("✅ Trained model found")
        return True
    else:
        print("⚠️  No trained model found - will use pre-trained model")
        return False

def start_application():
    """Start the Flask application"""
    print("\n🚀 Starting Rice Type Detection Application...")
    print("=" * 50)
    
    try:
        # Import and run the app
        from app import app
        print("\n✅ Application started successfully!")
        print("🌐 Open your browser and go to: http://localhost:5000")
        print("📱 The application will work on both desktop and mobile devices")
        print("\n🛑 Press Ctrl+C to stop the application")
        print("=" * 50)
        
        app.run(debug=True, host='0.0.0.0', port=5000)
        
    except KeyboardInterrupt:
        print("\n\n🛑 Application stopped by user")
    except ImportError as e:
        print(f"\n❌ Import error: {e}")
        print("This might be due to missing packages. Try running:")
        print("pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"\n❌ Error starting application: {e}")
        return False
    
    return True

def main():
    """Main function"""
    print("🌾 Rice Type Detection - Startup Script")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Check if we're in the right directory
    if not os.path.exists('app.py'):
        print("❌ app.py not found. Please run this script from the project root directory.")
        return
    
    # Create uploads directory
    create_uploads_directory()
    
    # Check model file
    check_model_file()
    
    # Install requirements
    if not install_requirements():
        print("❌ Failed to install requirements. Please check your internet connection.")
        print("You can try running the application directly with: python app.py")
        response = input("Do you want to try starting the application anyway? (y/n): ")
        if response.lower() != 'y':
            return
    
    # Start the application
    start_application()

if __name__ == "__main__":
    main() 