import os

for (root,dirs,file) in os.walk('test'):
	print('root', root)
	print('directory', dirs)
	print('file', file)