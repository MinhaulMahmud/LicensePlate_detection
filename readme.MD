# Number Plate Replacement using YOLO

This Python script utilizes YOLO (You Only Look Once) object detection to locate number plates in images and replace them with a custom replacement image. It's particularly useful for anonymizing or censoring sensitive information in images.

# Requirements

Python 3.x
OpenCV (cv2)
Ultralytics YOLO (make sure it's installed and configured properly)

# Usage

1.  Install Dependencies: Install the required dependencies by running

        pip install -r requirements.txt

2.  Replace Number Plate Image: Prepare a replacement image that you want to use to replace the number plates in the input images. The replacement image should have similar dimensions to the detected number plates.

3.  Run the Script: Execute the script numberplate.py with appropriate parameters:

        python numberplate.py input_image_path replacement_image_path

    input_image_path: Path to the input image containing the number plate to be replaced.
    replacement_image_path: Path to the replacement image used to replace the number plates.

4.  View the Result: The modified image with replaced number plate will be displayed.

# Example

    python numberplate.py tests/test.jpg numberplate.jpg

# Notes

- The script uses a pre-trained YOLO model to detect objects in the input image. Make sure you have the YOLO model and its configuration properly set up.
- Adjust the threshold value according to your requirements to control the sensitivity of object detection.
- The script will print "No numberplate detected" if no number plates are found in the input image.
