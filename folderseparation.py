import os
import pandas as pd 
import numpy as np 
from shutil import copyfile
import cv2

	 
import os
outPath = "/home/samanth/Downloads/1_jio_re_verification_data/Jio_re_vef_prod_frommay02/image_1/"
outPath2 = "/home/samanth/Downloads/1_jio_re_verification_data/Jio_re_vef_prod_frommay02/image_2/"

rootdir = os.getcwd()+"/rd_output/"

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        #print(filepath)
        img = cv2.imread(filepath)
        if filepath.endswith("_image.png"):
        	cv2.imwrite(outPath+file,img)
        else:
         	cv2.imwrite(outPath2+file,img)	

       