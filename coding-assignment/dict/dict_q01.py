# sorting a dictionary by keys or values
my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'mango': 3}

# Sort by keys
sorted_by_keys = dict(sorted(my_dict.items()))
print(sorted_by_keys)  # Output: {'apple': 5, 'banana': 2, 'mango': 3, 'orange': 8}

# Sort by values
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_by_values)  # Output: {'banana': 2, 'mango': 3, 'apple': 5, 'orange': 8}