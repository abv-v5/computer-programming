# program to find all index values of a given character in a given string
st = 'python programming op'
ch = 'o'
cc = st.count(ch)
t = 0
for i in range(cc):
    a = st.index(ch, t)
    print(a)
    t = a + 1