# Given a list of prefixes, replace every instance of a word that starts with a prefix 
# with the shortest prefix. 
# Ex: Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"

def replace_words(prefixes, sentence): 
	words = sentence.split(' ')

	# Put all the prefixes in a dictionary for faster lookup 
	prefix_dict = {}
	for prefix in prefixes: 
		prefix_dict[prefix] = prefix

	return_string = ''
	for word in words: 
		index = 1
		while index < len(word): 
			substring = word[:index]
			if substring in prefix_dict:
				break
			index += 1
		if return_string == '': 
			return_string = word[:index]
		else: 
			return_string = return_string + ' ' + word[:index]

	return return_string 

# Tests 
print replace_words(["cat", "bat", "rat"], "the cattle was rattled by the battery") == "the cat was rat by the bat"
print replace_words(["cat", "ca", "bat", "ba", "rat", "ra"], "the cattle was rattled by the battery") == "the ca was ra by the ba"