# wrrite a function to find first missing positive inteoo
def first_missing_positive(nums):
    nums = set(nums)
    smallest = 1
    while smallest in nums:
        smallest += 1
    return smallest

# Test
print(first_missing_positive([3, 4, -1, 1]))  # 2
print(first_missing_positive([1, 2, 0]))      # 3
