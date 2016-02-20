# SELECTION SORT

def findMinimumPosition(array, start, end):
	min = start
	for i in range(start, end+1):
		if array[i] < array[min]:
			min = i
	return min

def swap(array, i, j):
	tmp = array[i]
	array[i] = array[j]
	array[j] = tmp

def selectionSort(array):
	# Iterate over all elements in the array
	if len(array) == 1:
		return
	# Else we have at least 2 elements
	for i in range(len(array)-1):
		minPos = findMinimumPosition(array, i, len(array)-1)
		swap(array, i, minPos)
		print(array)


array = [3,2,5,4,4,6]

print(findMinimumPosition(array, 0, len(array)-1))

selectionSort(array)
print(array)
