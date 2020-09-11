# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
import string
letters = string.ascii_uppercase

f = open('ciphertext.txt', 'r')
text = f.read()
f.close()

def crack_it(text):
	counts = {}
	frequency = ["E", "T", "A", "O", "H", "N", "R", "I", "S", "D", "L", "W", "U", "G", "F", "B", "M", "Y", "C", "P", "K", "V", "Q", "J", "X", "Z"]
	
	for char in text.upper():
		if char in letters:
			if counts.get(char):
				counts[char] += 1
			else:
				counts[char] = 1

	counts_list = list(counts.items())
	counts_list = sorted(counts_list, key=lambda a : a[1], reverse=True)
	text_frequency = [a[0] for a in counts_list]

	cypher = {}

	for i, char in enumerate(text_frequency):
		if char in letters:
			cypher[char] = frequency[i]

	decoded = []

	for char in text.upper():
		if char in letters:
			decoded.append(cypher[char])
		else:
			decoded.append(char)

	return "".join(decoded)

print(crack_it(text))



