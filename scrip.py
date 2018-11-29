import os
from PIL import Image,ImageStat 

FOLDER_PATH = '../restored/'
print('start')
for filename in os.listdir(FOLDER_PATH):
	try: # These next functions may produce an exception
  		image = Image.open(FOLDER_PATH+filename)
  		# image.verify()
  		stats = ImageStat.Stat(image);
  		print('extrema',stats.extrema) #Min/max values for each band in the image.
  		print('count',stats.count) #Total number of pixels for each band in the image.
  		print('sum',stats.sum) #Sum of all pixels for each band in the image.
  		print('sum2',stats.sum2) #Squared sum of all pixels for each band in the image.
  		print('mean',stats.mean) #Average (arithmetic mean) pixel level for each band in the image.
  		print('median',stats.median) #Median pixel level for each band in the image.
  		print('rms',stats.rms) #RMS (root-mean-square) for each band in the image.
  		print('var',stats.var) #Variance for each band in the image.
  		print('stddev',stats.stddev) #Standard deviation for each band in the image.
	except (IOError, SyntaxError) as e: # These are the exceptions we're looking for
		print('Bad file:', filename)
print('end') # print out the names of corrupt files