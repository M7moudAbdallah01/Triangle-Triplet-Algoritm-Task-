# Non-Recursive 
def triangle(nums):

    n = len(nums)

    for i in range(1, n):

        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

    for i in range(n - 2):

        if nums[i] + nums[i + 1] > nums[i + 2]:
            return 1

    return 0

# Non-Recursive Result

nums1 = [10, 50, 1]
print("Non-Recursive (Ex1) :" ,triangle(nums1))  

nums2 = [10, 2, 5, 1, 8, 20]
print("Non-Recursive (Ex2) :"  , triangle(nums2))  


#===========================================================
# Recursive

def merge_sort(nums):

    if len(nums) > 1:

        mid = len(nums) // 2

        left = nums[:mid]
        right = nums[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

def check_triangle(nums, i):

    if i > len(nums) - 3:
        return 0

    if nums[i] + nums[i + 1] > nums[i + 2]:
        return 1

    return check_triangle(nums, i + 1)




def triangle_recursive(nums):

    merge_sort(nums)

    return check_triangle(nums, 0)


# Results

nums1 = [10, 50, 1]
print("Recursive (Ex1):", triangle_recursive(nums1))

nums2 = [10, 2, 5, 1, 8, 20]
print("Recursive (Ex2):", triangle_recursive(nums2))