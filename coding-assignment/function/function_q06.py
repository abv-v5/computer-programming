# Define a function named 'all_even' that takes one parameter 'numbers'
def all_even(numbers):
    # Check if all numbers in the list are even using a generator expression
    if all(num % 2 == 0 for num in numbers):
        # If all numbers are even, print True
        print(True)
    else:
        # If any number is not even, print False
        print(False)