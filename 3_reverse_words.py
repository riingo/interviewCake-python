# Reverse a list of words in place. Words are separated by spaces. 
# Ex: ['h', 'i', ' ', 'b', 'y', 'e'] => ['b', 'y', 'e', ' ', 'h', 'i']

def reverse_words(words): 
	if len(words) < 2: 
		return words
	if ' ' not in words: 
		return words

	# Reverse it normally
	reverse_inplace_subsequence(words, 0, len(words) - 1)

	# Now go through and reverse AGAIN when there is a space. 
	lower_index = 0
	for (i, letter) in enumerate(words): 
		if letter == ' ':
			reverse_inplace_subsequence(words, lower_index, i - 1)
			lower_index = i + 1

		# Reverse the last word too
		if i == len(words) - 1: 
			reverse_inplace_subsequence(words, lower_index, i)

	return words

def reverse_inplace_subsequence(lst, lower, upper): 
	while lower < upper: 
		temp = lst[lower]
		lst[lower] = lst[upper]
		lst[upper] = temp

		lower += 1
		upper -= 1
	return 

# Tests
test1 = ['h', 'i', ' ', 'b', 'y', 'e']
print ''.join(reverse_words(test1)) == 'bye hi'

test2 = ['c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l']
print ''.join(reverse_words(test2)) == 'steal pound cake'

test3 = ['f', 'o', 'o']
print ''.join(reverse_words(test3)) == 'foo'

