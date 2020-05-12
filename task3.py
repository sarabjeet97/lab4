fn1 = open("1342-0.txt")
content = fn1.read()
list2 = list(content.strip(" "))
d = {}
t= []
s= []
f = 1
for words in list2:
  if words not in d:
    d[words] = list2.count(words)
  else:
    pass

for k,v in d.items():
  t.append((v,k))
s = (sorted(t, reverse=True))
for i,j in s:
  print(i,j)


