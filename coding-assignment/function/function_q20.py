# summ of squares of all even numbers in a list
def sum_of_squares_even(nums):
    return sum(x**2 for x in nums if x % 2 == 0)

# Test
print(sum_of_squares_even([1, 2, 3, 4, 5]))  # 20 (2^2 + 4^2)
