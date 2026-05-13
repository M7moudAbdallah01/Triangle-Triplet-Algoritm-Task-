# (non-recursive)
def has_triangle(A):
    A.sort()

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
    A.sort()
    return check_triangle(A, 0)


#===========================================================

# Data
A = [10, 50 , 1]

# non-recursive Result
print("non-recursive:", has_triangle(A.copy()))

# Recursive Result
print("Recursive:", has_triangle_recursive(A.copy()))