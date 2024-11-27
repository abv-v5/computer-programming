# count the number of odd and even numbers in the tuple 
tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count = sum(1 for x in tuple if x %2==0)
odd_count = len(tuple)-even_count
print("even count",even_count)
print("odd count", odd_count)