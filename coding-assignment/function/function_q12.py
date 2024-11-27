# function to find longest wword in a sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Test
print(longest_word("The quick brown fox jumps over the lazy dog"))  # jumps
