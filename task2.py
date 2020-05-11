fn1 = open("1342-0.txt")
content = fn1.read()
list2 = content.strip(" ")
list3 = []

print(len(list2))
for words in list2:
  list3.append(list2.count(words))
print(list(zip(words,list3)))  
