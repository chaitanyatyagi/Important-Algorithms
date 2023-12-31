# Insertion Sort --------> Time Complexity = O(n^2)
# Take an element and place it in its correct position

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array


if __name__ == '__main__':
    array = [1, 5, 4, 7, 3, 6,6, 2, 9]
    print(insertion_sort(array))
