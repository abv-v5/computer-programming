#Write a function factorial that calculates the factorial of a given number.
# Define a function named 'factorial' that calculates the factorial of a number 'n'
def factorial(n):
    # Base case: if 'n' is 0, return 1 (because 0! = 1)
    if n == 0:
        return 1
    else:
        # Recursive case: return 'n' times the factorial of 'n-1'
        return n * factorial(n - 1)

# Prompt the user to enter a number and convert the input to an integer
n = int(input("Enter the number: "))

# Call the 'factorial' function with the user's input as the argument and store the result
result = factorial(n)

# Print the result of the factorial calculation
print(result)