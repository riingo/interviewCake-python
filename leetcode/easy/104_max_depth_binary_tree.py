# Given a binary tree find its maximum depth. 

class TreeNode(): 
	def __init__(self, x): 
		self.value = x
		self.right = None
		self.left = None 

def max_depth(root): 
	if not root: 
		return 0

	left_depth = right_depth = 0

	# Get max depth of left side 
	if (root.left): 
		left_depth = max_depth(root.left)

	# Get max depth of right side 
	if (root.right): 
		right_depth = max_depth(root.right)

	return 1 + max(left_depth, right_depth)

