# program to find all index values of a given character in a given string
str = 'python programming op'
ch = 'o'
cc = str.count(ch)
t = 0
for i in range(cc):
    a = str.index(ch, t)
    print(a)
    t = a + 1