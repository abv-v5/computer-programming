'''
Find All Permutations of a String
Problem: Write a function to generate all possible permutations of a given string.

Scenario: You are working on a password generator, and need to generate all possible combinations.
'''
def string_permutations(s, current=""):
    # Base case: when the string is empty, print the current permutation
    if len(s) == 0:
        print(current)
        return

    # Recursive case: generate permutations by fixing each character
    for i in range(len(s)):
        # Remove the current character from the string
        remaining = s[:i] + s[i+1:]
        # Recurse with the remaining characters
        string_permutations(remaining, current + s[i])

# Example usage
input_string = "abc"
string_permutations(input_string)
