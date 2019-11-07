# import the Python Image processing Library

from PIL import Image

 

# Create an Image object from an Image

imageObject  = Image.open("./frame962.jpg")

 

# Crop the iceberg portion
#cropped =       (distance from left edge-top left corner),(y-distance down top left corner);
                #(right bottom corner distance from left edge,(bottom right corner distance down from top)    )
cropped     = imageObject.crop((400,680,3500,1300))

 

# Display the cropped portion

cropped.show()
