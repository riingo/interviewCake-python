# There are N rooms and you start in room 0. Each room has a distinct number 0 through N-1. 
# Each room has keys to access the next room. Return whether we can enter every room. 

# Ex: [[1],[2],[3],[]]
# True, we start in room 0 -> key to room 1 -> key to room 2 -> key to room 3 -> done
# Ex: [[1,3],[3,0,1],[2],[0]]
# False, we start in room 0 -> key to room 1 and 3 -> key to room 3, 0, and 1 -> no key to room 2

def can_visit_all_rooms(rooms): 
	if len(rooms) < 2: 
		return True 

	# Walk through all the rooms and see if the keys we have form the consecutive numbers up to n - 1. 
	visited = set() 
	visited.add(0) # room 0 always visited
	to_visit = set() # We use set since we don't care about duplicate keys

	# Start with the first room, room 0. 
	for key in rooms[0]: 
		to_visit.add(key)

	# Visit all the rooms we can
	while len(to_visit) > 0: 
		next_key = to_visit.pop()
		if next_key not in visited: 
			visited.add(next_key)
			next_room_keys = rooms[next_key]
			to_visit.update(next_room_keys)

	# Check if all the rooms were visited 
	return len(visited) == len(rooms)

# Tests
print can_visit_all_rooms([[1], [2], [3], []])
print False == can_visit_all_rooms([[1,3],[3,0,1],[2],[0]])
print can_visit_all_rooms([[1], [1, 0]])



