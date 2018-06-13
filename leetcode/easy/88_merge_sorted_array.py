# Given two sorted arrays, merge them into one array. 

def merge(nums1, nums2): 
	return_array = []

	i = j = 0 
	while i < len(nums1) and j < len(nums2): 
		if nums1[i] <= nums2[j]: 
			return_array.append(nums1[i])
			i += 1
		else: 
			return_array.append(nums2[j])
			j += 1

	if i < len(nums1): 
		return_array += nums1[i:]

	if j < len(nums2): 
		return_array += nums2[j:]

	return return_array

# Tests
print merge([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]
print merge([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]