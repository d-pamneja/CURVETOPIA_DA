from src.dependencies import *

def preprocess_image(image_path, target_size=(128, 128)):
    """
    Preprocess an image for prediction.
    
    Parameters:
    - image_path: Path to the image file.
    - target_size: Size to which the image should be resized.
    
    Returns:
    - img: Preprocessed image as a numpy array.
    """
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if(img is not None):
        img = cv2.resize(img, target_size)
        img = img.reshape((1, 128, 128, 1)) / 255.0
        
    return img

def predict_image(model, image_path, label_encoder):
    """ 
    Predict the class of an image.
    
    Parameters:
    - model: The trained model to use for prediction.
    - image_path: Path to the image file.
    - label_encoder: The label encoder used to encode the classes.
    
    Returns:
    - predicted_class: The predicted class of the image.
    """
    img = preprocess_image(image_path)
    prediction = model.predict(img)
    predicted_class = label_encoder.inverse_transform([np.argmax(prediction)])
    return predicted_class[0]

    
# Loading the Label Encoder
label_encoder = LabelEncoder()
label_encoder.classes_ = np.array(['line', 'circle', 'ellipse', 'rectangle', 'rounded_rectangle', 'regular_polygon', 'star'])


# Loading the trained model
model = load_model("./models/shapes_created_model.h5")

# Prediction Function
def prediction(user_image_path):
    predicted_class = predict_image(model, user_image_path, label_encoder)
    return predicted_class

