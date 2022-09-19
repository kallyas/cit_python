import csv
import numpy as np
import cv2
import glob
import time

start_time = time.time()

# path of the folder containing images
path = "C:/Users/Admin/Documents/programming/cit_python/images"
images = (".jpg", ".png", ".jpeg")

# iterate over all the images in the folder
for file in glob.iglob(path + "/*"):
    if file.endswith(images):
        # read the image
        img = np.array(cv2.imread(file))

        # save data to csv file
        with open('C:/Users/Admin/Documents/programming/cit_python/images/data.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(img.flatten())
            csvfile.close()
        print("Image saved to csv file")
    else:
        print("File not an image")
        break
print("program finished converting images to csv file in {} seconds".format(round(time.time() - start_time)))
