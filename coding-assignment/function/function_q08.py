#Write a recursive function sum_digits that sums the digits of a given number.
# Define a function named 'sum_digits' that takes one parameter 'n'
def sum_digits(n):
    c = 0  # Initialize a counter variable to store the sum of digits
    # Check if the number 'n' is 0
    if n == 0:
        return 0  # Return 0 if 'n' is 0
    else:
        # While 'n' is not 0
        while n != 0:
            last_number = n % 10  # Get the last digit of 'n'
            n = n // 10  # Remove the last digit from 'n'
            c += last_number  # Add the last digit to the counter
        return c  # Return the sum of all digits

# Prompt the user to enter a number and convert the input to an integer
n = int(input("Enter the number: "))

# Call the 'sum_digits' function with the user's input as the argument and store the result
result = sum_digits(n)

# Print the sum of all digits
print("Sum of all digits is:", result)
