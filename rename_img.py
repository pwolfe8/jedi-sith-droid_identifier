import shutil, os
os.chdir('./r2d2_classifier')

counter = 0
for name in os.listdir('./'):
	shutil.move(name, 'img' + str(counter) + '.jpg')
	counter += 1
