#Iterate both lists simultaneously
#Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order
#  and items from list2 in reverse order.
list1 = [50,60,70,80]
list2 = [500,600,700,800]
for x, y in zip(list1,list2[::-1]):
    print(x,y)