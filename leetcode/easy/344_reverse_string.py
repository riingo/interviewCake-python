# Given a string, reverse the string. 

def reverse_string(s): 
	reversed = list(s)
	reversed.reverse()
	return ''.join(reversed)

# Tests
print reverse_string("hello") == "olleh"