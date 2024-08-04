from inky import InkyPHAT
from PIL import Image
from inky.auto import auto
import os
import time

# Detect the display.
inky_display = auto()

# Variable for the image path. ***UPDATE WITH CORRECT PATH***
directory_path = '../Photos/<Album Name>/'

# Create list of images.
image_list = [f for f in os.listdir(directory_path)]

# Loop forever.
while True:
    # Loop through images in list.
    for name in image_list:
        # Create image path variable with directory and image name.
        image_path = os.path.join(directory_path, name)
        # Open the image.
        image = Image.open(image_path)
        # Resize image for display.
        image = image.resize(inky_display.resolution)
        # Display the image.
        inky_display.set_image(image)
        inky_display.show()
        # Display refresh rate 40 seconds.
        # Pause on image for 1 hour. ***UPDATE VALUE FOR LONGER DURATION***
        time.sleep(3600)
