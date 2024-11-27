#Define a function gcd that calculates the greatest common divisor of two numbers using recursion.
# Define a function named 'gcd' that takes two parameters 'a' and 'b'
def gcd(a, b):
    # Base case: if 'b' is 0, return 'a' (because the GCD of any number and 0 is the number itself)
    if b == 0:
        return a
    else:
        # Recursive case: call the 'gcd' function with 'b' and 'a % b'
        return gcd(b, a % b)

# Prompt the user to enter the first number and convert the input to an integer
a = int(input("Enter the first number: "))

# Prompt the user to enter the second number and convert the input to an integer
b = int(input("Enter the second number: "))

# Call the 'gcd' function with the user's inputs as arguments and print the result
print("Greatest common divisor is:", gcd(a, b))