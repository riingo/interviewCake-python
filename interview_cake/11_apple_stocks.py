# Given a list of stock prices where index = time and value = price of stock, write 
# a function to return best profit you can make with one purchase and one sale. 
# You must buy before you can sell, and you cannot buy and sell in the same step.

def max_profit(stocks): 
	if len(stocks) < 2: 
		return 0

	min_stock = stocks[0]
	max_profit = stocks[1] - min_stock

	for i in xrange(1, len(stocks)): # start at 2nd value
		if stocks[i] < min_stock: 
			min_stock = stocks[i]
		elif stocks[i] > min_stock: 
			max_profit = max(max_profit, stocks[i] - min_stock)

	return max_profit

# Tests
print max_profit([10, 7, 5, 8, 11, 9]) == 6
print max_profit([1, 2, 3, 4, 5]) == 4
print max_profit([10, 6, 5, 11, 1]) == 6
print max_profit([5, 4, 3, 2, 1]) == -1