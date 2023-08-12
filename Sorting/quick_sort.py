# Quick Sorting time complexity: O(n^2)
# Steps
# 1) Pick a pivot and place it in the correct order as in the sorted array
# 2) Pivot can be any random integer in the array, we will take first element
# 3) Now, all smaller integers than pivot are placed on the left side while all larger integers than pivot are placed on the right side.
# 4) Keep on doing this process.

def helper(array,low,high):
	pivot = array[low]
	i,j = low,high
	while i < j:
		while i <= high and array[i] <= pivot:
			i += 1
		while j >= low and array[j] >= pivot:
			j -= 1
		if i < j:
			array[i],array[j] = array[j],array[i]
	array[low],array[j] = array[j],array[low] 
	return j\
	
def quicksort(array,low,high):
	if low < high:
		pivotIndex = helper(array,low,high)
		quicksort(array,low,pivotIndex-1)
		quicksort(array,pivotIndex+1,high)

if __name__ == '__main__':
	array = [10, 7, 8, 9, 1, 5]
	N = len(array)
	print('Unsorted array:',array)
	quicksort(array, 0, N - 1)
	print('Sorted array:',array)
