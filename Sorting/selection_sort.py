# Selection Sorting -------> Time Complexity = O(n^2)

def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(min_index+1, n):
            if array[min_index] > array[j]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array


if __name__ == '__main__':
    array = [1, 5, 4, 7, 3, 6, 2, 9]
    print(selection_sort(array))
