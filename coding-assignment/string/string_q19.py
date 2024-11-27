'''
 Compress a String Using the Counts of Repeated Characters
Problem: Write a function to compress a string by replacing consecutive repeated characters with the character followed by the count.

Scenario: You are implementing a data compression algorithm.

Example:

Input: "aaabbcccc"
Output: "a3b2c4"
'''
def compress_string(s):
    result = ""  # Initialise an empty string for the result
    count = 1

    # Iterate through the string
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            # Increment count if the current character is the same as the previous one
            count += 1
        else:
            # Add the character and its count to the result
            result += s[i - 1] + str(count)
            count = 1  # Reset count for the next character

    # Add the last character and its count
    if s:
        result += s[-1] + str(count)

    return result

# Example usage
input_string = "aaabbcccc"
output = compress_string(input_string)
print(output)  # Output: "a3b2c4"
