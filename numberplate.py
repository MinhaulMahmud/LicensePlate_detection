import os
import cv2
from ultralytics import YOLO


def replace_numberplate(image_path, replacement_image, found=False):
    # Read the input image
    frame = cv2.imread(image_path)
    H, W, _ = frame.shape

    # Detect objects in the image
    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            # Object detected, set found = True
            found = True

            # Calculate the width and height of the cropped area
            width = int(x2 - x1)
            height = int(y2 - y1)

            # Resize the replacement image to match the dimensions of the cropped area without rounding
            resized_replacement = cv2.resize(
                replacement_image, (width, height), interpolation=cv2.INTER_AREA)

            # Replace the detected area with the replacement image
            frame[int(y1):int(y1) + height, int(x1)                  :int(x1) + width] = resized_replacement

    if not found:
        print("No numberplate detected")

    # Display the modified image
    cv2.imshow("Modified Image", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Path to the directory containing the input images
IMAGES_DIR = os.path.join('.', 'tests') 

# Path to the YOLO model
model_path = os.path.join('.', 'numberplate.pt')

# Load the YOLO model
model = YOLO(model_path)

# Threshold for object detection
threshold = 0.2

# Example usage
# Provide the path to your input image
image_path = os.path.join(IMAGES_DIR, 'test3.jpg')

# Load the replacement image
# Provide the path to the replacement image
replacement_image = cv2.imread('numberplate.jpg')

# Replace numberplate
replace_numberplate(image_path, replacement_image)
