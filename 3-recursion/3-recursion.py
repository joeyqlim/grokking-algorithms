def countdown(i):
	print i
	if i <= 0: # base case
		return
	else:
		countdown(i-1) # recursive case

# countdown(3)

def factorial(x):
	if x == 1: # base case
		return 1
	else:
		return x * factorial(x-1) # recursive case

# print factorial(3)

# factorial(3) -> factorial(3-1) -> factorial(2-1)
# factorial(2-1) = 1
# factorial(3-1) = 2
	# x * factorial(2-1) = 2 * 1 = 2
# factorial(3) = 6
	# x * factorial(3-1) = 3 * 2 = 6