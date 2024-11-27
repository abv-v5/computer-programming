# check if two strings are anagrams
def are_anagrams(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

# Test
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
