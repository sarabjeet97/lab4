#first program

fn1 = open("1342-0.txt")
content = fn1.read()
list2 = content.strip(" ")
list3 = " "
list4 = " "
for words in list2:
  
  if words == " " or words == " ,":
    list3= list2.replace(" ","")
    list4 = list3.strip("#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
  else:
    pass

print(list4.lower())

