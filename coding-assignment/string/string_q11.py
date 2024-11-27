# remove consecutive duplicates
def remove_consecutive_duplicates(s):
    result = [s[0]]  # Start with the first character
    for char in s[1:]:
        if char != result[-1]:  # Only add the character if it's not the same as the last one
            result.append(char)
    return ''.join(result)

# Example
input_string = "aaabbbcccaaa"
print("After Removing Consecutive Duplicates:", remove_consecutive_duplicates(input_string))