# Melanoma Detection Using Deep Learning

# Overview

Melanoma Detection is an AI-powered web application that helps classify skin lesion images as Benign Melanoma or Malignant Melanoma using a Convolutional Neural Network (CNN).

The project is developed using TensorFlow, Keras, Flask, and Python, providing a simple interface for image upload and real-time prediction.

## Features

* Skin lesion image classification
* Deep learning-based prediction
* Flask web interface
* Image upload functionality
* Prediction confidence score
* Benign vs Malignant classification

## Tech Stack

* Python
* TensorFlow
* Keras
* Flask
* NumPy
* Pillow

## Model Information

* Architecture: VGG16-based CNN
* Accuracy: 84.09%
* Classes:

  * Benign Melanoma
  * Malignant Melanoma

## Installation

```bash
git clone https://github.com/yourusername/melanoma-detection-cnn.git

cd melanoma-detection-cnn

pip install -r requirements.txt
```

## Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Project Structure

```text
app.py
requirements.txt
skin.h5
static/
templates/
```

## Future Improvements

* Multi-class skin disease classification
* Improved accuracy with EfficientNet
* Explainable AI visualizations
* Cloud deployment
* Mobile application support

## Disclaimer

This project is intended for educational and research purposes only and should not be used as a substitute for professional medical diagnosis.
