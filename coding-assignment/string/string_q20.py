'''
 Check if a String Contains Only Digits
Problem: Write a function to check if a string contains only digits.

Scenario: You are validating a phone number input to ensure that it only contains numbers.

Example:

Input: "12345"
Output: True

Input: "123a5"
Output: False
'''
def contains_only_digits(s):
    return s.isdigit()

# Example usage
input1 = "12345"
input2 = "123a5"

print(contains_only_digits(input1))  # Output: True
print(contains_only_digits(input2))  # Output: False
