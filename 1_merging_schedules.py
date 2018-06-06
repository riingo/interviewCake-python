# Merging ranges 

def merged_ranges(times): 
	sorted_times = sorted(times)
	merged_times = []

	for time in sorted_times: 
		if len(merged_times) == 0: 
			merged_times.append(time)
		previous_window = merged_times[-1] # Pull the latest range 
		if previous_window[0] <= time[0] and time[0] < previous_window[1]: # This time falls in existing window
			merged_times[-1] = (previous_window[0], max(time[1], previous_window[1]))
		elif time[0] == previous_window[1]: # Beginning of this time touches
			merged_times[-1] = (previous_window[0], time[1])
		else: # Does not overlap
			merged_times.append(time)
	return merged_times

# Tests
test1 = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
print (merged_ranges(test1) == [(0, 1), (3, 8), (9, 12)])

test2 = [(1, 2), (2, 3)]
print (merged_ranges(test2) == [(1, 3)])

test3 = [(1, 5), (2, 3)]
print (merged_ranges(test3) == [(1, 5)])

test4 = [(1, 10), (2, 6), (3, 5), (7, 9)]
print (merged_ranges(test4) == [(1, 10)])