#function to find the second largest number in a list
def second_largest(nums):
    unique_nums = list(set(nums))
    if len(unique_nums) < 2:
        return None  # No second largest number
    unique_nums.sort()
    return unique_nums[-2]

# Test
print(second_largest([10, 20, 4, 45, 99]))  # 45
