import os
import random
import argparse
import shutil


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image_folder", type=str, default="",
	help="path to input image_folder")
ap.add_argument("-d", "--destination", type=str, default="",
	help="path to input image_folder")
ap.add_argument("-n", "--number of images", type=int, default="",
	help="path to input image_folder")
args = vars(ap.parse_args())

for i in range(args["number of images"]):
	filename = random.choice(os.listdir(args["image_folder"]))
	path = os.path.join(args["image_folder"], filename)
	#print(path)
	shutil.move(path,args["destination"])
	# shutil.move(x, dest)
