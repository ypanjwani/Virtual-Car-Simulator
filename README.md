## Autonomous Driving Simulation
# OverView
This project implements an autonomous driving simulation using the Udacity car simulator, Flask, and machine learning models trained in Google Colab. The system collects driving data, processes it using deep learning models, and controls the vehicle in the simulator.

# Features

Real-time autonomous driving in the Udacity simulator

Flask API for communication between the simulator and the ML model

Data collection and preprocessing for training

Deep learning-based self-driving model (trained in Google Colab)

# Tech Stack

**🕹 Udacity Car Simulator** - Provides the driving environment

**🌐 Flask** - Acts as a bridge between the simulator and the ML model

**💻 Google Colab** - Used for training deep learning models

**🐍 Python** - Main programming language

**🔬 TensorFlow/Keras** - Deep learning framework for model training

**📷 OpenCV** - Image preprocessing

**📈 NumPy & Pandas** - Data handling

# Model Training

1. **Collect driving data** by running the simulator in "Training Mode."

2. **Preprocess the collected data** (stored in .csv format with images).

3. **Train a deep learning model** in Google Colab using train_model.ipynb.

4. **Save the trained model** and use it in server.py for inference.

# Future Improvements

1. 🚀 Implement reinforcement learning for better driving behavior

2. ⚡ Optimize model inference speed

3. 🛑 Add object detection for obstacle avoidance
