def check_triangle(A, i):
    if i > len(A) - 3:
        return 0

    if A[i] + A[i+1] > A[i+2]:
        return 1

    return check_triangle(A, i + 1)

def has_triangle_recursive(A):
    A.sort()
    return check_triangle(A, 0)

A = [10, 2, 5, 1, 8, 20]
print(has_triangle_recursive(A))  