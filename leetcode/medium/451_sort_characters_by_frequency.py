# Given a string, sort it in descending order based on the frequency of characters. 
# Ex: "tree" -> "eert" or "eetr"
# Capital letters are considered different from lowercase. 

def sort_characters(s): 
	if len(s) < 2: 
		return s

	frequencies = {} 
	for character in s: 
		if character in frequencies: 
			frequencies[character] += 1
		else: 
			frequencies[character] = 1

	# Get a list of tuples representing key-value pairs 
	frequency_pairs = frequencies.items()

	# Sort them by descending frequency 
	# The lambda function basically says to apply the sorted method on the second element of the tuple * -1. 
	frequency_pairs = sorted(frequency_pairs, key = lambda x: -x[1]) 

	# Return the string 
	return_string = ''
	return ''.join(pair[0] * pair[1] for pair in frequency_pairs)

# Tests
test1 = "tree"
print sort_characters(test1) in ['eert', 'eetr']

test2 = "aaabbb"
print sort_characters(test2) in ['aaabbb', 'bbbaaa']

test3 = 'aAaAa'
print sort_characters(test3) in ['aaaAA']

