import numpy as np
import os
import PIL.Image
import math

## Run
def scaleImage():
	## Scale images to 512x512
	size = (512,512)
	## file is a string for the filename\
	i = 0
	factor = 1
	for file in os.listdir("."):
		factor = 1
		if file.endswith(".jpg"):
			img = PIL.Image.open(file)
			width, height = img.size
			smallest = min(width,height)
			factor = int(math.ceil(float(512) / float(smallest)))
			## Adjust by the factor to keep aspect ratio
			width *= factor
			height *= factor
			img = img.resize((width, height))
			img = img.crop((0, 0, 512, 512))
			img.save("test_" + str(i) + ".png")
			i += 1

scaleImage()