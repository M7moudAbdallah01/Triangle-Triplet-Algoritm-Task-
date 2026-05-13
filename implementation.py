# (sorting)
def insertionSort(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A
#===========================================================
# (non-recursive)
def has_triangle(A):
    insertionSort(A)

    for i in range(len(A) - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            return 1

    return 0

#===========================================================
def mergeSort(A):
    if len(A) > 1:
        # 1. Division Phase: Finding the mid and splitting the array
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]

        # Recursive calls to split the sub-arrays
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        # 2. Merge Phase: Sorting and merging the sub-arrays
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left in L or R
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
    return A

# (recursive)
def check_triangle(A, i):
    if i > len(A) - 3:
        return 0

    if A[i] + A[i + 1] > A[i + 2]:
        return 1

    return check_triangle(A, i + 1)


def has_triangle_recursive(A):
    mergeSort(A)
    return check_triangle(A, 0)

#===========================================================

# Data
A = [10, 50 , 1]

# non-recursive Result
print("non-recursive:", has_triangle(A.copy()))

# Recursive Result
print("Recursive:", has_triangle_recursive(A.copy()))