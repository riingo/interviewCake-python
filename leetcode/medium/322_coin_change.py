# Given an array of coins and target amount, compute the fewest number of coins 
# you need to make that amount. 

def min_coins(coins, amount): 
	if amount == 0: 
		return 0

	# Memo to keep track of min number for each target value
	memo = [-1] * (amount + 1) 
	memo[0] = 0

	for coin in coins: 
		for i in xrange(len(memo)): 
			if coin == i: 
				memo[i] = 1 # Need one coin (minimum) to make that amount.
			elif i > coin: 
				potential = 1 + memo[i - coin]
				if potential > 0 and memo[i] > 0: 
					memo[i] = min(1 + memo[i - coin], memo[i]) 
				elif potential > 0 and memo[i] < 0: 
					memo[i] = potential

	return memo[amount]

# Tests
print min_coins([1, 2, 5], 5) 
print min_coins([2], 3)
print min_coins([1, 2, 5], 11)

# 0  1  2  3  4  5
# 0 -1 -1 -1 -1 -1 
# 0  1 -1 -1 -1 -1
# 0  1  2  3  4  5