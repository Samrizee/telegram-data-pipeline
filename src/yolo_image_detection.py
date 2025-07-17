import os
import pandas as pd
from ultralytics import YOLO

# Initialize the YOLOv8 model
model = YOLO('yolov8n.pt') # Use the appropriate model file

# Function to scan for new images
def scan_for_images(image_directory):
    return [os.path.join(image_directory, f) for f in os.listdir(image_directory) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Function to detect objects in images
def detect_objects(image_paths):
    results = []
    for image_path in image_paths:
        detections = model(image_path)  # Run detection
        for result in detections:
            # Access boxes directly
            if result.boxes is not None:
                for box in result.boxes:
                    detected_class = model.names[int(box.cls)]  # Get class name
                    confidence_score = float(box.conf)  # Get confidence score
                    results.append({
                        'image_path': image_path,
                        'detected_object_class': detected_class,
                        'confidence_score': confidence_score
                    })
    return results

# Main function
def main(image_directory):
    image_paths = scan_for_images(image_directory)
    # print(f"Found images: {image_paths}")  # Debug: List of found images
    detections = detect_objects(image_paths)
    #print(f"Detections: {detections}")  # Debug: Check detections
    return detections



if __name__ == "__main__":
    image_directory = '/home/samrawit/telegram-data-pipeline/data/raw/Image/2025-07-15'
    results = main(image_directory)
    # Convert to DataFrame for further processing
    detections_df = pd.DataFrame(results)
    # Save the DataFrame to a CSV file
    detections_df.to_csv('/home/samrawit/telegram-data-pipeline/data/clean/image_detections.csv', index=False)
    # Print the DataFrame
    print(detections_df)
