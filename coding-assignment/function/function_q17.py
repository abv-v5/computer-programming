# function to find the most frequent words in a given list of words. If there is a tie return the first string
def most_frequent_word(words):
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    max_count = max(freq.values())
    for word in words:
        if freq[word] == max_count:
            return word

# Test
print(most_frequent_word(["apple", "banana", "apple", "orange", "banana", "apple"]))  # apple
