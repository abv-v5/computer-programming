# Problem: You want to count the occurrences of items in a list and store the result in a dictionary.

items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
count_dict = {}
for item in items:
    count_dict[item] = count_dict.get(item, 0) + 1
print(count_dict)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}