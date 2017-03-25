#Helper functions - may become outdated as the model grows

char_to_ix = {}
for i in xrange(0, 26):
	char_to_ix[chr(ord('a') + i)] = i
for i in xrange(0, 26):
	char_to_ix[chr(ord('A') + i)] = i + 26
char_to_ix[' '] = 52
char_to_ix['.'] = 53

def char_to_index(character):
	return char_to_ix[character]

def image_array(filename):
	img = Image.open(filename)
	arr = np.array(img)
	arr[20, 30]
	return arr

def create_image(rgbArray):
	img = Image.fromarray(rgbArray, 'RGB')
	img.save('my.png')
	img.show()
	
	import numpy as np
	import os
	from PIL import Image
	import PIL.Image
	import math
	
## Gets all files where the py file is
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
			factor = math.ceil(512 / smallest)
			## Adjust by the factor to keep aspect ratio
			width *= factor
			height *= factor
			img = img.resize((width, height))
			img = img.crop((0, 0, 512, 512))
			img.save("test_" + str(i) + ".png")
			i += 1
