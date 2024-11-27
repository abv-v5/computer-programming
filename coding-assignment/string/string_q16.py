'''
 Find the First Non-Repeating Character
Problem: Write a function to find the first non-repeating character in a string.

Scenario: You need to identify the first character in a string that does not repeat.
'''
def first_non_repeating_char(string):
    for i in range(len(string)):
        # Check if the character is unique in the string
        if string.count(string[i]) == 1:
            return string[i]
    return None  # Return None if no non-repeating character is found

# Example usage
input_string = "swiss"
output = first_non_repeating_char(input_string)
print(output)  # Output: "w"
