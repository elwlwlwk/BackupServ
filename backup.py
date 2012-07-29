import os
import time
import string

def go_root():
	while 'root' not in os.listdir('.'):
		os.chdir('..')

while True:
	print('back up')

	go_root()
	os.chdir('/home/elwlwlwk/datas')
	origin= os.listdir('.')

	go_root()
	os.chdir('/media/c/servbackup')
	dest= os.listdir('.')


	for files in origin:
		if files not in dest:
			filestr= str(files)
			os.system('cp -rf /home/elwlwlwk/datas/'+filestr.replace(' ', '\ ')+' /media/c/servbackup/')
			print(files)

	time.sleep(60)

