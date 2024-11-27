# python program to find frequency of each string literal
st = 'python programming op'
khali = ''
for ch in st:
    if ch not in khali:
        print(f"{ch}: {st.count(ch)}")
    khali += ch