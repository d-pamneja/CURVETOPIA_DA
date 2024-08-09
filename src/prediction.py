from src.utils import *

# Test Prediction
user_image_path = '/Users/dhruv/Desktop/Adobe_GenSolve/CURVETOPIA_DA/problems/occlusion1_rec.png' 
predicted_class = predict_image(model, user_image_path, label_encoder)
print(f'Predicted Class: {predicted_class}')
display_image_with_prediction(user_image_path, predicted_class)