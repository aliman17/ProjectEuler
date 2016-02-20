# BUBBLE SORT

def swap(array, i, j):
	tmp = array[i]
	array[i] = array[j]
	array[j] = tmp

def traverseBack(array, position):
	# Compare this and previous position
	while position != 0:
		if array[position] < array[position-1]:
			swap(array, position, position-1)
		position -= 1
		
	
def bubbleSort(array):
	for position in range(len(array)):
		traverseBack(array, position)
		print(array)
array = [3,2,4,4,5, 2, 1]
bubbleSort(array)
print(array)

