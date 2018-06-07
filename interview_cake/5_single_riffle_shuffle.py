# Write a method to determine if a full deck of cards is a single riffle of two 
# other halves. 
# The question says we can assume the cards are integers 1 thru 52, but let's 
# do this where it could be any number of cards.

def is_single_riffle(deck, half1, half2):
	if len(deck) != len(half1) + len(half2): 
		return False

	index1, index2 = 0, 0
	for card in deck: 
		if index1 < len(half1) and card == half1[index1]:
			index1 += 1
		elif index2 < len(half2) and card == half2[index2]:
			index2 += 1
		else: 
			return False

	return index1 == len(half1) and index2 == len(half2)

# Tests
print True == is_single_riffle([1, 2, 3, 4, 5], [1, 2, 5], [3, 4])
print True == is_single_riffle([1, 2, 3, 4, 5], [3, 4, 5], [1, 2])
print False == is_single_riffle([1, 2, 3, 4, 5], [1, 3, 2, 5], [4])
print True == is_single_riffle([1, 1, 1, 1, 3, 1, 1, 1, 2], [1, 1, 3, 1], [1, 1, 1, 1, 2])