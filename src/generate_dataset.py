from src.dependencies import *

# Defining the function to generate the dataset
def generate_custom_shapes_dataset(num_samples_per_class=1000, output_directory='./dataset'):
    """
    Generate a dataset of custom shapes.
    
    Parameters:
    - num_samples_per_class: Number of samples to generate per class.
    - output_dir: Directory to save the generated dataset.
    
    Returns:
    - None
    """
    
    shapes = ['line', 'circle', 'ellipse', 'rectangle', 'rounded_rectangle', 'regular_polygon', 'star']
    if(not os.path.exists(output_directory)):
        os.makedirs(output_directory)
    
    for shape in shapes:
        shape_directory = os.path.join(output_directory, shape)
        if(not os.path.exists(shape_directory)):
            os.makedirs(shape_directory)
        
        for i in range(num_samples_per_class):
            img = np.zeros((128, 128), dtype=np.uint8)
            
            if(shape == 'line'):
                x1, y1 = np.random.randint(0, 128, size=2)
                x2, y2 = np.random.randint(0, 128, size=2)
                cv2.line(img, (x1, y1), (x2, y2), 255, 2)
            
            elif(shape == 'circle'):
                radius = np.random.randint(10, 40)
                x, y = np.random.randint(radius, 128-radius, size=2)
                cv2.circle(img, (x, y), radius, 255, 2)
            
            elif(shape == 'ellipse'):
                x, y = np.random.randint(20, 108, size=2)
                axes = np.random.randint(10, 50, size=2)
                angle = np.random.randint(0, 180)
                cv2.ellipse(img, (x, y), tuple(axes), angle, 0, 360, 255, 2)
            
            elif(shape == 'rectangle'):
                x1, y1 = np.random.randint(0, 108, size=2)
                x2, y2 = x1 + np.random.randint(20, 40), y1 + np.random.randint(20, 40)
                cv2.rectangle(img, (x1, y1), (x2, y2), 255, 2)
            
            elif(shape == 'rounded_rectangle'):
                x1, y1 = np.random.randint(0, 108, size=2)
                x2, y2 = x1 + np.random.randint(20, 40), y1 + np.random.randint(20, 40)
                radius = np.random.randint(5, 15)
                cv2.rectangle(img, (x1, y1), (x2, y2), 255, 2)
                cv2.circle(img, (x1, y1), radius, 255, 2)
                cv2.circle(img, (x2, y2), radius, 255, 2)
                cv2.circle(img, (x1, y2), radius, 255, 2)
                cv2.circle(img, (x2, y1), radius, 255, 2)
            
            elif(shape == 'regular_polygon'):
                points = np.random.randint(0, 128, size=(5, 2))
                cv2.polylines(img, [points], isClosed=True, color=255, thickness=2)
            
            elif(shape == 'star'):
                points = np.random.randint(0, 128, size=(5, 2))
                cv2.polylines(img, [points], isClosed=True, color=255, thickness=2)
            
            img_path = os.path.join(shape_directory, f'{i}.png')
            cv2.imwrite(img_path, img)


generate_custom_shapes_dataset()