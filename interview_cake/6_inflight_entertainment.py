# Given an integer representing flight length and a list of integers representing movie lengths, 
# return a boolean indicating whether there are two numbers in the movie lengths list whose sum 
# equals flight length. 

def are_two_movies(flight, movies): 
	if len(movies) < 2: 
		return False

	complementary_times = set()

	for movie in movies: 
		if movie in complementary_times: 
			return True 
		complementary_times.add(flight - movie)

	return False

# Tests 
print are_two_movies(10, [1, 2, 4, 8, 9])
print False == are_two_movies(10, [1, 2, 3, 4, 5])

# Now return the specific movie lengths in a tuple. 
def are_two_movies_tuples(flight, movies): 
	if len(movies) < 2: 
		return False

	complementary_times = {}

	for movie in movies: 
		if movie in complementary_times: 
			return (min(movie, complementary_times[movie]), max(movie, complementary_times[movie]))
		complementary_times[flight - movie] = movie

	return None

# Tests
print (2, 8) == are_two_movies_tuples(10, [1, 2, 4, 8, 9])
print None == are_two_movies_tuples(10, [1, 2, 3, 4, 5])