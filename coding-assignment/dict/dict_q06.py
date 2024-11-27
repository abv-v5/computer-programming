# finding a key with maximum value
# Dictionary
sales = {'John': 2500, 'Emily': 3000, 'Sophia': 2800, 'Mike': 3100}

# Finding key with max value
max_key = max(sales, key=sales.get)

print("Key with Maximum Value:", max_key)
