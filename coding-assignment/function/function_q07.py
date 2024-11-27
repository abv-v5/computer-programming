#Write a function filter_even that takes a list and returns a list of only the even numbers.
# Define a function named 'filter_even' that takes one parameter 'numbers'
def filter_even(numbers):
    # Initialize an empty list to store even numbers
    even = []
    # Iterate over each number in the list 'numbers'
    for i in numbers:
        # Check if the number is even
        if i % 2 == 0:
            # If the number is even, append it to the 'even' list
            even.append(i)
        else:
            # If the number is not even, continue to the next iteration (this 'else' is not necessary, but included for clarity)
            continue
    # Print the filtered list of even numbers
    print("Filtered list is:", even)