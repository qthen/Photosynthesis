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
	arr = np.array(img) # 640x480x4 array
	arr[20, 30] # 4-vector, just like above
	return arr

def create_image(rgbArray):
	img = Image.fromarray(rgbArray, 'RGB')
	img.save('my.png')
	img.show()