# Coin exchange problem 

def make_change(coins, target): 
	if target == 0: 
		return 1

	memo = [0] * (target + 1)
	memo[0] = 1

	for coin in coins: 
		for i, amount in enumerate(memo): 
			if i == coin: 
				memo[i] += 1
			elif i > coin: 
				memo[i] = amount + memo[i - coin]


	return memo[target]

# Tests
print make_change([1, 2, 5], 5) # 11111, 1112, 122, 5 = 4
print make_change([1, 2, 5], 7) # 1111111, 111112, 11122, 1222, 115, 25 = 6
print make_change([1, 2, 5], 11)
#  0 1 2 3 4 5
# [0 0 0 0 0 0]
# [1 0 0 0 0 0]
# [1 1 0 0 0 0]
# [1 1 1 0 0 0]
# [1 1 1 1 1 1]
# [1 1 2 1 1 1]
# [1 1 2 2 1 1]
# [1 1 2 2 3 1]
# [1 1 2 2 3 3]
# [1 1 2 2 3 4]