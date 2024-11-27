#count strings with same start and same end 
words=["abc","abca","121","1234"]
count=0
for word in words:
    if len(word)>1 and word[0]==word[-1]:
        count=count+1
print(count)
