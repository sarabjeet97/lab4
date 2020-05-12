import hashlib
import filecmp
a= 0
b= 0

file_path1= "C:/Users/sarab/Desktop/inwk/python/lab4/new file.txt"
file1 = open(file_path1)
file_read1= file1.read()
hashobj1 = hashlib.md5(file_read1.encode())
a= hashobj1.hexdigest()  

file_path2 = "C:/Users/sarab/Desktop/inwk/python/lab4/new file2.txt"
file2 = open(file_path2)
file_read2 = file2.read()
hashobj2 = hashlib.md5(file_read2.encode())
b = hashobj2.hexdigest()

if a == b:
	print("same file")
else:
	print("different files")

comp = filecmp. cmp(file_path1 ,file_path2, shallow=True)
print(comp)