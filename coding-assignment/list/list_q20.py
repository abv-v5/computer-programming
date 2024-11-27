# remove all occurences of specific item in a list 
list=[5,10,15,20,34,20,25,65,20]
a=list.count(20)
for i in range(a):
    list.remove(20)
print(list)