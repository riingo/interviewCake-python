# Given a long string of words, build word cloud data in the dictionary, 
# where key = words and value = number of times the word occurred. 
# What do we do with capitalized words and/or names? 
# Make reasonable decisions - for instance, "Add" and "add" should be one
# word with value 2.

def make_word_cloud(s): 
	cloud = {} 

	# For now, make every thing lower case 
	s = s.lower()
	s = s.replace('.', ' ').replace('"', ' ').replace(',', ' ')
	words = s.split(' ')

	for word in words: 
		if len(word) > 0:
			word = clean_word(word)
			if word in cloud: 
				cloud[word] += 1
			else: 
				cloud[word] = 1

	return cloud

def clean_word(word):
	# Remove leading 
	leading_index = 0
	return_word = word
	if word[0] in "-'":
		while leading_index < len(word): 
			if word[leading_index] in "-'": 
				leading_index += 1
			else: 
				break

	# Remove trailing
	trailing_index = len(word) - 1
	if word[len(word) - 1] in "-'":
		while trailing_index >= 0: 
			if word[trailing_index] in "-'": 
				trailing_index -= 1
			else: 
				break 

	return word[leading_index:trailing_index + 1]


# Tests
test1 = "Hello. My name is riingo, riingo is my name..."
print make_word_cloud(test1)

test2 = "---hi--- my name is ri-ingo ''and'' ...i... can code'''''''"
print make_word_cloud(test2)
