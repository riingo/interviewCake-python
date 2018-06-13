# Write a function that takes a list of unsorted_scores and the highest_possible_score
# and return a sorted list of scores in less than O(n log n) time. 

# Ex: unsorted_scores = [37, 89, 41, 65, 91, 53]
#HIGHEST_POSSIBLE_SCORE = 100
# Returns [91, 89, 65, 53, 41, 37]

def sort_scores(unsorted_scores, highest): 
	# Make an array of every value from 0 to highest 
	scores = [0] * (highest + 1) 

	for score in unsorted_scores: 
		scores[score] += 1

	return_scores = []
	for i, num_times in reversed(list(enumerate(scores))): 
		return_scores += [i] * num_times

	return return_scores

# Tests
print sort_scores([37, 89, 41, 65, 91, 53], 100) 
