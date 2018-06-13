# Given two arrays write a function to compute their intersection 

def get_intersection(num1, num2): 
	num1_set = set(num1) 
	num2_set = set(num2) 

	return list(num1_set & num2_set)

print get_intersection([1, 2, 2, 1], [2, 3, 4]) == [2]
print get_intersection([1, 2, 3], [4, 5, 6]) == []
print get_intersection([1, 2, 3, 4], [5, 4, 2, 1, 1]) == [1, 2, 4]
