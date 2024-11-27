# fid the words in the list which are greater than given lenght n 
list=["the","quick","brown","fox","jump","over","the","tree"]
n=4
word_lenght=[]
for i in list:
    if len(i) > n:
        word_lenght.append(i)
print(word_lenght)        