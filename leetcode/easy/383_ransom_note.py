# Given an arbitrary ransom note string and another string containing all letters from magazines, 
# determine if the ransom note can be constructed from the magazines. 
# Each letter in the magazine string can only be used once in your ransom note. 

def can_construct(ransom, magazine): 
	if len(ransom) > len(magazine): 
		return False

	# Go through the magazine and make a dict of the # of times each letter appears. 
	letter_dict = {}
	for letter in magazine: 
		if letter not in letter_dict: 
			letter_dict[letter] = 1
		else: 
			letter_dict[letter] += 1

	# Then check if the ransom note can be made
	for letter in ransom: 
		if letter not in letter_dict or letter_dict[letter] == 0: 
			return False
		letter_dict[letter] -= 1

	return True

# Tests
print False == can_construct("a", "b")
print True == can_construct("aa", "aab")
print False == can_construct("aa", "ab")
print True == can_construct("cat", "act")