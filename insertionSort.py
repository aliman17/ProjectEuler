# INSERTION SORT

# Shift to the right
def shift(array, start, end):	
	for i in range(end, start-1, -1):
		array[i+1] = array[i]
		
# Find inserion place
def insertion(array, end, number):
	# Run all sorted numbers
	for i in range(end+1):
		# Check if it's ready to insert
		if array[i] > number:
			return i

def insertionSort(array):
	if len(array) == 1:
		return
	for i in range(1, len(array)):
		print(array)
		# Take a number
		number = array[i]
		posToInsert = insertion(array, i-1, number)
		shift(array, posToInsert, i-1)
		array[posToInsert] = number


array = [5,4,3,2,1]
insertionSort(array)
print(array)
