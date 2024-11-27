'''
Check if Two Strings are Rotations of Each Other
Problem: Write a function to check if one string is a rotation of another string.

Scenario: You are developing a circular queue system and need to check if one sequence is a rotated version of another.

Example:

Input: "abcde", "deabc"
Output: True

Input: "abcde", "abced"
Output: False

'''
def are_rotations(string1, string2):
    # Check if lengths of both strings are equal and string2 is a substring of string1 concatenated with itself
    return len(string1) == len(string2) and string2 in (string1 + string1)

# Example usage
input1, input2 = "abcde", "deabc"
print(are_rotations(input1, input2))  # Output: True

input1, input2 = "abcde", "abced"
print(are_rotations(input1, input2))  # Output: False
