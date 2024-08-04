from inky import InkyPHAT
from inky.auto import auto
from PIL import Image

# Detect the display.
inky_display = auto()

# Variable for image path. ***UPDATE WITH CORRECT PATH***
image_path = '../Photos/<Album Name>/<Photo>'

# Load the image.
image = Image.open(image_path)

# Resize image to fit display.
image = image.resize(inky_display.resolution)

# Display the image.
inky_display.set_image(image)
inky_display.show()