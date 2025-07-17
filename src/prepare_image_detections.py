import pandas as pd
import uuid
import re

# Load raw YOLO output
df = pd.read_csv("/home/samrawit/telegram-data-pipeline/data/clean/image_detections.csv")

# Extract filename and message_id (as date or integer surrogate)
def extract_message_id(image_path):
    # You can parse from photo_YYYY-MM-DD_HH-MM-SS.jpg
    match = re.search(r'photo_(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})', image_path)
    if match:
        # Format: "2025-07-14_12-45-25" → convert to datetime string or surrogate int
        return match.group(1)
    return None

df['message_id'] = df['image_path'].apply(extract_message_id)
df['detection_id'] = [str(uuid.uuid4()) for _ in range(len(df))]

# Reorder and select final columns
df_final = df[['detection_id', 'message_id', 'detected_object_class', 'confidence_score']]

# Save to CSV (no index)
df_final.to_csv('/home/samrawit/telegram-data-pipeline/data/clean/prepared.csv', index=False)
