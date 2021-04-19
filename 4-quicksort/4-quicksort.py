# 4.1 Sum function
def sum(arr):
	if len(arr) == 0:
		return 0
	elif len(arr) == 1:
		return arr[0]
	else:
		return arr.pop(0) + sum(arr)

# print sum([1, 2, 3]) #6
# print sum([7]) # 7
# print sum([]) # 0

# 4.2 Count number of items in a list
def count(arr):
	if len(arr) == 0:
		return 0
	else:
		return 1 + count(arr[1:]) # [1:] means from second item to the end

# print count([1, 2, 3])
# print count([])

# 4.3 Maximum number in a list
def max(arr):
	if len(arr) == 1:
		return arr[0]
	elif len(arr) == 0:
		return "error: list must contain at least one number!"
	else:
		sub_max = max(arr[1:])
		return sub_max if sub_max > arr[0] else arr[0]

# print max([1, 5, 2, 0, 100])
# print max([])
# print max([9])

# Quicksort code
def quicksort(arr):
	if len(arr) < 2:
		return arr
	else:
		pivot = arr[0]
		# create new sub-array consisting of remaining elements that are <= pivot
		less = [i for i in arr[1:] if i <= pivot]
		# create new sub-array consisting of remaining elements that are > pivot
		greater = [i for i in arr[1:] if i > pivot]
		return quicksort(less) + [pivot] + quicksort(greater)

# print quicksort([2, 1, 109, 20, 40, 10])