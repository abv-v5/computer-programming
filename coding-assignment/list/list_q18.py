# zig zag list
def zigzag(nums):
    for i in range(len(nums) - 1):
        if (i % 2 == 0 and nums[i] > nums[i + 1]) or (i % 2 == 1 and nums[i] < nums[i + 1]):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums

# Example
nums = [4, 3, 7, 8, 6, 2, 1]
print(zigzag(nums))  # Output: [3, 7, 4, 8, 2, 6, 1]
