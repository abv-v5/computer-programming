# update values in a nested dictionary and add new keys if they don't exist
my_dict = {'user1': {'name': 'John', 'age': 30}, 'user2': {'name': 'Alice', 'age': 25}}
my_dict['user1']['age'] = 31  # Update age for user1
my_dict['user3'] = {'name': 'Bob', 'age': 22}  # Add new user3
print(my_dict)  # Output: {'user1': {'name': 'John', 'age': 31}, 'user2': {'name': 'Alice', 'age': 25}, 'user3': {'name': 'Bob', 'age': 37}}