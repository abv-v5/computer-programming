'''
 Find the Longest Word in a String
Problem: Write a function to find the longest word in a given sentence.

Scenario: You need to highlight the longest word from a text document.
'''
def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word

input_sentence = "The quick brown fox"
output = find_longest_word(input_sentence)
print(output)  # Output: "quick"
