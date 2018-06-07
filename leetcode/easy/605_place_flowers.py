# A flowerbed is represented with an array of 0 and 1's where 0 = empty and 1 = has flower. 
# Given n, the number of new flowers, determine whether the flowers can be planted such that 
# no flower is adjacent to another. 

def can_plant(flowerbed, n):
	previous = 0 # The edge is okay!
	for (i, spot) in enumerate(flowerbed): 
		if n == 0: 
			return True
		
		if previous == 0 and spot == 0: 
			# Check if the next spot is a 1
			if i + 1 < len(flowerbed) and flowerbed[i+1] == 1: # Can't plant!
				previous = spot 
			else: 
				previous = 1
				n -= 1
		else: 
			previous = spot

	return n == 0


# Tests
print True == can_plant([1, 0, 0, 0, 1], 1)
print False == can_plant([1, 0, 0, 0, 1], 2)
print True == can_plant([0, 0, 1, 0, 0], 2)
print False == can_plant([1,0,0,0,0,1], 2)
print True == can_plant([0, 0, 0], 2)
print True == can_plant([0], 1)
print False == can_plant([1], 1)