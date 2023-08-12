# Bubble Sort -------> Time Complexity = O(n^2)
# Select the maximum and put it to the last

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


if __name__ == '__main__':
    array = [1, 5, 4, 7, 3, 6, 2, 9]
    print(bubble_sort(array))
