#Code examples for manipulating the host computer running python scripts

#Third party library for manipulating the host's clipboard
#pip install pyperclip
import pyperclip
pyperclip.copy('Hello, World')
print(pyperclip.paste())

import shutil, os
from pathlib import Path

#Copy a file
shutil.copy('numbers.txt', 'numbers2.txt')

#Copy a folder and all of its subfolders and files
#shutil.copytree('data', 'data2')

#Move a file and rename it
shutil.move('numbers.txt', Path('data/n.txt'))

#Move it back
shutil.move(Path('data/n.txt'), 'numbers.txt')

#Delete a directory
#os.unlink('data2')

#Delete a file
os.unlink('numbers2.txt')

#Send it to the recycle bin
#pip install send2trash
import send2trash
shutil.copy('numbers.txt', 'numbers2.txt')
send2trash.send2trash('numbers2.txt')

#Walk through every file and folder in the home directory
def walk():
	for folder, subFolders, files in os.walk(Path.home()):
		print(folder)

		for subFolder in subFolders:
			print(folder + "/" + subFolder)

		for file in files:
			print(folder + "/" + file)

#walk()

import zipfile

#Create a zipfile
z = zipfile.ZipFile('test.zip', 'w')
z.write('numbers.txt', compress_type=zipfile.ZIP_DEFLATED)
z.close()

#Get info about the zip file
z = zipfile.ZipFile('test.zip')
print(z.namelist())
#['numbers.txt']
fi = z.getinfo('numbers.txt')
print(fi.file_size)
#29
print(fi.compress_size)
#30

#Extract all the files
z.extractall()

#Extract and move to new folder
z.extract('numbers.txt', 'data')

z.close()