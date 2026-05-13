def sortArray(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A
# (non-recursive)
def has_triangle(A):
    sortArray(A)

    for i in range(len(A) - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            return 1

    return 0

#===========================================================
# (recursive)
def check_triangle(A, i):
    if i > len(A) - 3:
        return 0

    if A[i] + A[i + 1] > A[i + 2]:
        return 1

    return check_triangle(A, i + 1)


def has_triangle_recursive(A):
    sortArray(A)
    return check_triangle(A, 0)


#===========================================================

# Data
A = [10, 50 , 1]

# non-recursive Result
print("non-recursive:", has_triangle(A.copy()))

# Recursive Result
print("Recursive:", has_triangle_recursive(A.copy()))