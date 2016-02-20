# QUICK SORT

def swap(array, i, j):
	tmp = array[i]
	array[i] = array[j]
	array[j] = tmp


def sortHelper(array, first, last):
	if first >= last:
		return
	split = partition(array, first, last)
	sortHelper(array, first, split-1)
	sortHelper(array, split+1, last)

def partition(array, i, j):
		
	m = array[i]
	left = i + 1
	right = j
	done = False
	while not done:
		while array[left] <= m and left <= right:
			left += 1
		while array[right] >= m and left <= right:
			right -= 1
		# Swap found
		if left>=right:
			done =  True
		else:
			swap(array, left, right)
	swap(array, i, right)
	return right

a = [4,1,3,5,2]
sortHelper(a, 0, len(a)-1)
print(a)
