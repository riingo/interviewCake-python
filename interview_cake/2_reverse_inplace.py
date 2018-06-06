# Reverse a list of characters in place 

def reverse_inplace(charas): 
	if len(charas) < 2: 
		return charas

	index1 = 0 
	index2 = len(charas) - 1

	while index1 < index2: 
		temp = charas[index1]
		charas[index1] = charas[index2]
		charas[index2] = temp
		index1 += 1
		index2 -= 1

	return charas 

# Tests
test1 = ['1', '2', '3', '4', '5']
print reverse_inplace(test1) == ['5', '4', '3', '2', '1']

test2 = ['1', '2', '3', '4']
print reverse_inplace(test2) == ['4', '3', '2', '1']

test3 = []
print reverse_inplace(test3) == []

test4 = ['hi']
print reverse_inplace(test4) == ["hi"]