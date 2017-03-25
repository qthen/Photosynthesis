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



