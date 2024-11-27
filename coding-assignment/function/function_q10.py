# function to check a palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Ignore case and spaces
    return s == s[::-1]

# Test
print(is_palindrome("Racecar"))  # True
print(is_palindrome("hello"))    # False
