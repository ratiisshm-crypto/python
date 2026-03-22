# Quick sort in python

# function to find the partition position
def partition(A, low, high):

    # choosing the rightmost element as pivot
    pivot = A[high]

    # pointer for great element
    i = low - 1

    # compare each element with the pivot
    for j in range(low, high):
        if A[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swaapping element at i with element at j
            (A[i], A[j]) = (A[j], A[i])

    # swap the pivot element with the greater element specified by i
    (A[i + 1], A[high]) = (A[high], A[i + 1])

    # return the position from whee the partition is done
    return i + 1

# function to perform quicksort
def quicksort(A, low, high):

    if low < high:
        # find pivot elements such that
        # elements smaller than the pivot are on the left
        # elemnts greater than the pivot are on the right
        pi = partition(A, low, high)

        # recursive call on the left of the pivot
        quicksort(A, low, pi - 1)

        # recursive call on the right of the pivot
        quicksort(A, pi + 1, high)
    
A = [8, 17, 22, 12, 0, 9, 16]
print("Unsorted array: ")
print(A)

n = len(A) - 1

quicksort(A, 0, n)

print('Sorted array:')
print(A)