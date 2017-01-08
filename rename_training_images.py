#for renaming the bulk image download
import shutil, os, sys
image_folder = sys.argv[1]

print('rename images in folder: ' + image_folder + 'this includes: \n')
print(os.listdir(image_folder))
correct = raw_input("Would you like to continue? [y/n] ")
if(correct == 'y'):
	counter = 0
	for name in os.listdir(image_folder):
		shutil.move(name, 'img' + str(counter) + '.jpg')
		counter += 1	
	print('completed')


print('exiting')




