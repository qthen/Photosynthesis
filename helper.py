import numpy as np
from PIL import Image
#Helper functions - may become outdated as the model grows

char_to_ix = {}
for i in range(0, 26):
	char_to_ix[chr(ord('a') + i)] = i + 1
for i in range(0, 26):
	char_to_ix[chr(ord('A') + i)] = i + 26
char_to_ix[' '] = 53
char_to_ix['.'] = 54
char_to_ix[':'] = 55
char_to_ix[','] = 56
char_to_ix['?'] = 57
char_to_ix['"'] = 58
char_to_ix['\n'] = 59

print(char_to_ix['R'])
def char_to_index(character):
	return char_to_ix[character]

def image_array(filename):
	img = Image.open(filename)
	arr = np.array(img)
	return arr

def create_image(rgbArray):
	img = Image.fromarray(rgbArray, 'RGB')
	img.save('my.png')
	img.show()