# rotate a list
def rotate_list(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

# Example
print(rotate_list([1, 2, 3, 4, 5, 6, 7], 3))  # Output: [5, 6, 7, 1, 2, 3, 4]
