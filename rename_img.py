#for renaming the bulk image download
import shutil, os, sys
image_folder = sys.argv[0]
counter = 0
for name in os.listdir('./'):
	shutil.move(name, 'img' + str(counter) + '.jpg')
	counter += 1
