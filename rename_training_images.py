# quick script i made for renaming the bulk image download
# training data to something reasonable and consistent
import shutil, os, sys
image_dir = sys.argv[1]

print('rename images in folder: ' + image_dir + '  This includes: \n')
print(os.listdir(image_dir))
correct = raw_input("Would you like to continue? [y/n] ")
if(correct == 'y'):
	counter = 1
	for name in os.listdir(image_dir):
		filename = '\'' + str(name) + '\'' #put quotes around in case there are spaces in file name
		os.system('mv ' + image_dir+'/'+filename + ' ' + image_dir+'/'+'img'+str(counter)+'.jpg') #rename 
		counter += 1
	print('completed')
print('exiting')
