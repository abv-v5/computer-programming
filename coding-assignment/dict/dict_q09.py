#Write a Python program to check whether a specific key exists in a dictionary.
# Dictionary
marks = {'Math': 90, 'Science': 85, 'English': 88}

# Check if key exists
subject = 'Science'
if subject in marks:
    print(f"{subject} exists in the dictionary.")
else:
    print(f"{subject} does not exist in the dictionary.")
