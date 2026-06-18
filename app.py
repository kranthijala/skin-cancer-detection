from flask import Flask, render_template, request, redirect, url_for, session
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import base64
from io import BytesIO

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session handling

# Load model from the project root (not inside static/)
MODEL_PATH = "skin.h5"
model = load_model(MODEL_PATH)

# Ensure uploads folder exists
UPLOAD_FOLDER = "static/uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Class labels
CLASS_LABELS = ["Benign Melanoma", "Malignant Melanoma"]

# Route for Home Page
@app.route('/')
def first():
    return render_template("first.html")

# Route for Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('pwd')

        if username == "admin" and password == "admin":
            session['user'] = username  # Save session
            return redirect(url_for('index'))  # Redirect to Preview Page
        else:
            return render_template('login.html', error="Invalid Credentials")

    return render_template('login.html')

# Route for Preview Page (Image Upload)
@app.route('/index', methods=['GET', 'POST'])
def index():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        if 'imagefile' not in request.files:
            return render_template("index.html", error="No file uploaded!")

        file = request.files['imagefile']
        if file.filename == '':
            return render_template("index.html", error="No selected file!")

        # Save uploaded file
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Process the image
        img = image.load_img(file_path, target_size=(224, 224))  # Resize to model input
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize

        # Get prediction
        predictions = model.predict(img_array)
        predicted_label = CLASS_LABELS[np.argmax(predictions)]
        confidence = np.max(predictions) * 100  # Convert to percentage

        # Encode image to display in result page
        with open(file_path, "rb") as img_file:
            img_base64 = base64.b64encode(img_file.read()).decode("utf-8")

        return render_template("result.html", out_pred=predicted_label, out_prob=confidence, processed_file=img_base64)

    return render_template("index.html")

# Route for Result Page
@app.route('/result')
def result():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template("result.html")

# Route for Performance Page
@app.route('/performance')
def performance():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template("performance.html")

# Route for Chart Page
@app.route('/chart')
def chart():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template("chart.html")

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
