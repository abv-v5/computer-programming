# count elements in list within given range
list=[10, 20, 30, 40, 40, 40, 70, 80, 99]
minimum_range=int(input())
maximum_range=int(input())
count=0
for x in list:
    if minimum_range <= x <= maximum_range:
        count=count+1
print(count) 