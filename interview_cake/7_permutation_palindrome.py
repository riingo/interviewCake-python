# Write an efficient function that checks if any permutation of an input string
# is a palindrome. 

def is_palindrome(s): 
	# To be a palindrome, if there are an even # of characters, each one must be 
	# matched with another. If there are odd #, then all except one must be matched. 
	seen_letters = {} 
	for letter in s: 
		if letter in seen_letters: 
			if seen_letters[letter] == 0: 
				seen_letters[letter] += 1
			else: 
				seen_letters[letter] -= 1
		else:
			seen_letters[letter] = 1

	values = seen_letters.values()

	if len(s) % 2 == 0: # even 
		return 1 not in values
	else: # odd
		return sum(values) == 1

# Tests
print is_palindrome("civic")
print False == is_palindrome("civil")
print is_palindrome("a")
print is_palindrome("aa")
print is_palindrome("aab")
print False == is_palindrome("ac")