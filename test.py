import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

# Load model
model = load_model("artifacts/training/trained_model.h5")

# Use an actual image from your dataset
test_image_path = "artifacts/data_ingestion/unzip/Chicken-fecal-images/Coccidiosis/coccidiosis_001.jpg"  # Adjust filename

# Or find any image
import glob
images = glob.glob("artifacts/data_ingestion/unzip/Chicken-fecal-images/*/*.jpg")
if images:
    test_image_path = images[0]
    print(f"Testing with: {test_image_path}")

if os.path.exists(test_image_path):
    test_image = image.load_img(test_image_path, target_size=(224, 224))
    test_image = image.img_to_array(test_image)
    test_image = test_image / 255.0
    test_image = np.expand_dims(test_image, axis=0)
    
    prediction = model.predict(test_image)
    print(f"Raw prediction: {prediction}")
    print(f"Prediction probabilities: Class 0: {prediction[0][0]:.4f}, Class 1: {prediction[0][1]:.4f}")
    
    result = np.argmax(prediction, axis=1)
    print(f"Predicted class: {result[0]}")
    
    if result[0] == 1:
        print("Prediction: Coccidiosis")
    else:
        print("Prediction: Healthy")