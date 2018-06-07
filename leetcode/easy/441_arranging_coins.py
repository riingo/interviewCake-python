# You have a total of n coins you want to form in a staircase shape, where 
# every k-th row must have exactly k coins. 
# Given n, find the total number of full staircase rows that can be formed. 

# Ex: n = 5
# You can form the rows: 
# o
# o o 
# o o 
# Because the third row is incomplete, we return 2. 

# Ex: n = 8
# You can form the rows: 
# o
# o o
# o o o
# o o
# We return 3. 

def num_staircases(n): 
	if n == 0: 
		return 0

	rows = 0 
	while n > 0: 
		if n < rows: 
			break 
		n -= rows 
		rows += 1

	return rows - 1

# Tests
print 2 == num_staircases(5)
print 3 == num_staircases(8)
print 4 == num_staircases(10)
print 0 == num_staircases(0)
