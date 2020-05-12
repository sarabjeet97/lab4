import os

def walk(curr_dir):
	directory = os.listdir(root)
	for file in directory:
		path = os.path.join(root,file)
		if os.path.isfile(path) and path.endswith(".mp3"):
			print('filename', file)

		else:
			if os.path.isdir(path):
				walk(path)

			else:
				pass
print("no file")			

walk('test')						