import os
import cv2
import time  # Import the time module to use sleep

# Directory where the data will be stored
DATA_DIR = './dataf'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Number of classes (for 29 classes)
number_of_classes = 26
dataset_size = 300  # Number of images to collect for each class

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS,10)
 # Use the correct camera index (0 is typically default)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Create directories for each class (0 to 28)
for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print(f'Collecting data for class {j}...')

    # Wait for the user to be ready to start collecting images
    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" to start collecting images!', (100, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    # Introduce a 3-second delay after pressing Q
    print("Waiting for 3 seconds...")
    time.sleep(3)

    # Collect dataset_size images for the current class
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)  # Show the frame to the user

        # Save image to the corresponding class folder
        cv2.imwrite(os.path.join(DATA_DIR, str(j), f'{counter}.jpg'), frame)
        print(f'Collected {counter + 1}/{dataset_size} images for class {j}')

        counter += 1

# Release the webcam and close any open OpenCV windows
cap.release()
cv2.destroyAllWindows()

print("Image collection complete!")
