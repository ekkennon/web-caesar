import string

def encrypt(text,rot):
	encrypted = ""
	for i in range(len(text)):
		encrypted += rotate_character(text[i],rot)
	return encrypted

def rotate_character(char,rot):
	if rot == -1:
		return char
	lower = char == char.lower()

	i = alphabet_position(char)
	if i == -1:
		return char

	i += rot
	while i > 25:
		i %= 26

	if lower:
		return string.ascii_lowercase[i]
	else:
		return string.ascii_uppercase[i]


def alphabet_position(letter):
	""" returns ascii number of lowercase letter """
	return string.ascii_lowercase.find(letter.lower())