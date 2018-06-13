# Given a list of times Teemo attacks and the length of time his poison lasts, 
# return seconds that the target will be poisoned. 

# Ex: [1, 4], 2 
# Output: 4
# At t = 1, Teemo poisons the target for 2 seconds. Then at t = 4, he posions the
# target again for a total of 4 seconds. 

# Ex: [1, 2], 2
# Output: 3
# At t = 1, Teemo poisons the target for 2 seconds. But at t = 2, he poisons the 
# target again. Poison does not stack, so this "replaces" the original poison and 
# lasts for 2 seconds. Thus the total is 3 seconds. 

def poison_time(times, duration): 
	if len(times) == 0: 
		return 0
	if duration == 1: 
		return len(times) 

	total_time = 0 
	previous_time = 0
	end_duration = None # Time that the current poisoning ends 
	for time in times: 
		if end_duration: 
			if time >= end_duration: # No overlap
				total_time += duration 
			if time < end_duration: # Overlap
				total_time += time - previous_time
		previous_time = time
		end_duration = time + duration 
	return total_time + duration

print poison_time([1, 4], 2) == 4
print poison_time([1, 2], 2) == 3
print poison_time([1, 2, 5], 1) == 3
print poison_time([1, 2, 3, 4, 5], 5) == 9