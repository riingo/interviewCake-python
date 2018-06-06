# Merge two sorted lists into one sorted list. 

def merge_sorted(l1, l2): 
	# Keep two pointers, one for each list and keep comparing them. 
	if len(l1) == 0: 
		return l2
	elif len(l2) == 0: 
		return l1

	sorted_list = []
	p1, p2 = 0, 0

	while p1 < len(l1) and p2 < len(l2): 
		if l1[p1] <= l2[p2]: 
			sorted_list.append(l1[p1])
			p1 += 1
		else: 
			sorted_list.append(l2[p2])
			p2 += 1

	# Add the remaining bits of the other list if needed
	if p1 < len(l1): 
		sorted_list += l1[p1:]
	elif p2 < len(l2): 
		sorted_list += l2[p2:]

	return sorted_list

# Tests
test1_1 = [1, 2, 3, 4, 5]
test1_2 = []
print merge_sorted(test1_1, test1_2) == [1, 2, 3, 4, 5]

test2_1 = [3, 4, 6, 10, 11, 15]
test2_2 = [1, 5, 8, 12, 14, 19]
print merge_sorted(test2_1, test2_2) == [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

test3_1 = [1, 1, 1]
test3_2 = [1, 1, 1]
print merge_sorted(test3_1, test3_2) == [1, 1, 1, 1, 1, 1]

test4_1 = [1, 3, 4, 5]
test4_2 = [2]
print merge_sorted(test4_1, test4_2) == [1, 2, 3, 4, 5]
