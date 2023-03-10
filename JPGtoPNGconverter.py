import sys
import os
from PIL import Image

#grab the first and second argument
folder = sys.argv[1]
new_folder = sys.argv[2]

#path of the folder we are grabbing the images from
pathfolder = f'/Users/jemil/Desktop/{folder}'
#path where we want to create it
pathnew = f'/Users/jemil/Desktop/{new_folder}'


#check if new/ exist, if not create it
if not os.path.exists(new_folder):
	os.mkdir(pathnew)
	print(f'Folder {new_folder} created succesfully!')
else:
	print(f'{new_folder}, already exists')

#loop through pokedex
#convert to png and save to new folder

for pokemon in os.listdir(pathfolder):
	img = Image.open(f'{pathfolder}/{pokemon}')
	img.save(f'{pathnew}/{pokemon[:-4:]}.png')
	print('all done')




