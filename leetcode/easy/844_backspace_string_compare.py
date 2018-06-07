# Given two strings, return if they are equal when typed into editors. A # symbol means a backspace. 
# Ex: s1 = "ab#c", s2 = "ad#c"
# Results in true since both become "ac" 

# O(N) time and O(N) space
def backspace_compare(s1, s2): 
	stack1, stack2 = [], []

	for character in s1: 
		if character == "#": 
			if len(stack1) > 0:
				stack1.pop()
		else: 
			stack1.append(character)

	for character in s2: 
		if character == "#": 
			if len(stack2) > 0: 
				stack2.pop()
		else: 
			stack2.append(character)


	return stack1 == stack2 

# Tests 
print True == backspace_compare("ab#c", "ad#c")
print True == backspace_compare("ab##", "c#d#")
print True == backspace_compare("a##c", "#a#c")
print False == backspace_compare("a#c", "b")






