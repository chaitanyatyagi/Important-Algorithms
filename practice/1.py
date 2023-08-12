# def selectionsort(array):
#     n = len(array)
#     for i in range(n):
#         mn_indx = i
#         for j in range(i+1,n):
#             if array[j] < array[mn_indx]:
#                 mn_indx = j
#         array[i],array[mn_indx] = array[mn_indx],array[i]
#     return array

# print(selectionsort([5,9,2,4,10,7,4,6]))

# def bubblesort(array):
#     n = len(array)
#     for i in range(n):
#         for j in range(n-i-1):
#             if array[j] > array[j+1]:
#                 array[j],array[j+1] = array[j+1],array[j]
#     return array

# print(bubblesort([5,9,2,4,10,7,4,6]))

def mergesort(array):
    if len(array) <= 1: return
    mid = len(array)//2
    left,right = array[:mid],array[mid:]
    mergesort(left)
    mergesort(right)

    l,r,m = 0,0,0
    
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            array[m] = left[l]
            l += 1
        else:
            array[m] = right[r]
            r += 1
        m += 1
    while l < len(left):
        array[m] = left[l]
        m += 1
        l += 1
    while r < len(right):
        array[m] = right[r]
        m += 1
        r += 1
array = [5,9,2,4,10,7,4,6]
print(array)
mergesort(array)
print(array)