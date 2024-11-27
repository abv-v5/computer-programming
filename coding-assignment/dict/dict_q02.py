# using dictionary to swap keys and values
# Problem: You want to swap the keys and values in a dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}
swapped_dict = {v: k for k, v in my_dict.items()}
print(swapped_dict)  # Output: {1: 'a', 2: 'b', 3: 'c'}
