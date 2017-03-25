#Helper functions - may become outdated as the model grows


char_to_ix = {}
for i in xrange(1, 27):
	char_to_ix[chr(ord('a') + i)] = i
for i in xrange(27, 53):
	char_to_ix[chr(ord('A') + i)] = i + 26
char_to_ix[' '] = 53
char_to_ix['.'] = 54
char_to_ix[':'] = 55
char_to_ix[','] = 56
char_to_ix['?'] = 57
char_to_ix['"'] = 58
char_to_ix['\''] = 59

def char_to_index(character):
	return char_to_ix[character]



