def has_triangle(A):
    A.sort()
    n = len(A)

    for i in range(n - 2):
        if A[i] + A[i+1] > A[i+2]:
            return 1

    return 0

# Example
A = [10, 2, 5, 1, 8, 20]
print(has_triangle(A))  # Output: 1