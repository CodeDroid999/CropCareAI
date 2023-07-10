from flask import Flask, render_template, request
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load the model
model = load_model('./models/apple-224.h5')

def model_predict(img_path, model):
    test_image = image.load_img(img_path, target_size=(224, 224))
    test_image = image.img_to_array(test_image)
    test_image = test_image / 255.0
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)
    return result

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the uploaded image file
    image_file = request.files['file']

    # Save the file to the uploads folder
    basepath = os.path.dirname(os.path.realpath('__file__'))
    file_path = os.path.join(basepath, './uploads', secure_filename(image_file.filename))
    image_file.save(file_path)
    
    

    # Make prediction
    result = model_predict(file_path, model)

    categories = ['Healthy', 'Multiple Disease', 'Rust', 'Scab']

    # Process the result
    pred_class = np.argmax(result)
    output = categories[pred_class]
    
    # Return the prediction result
    return output

if __name__ == '__main__':
    app.run(debug=False, port=5926)
