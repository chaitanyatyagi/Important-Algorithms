# Merge Sorting   -------> Time Complexity = O(nlogn)

def merge_sort(array):
    
    if len(array) <= 1: return array
    
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]

    merge_sort(left)
    merge_sort(right)

    i,j,k = 0,0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
    
    return array

if __name__ == '__main__':
    array = [1, 5, 4, 7, 3, 6, 2, 9]
    print(merge_sort(array))