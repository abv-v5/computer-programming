# merging of two dictionaries
# Dictionaries to merge
dict1 = {'a': 5, 'b': 10, 'c': 15}
dict2 = {'b': 7, 'c': 3, 'd': 20}

# Merging dictionaries
merged_dict = dict1.copy()
for key, value in dict2.items():
    merged_dict[key] = merged_dict.get(key, 0) + value

print("Merged Dictionary:", merged_dict)
