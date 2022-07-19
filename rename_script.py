from PIL import Image 
import argparse
import random
import os
import copy
from random import random
from time import sleep

###run this script as : python3 script_name.py -i images -f objects

#1111111111111111111111111111111

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="",
    help="path to input image file") #images folder
#ap.add_argument("-f", "--folder", type=str, default="",
 #   help="path to input image file") #object folder
args = vars(ap.parse_args())
images = args["image"]

#folder = args["folder"]
#list1 = os.listdir(images) # dir is your directory path
#count1 = len(list1)
#list2 = os.listdir(folder) # dir is your directory path
#count2 = len(list2)
#res=count1*count2*12
#print("Target images: ",res)
count=0
image_path_output = 'output'
for fl in os.listdir(images):
    if fl == ".DS_Store" or fl == "_DS_Store":
        print("stupid files")
    else:
        image0 = os.path.join(images,fl)
        Image1 = Image.open(image0)

        val= random()

        Image1.save(str(image_path_output) + "/" + "_pap_1_" +str(val)+ ".jpg")

        # for i in os.listdir(folder):
        #     print("target images: {}, done with {} images".format(res,count))
        #     count=count+12
        #     image0 = os.path.join(images,fl)
        #     a0=1705
        #     b0=1296
        #     Image1 = Image.open(image0)
        #     # Image1 = Image.grayscale(Image1)
        #     Imageres1=Image1.resize((b0,a0))
        #     Image1copy=Imageres1.copy()
        #     Image1acopy=Imageres1.copy()
        #     Image1bcopy=Imageres1.copy()
        #     Image1ccopy=Imageres1.copy()
        #     Image1dcopy=Imageres1.copy()
        #     Image1ecopy=Imageres1.copy()
        #     Image1fcopy=Imageres1.copy()
        #     Image1gcopy=Imageres1.copy()
        #     Image1hcopy=Imageres1.copy()
        #     Image1icopy=Imageres1.copy()
        #     Image1jcopy=Imageres1.copy()
        #     Image1kcopy=Imageres1.copy()
        #     Image1lcopy=Imageres1.copy()
        #     # Image1mcopy=Imageres1.copy()
        #     # Image1ncopy=Imageres1.copy()
        #     # Image1ocopy=Imageres1.copy()
        #     # Image1pcopy=Imageres1.copy()
        #     # Image1qcopy=Imageres1.copy()
        #     # Image1rcopy=Imageres1.copy()
        #     # Image1scopy=Imageres1.copy()
        #     image2 = os.path.join(folder,i)
        #     Image3 = Image.open(image2)
        #     # Image3 = Image.grayscale(image3)
        #     a1=82
        #     b1=38
        #     diff_num_sizes = 6
        #     a11 = 1.15
        #     for z in range(3,diff_num_sizes):
        #           a1 = 192
        #           b1 = 68
        #           print(a11)
        #           a1 = a1 * a11
        #           print(a1)
        #           b1 = b1 * a11
        #           print(b1)
        #           Imageres2=Image3.resize((int(a1),int(b1)))

        #           value = random()
        #           Image2cp = Imageres2.copy()
        #           fl2 = fl.split('.')[0]
        #           rr = Image1copy.paste(Image2cp,(700,60))
        #           # Image1copy.grayscale(Image1copy)
        #           Image1copy.save(str(image_path_output) + "/" + "_pap_1_" + str(fl2)+str(value)+ ".jpg")

        #           value = random()
        #           rr = Image1acopy.paste(Image2cp,(600,274))
        #           # Image1acopy.grayscale(Image1acopy)
        #           Image1acopy.save(str(image_path_output) + "/" + "_pap_2_" + str(fl2)+str(value)+ ".jpg")

        #           value = random()
        #           rr = Image1bcopy.paste(Image2cp,(700,539))
        #           # Image1bcopy.grayscale(Image1bcopy)
        #           Image1bcopy.save(str(image_path_output) + "/" + "_pap_3_" + str(fl2)+str(value)+ ".jpg")

        #           value = random()
        #           rr = Image1ccopy.paste(Image2cp,(750,787))
        #           # Image1ccopy.grayscale(Image1ccopy)
        #           Image1ccopy.save(str(image_path_output) + "/" + "_pap_4_" + str(fl2)+str(value)+ ".jpg")

        #           value = random()
        #           rr = Image1dcopy.paste(Image2cp,(725,1043))
        #           # Image1dcopy.grayscale(Image1dcopy)
        #           Image1dcopy.save(str(image_path_output) + "/" + "_pap_5_" + str(fl2)+str(value)+ ".jpg")

        #           value = random()
        #           rr = Image1ecopy.paste(Image2cp,(714,1299))
        #           # Image1ecopy.grayscale(Image1ecopy)
        #           Image1ecopy.save(str(image_path_output) + "/" + "_pap_6_" + str(fl2)+str(value)+ ".jpg")


        #           value = random()
        #           rr = Image1fcopy.paste(Image2cp,(80,90))
        #           # Image1fcopy.grayscale(Image1fcopy)
        #           Image1fcopy.save(str(image_path_output) + "/" + "_pap_7_" + str(fl2)+str(value)+ ".jpg")

        #           value = random()
        #           rr = Image1gcopy.paste(Image2cp,(60,274))
        #           # Image1gcopy.grayscale(Image1gcopy)
        #           Image1gcopy.save(str(image_path_output) + "/" + "_pap_8_" + str(fl2)+str(value)+ ".jpg")

        #           value = random()
        #           rr = Image1hcopy.paste(Image2cp,(65,530))
        #           # Image1hcopy.grayscale(Image1hcopy)
        #           Image1hcopy.save(str(image_path_output) + "/" + "_pap_9_" + str(fl2)+str(value)+ ".jpg")

        #           value = random()
        #           rr = Image1icopy.paste(Image2cp,(90,787))
        #           # Image1icopy.grayscale(Image1icopy)
        #           Image1icopy.save(str(image_path_output) + "/" + "_pap_10_" + str(fl2)+str(value)+ ".jpg")

        #           value = random()
        #           rr = Image1jcopy.paste(Image2cp,(90,1043))
        #           # Image1jcopy.grayscale(Image1jcopy)
        #           Image1jcopy.save(str(image_path_output) + "/" + "_pap_11_" + str(fl2)+str(value)+ ".jpg")

        #           value = random()
        #           rr = Image1kcopy.paste(Image2cp,(150,1299))
        #           # Image1kcopy.grayscale(Image1kcopy)
        #           Image1kcopy.save(str(image_path_output) + "/" + "_pap_12_" + str(fl2)+str(value)+ ".jpg")

        #           value = random()
        #           rr = Image1lcopy.paste(Image2cp,(164,1200))
        #           # Image1lcopy.grayscale(Image1lcopy)
        #           Image1lcopy.save(str(image_path_output) + "/" + "_pap_13_" + str(fl2)+str(value)+ ".jpg")
        #           # rr = Image1mcopy.paste(Image2cp,(20,18))
        #           # Image1mcopy.save(str(image_path_output) + "/" + "_pap_1_" + str(fl2)+str(value)+ ".jpg")
        #           # rr = Image1ncopy.paste(Image2cp,(20,18))
        #           # Image1ncopy.save(str(image_path_output) + "/" + "_pap_1_" + str(fl2)+str(value)+ ".jpg")
        #           # rr = Image1ocopy.paste(Image2cp,(20,18))
        #           # Image1ocopy.save(str(image_path_output) + "/" + "_pap_1_" + str(fl2)+str(value)+ ".jpg")
        #           # rr = Image1pcopy.paste(Image2cp,(20,18))
        #           # Image1pcopy.save(str(image_path_output) + "/" + "_pap_1_" + str(fl2)+str(value)+ ".jpg")
        #           # rr = Image1qcopy.paste(Image2cp,(20,18))
        #           # Image1qcopy.save(str(image_path_output) + "/" + "_pap_1_" + str(fl2)+str(value)+ ".jpg")
        #           # rr = Image1rcopy.paste(Image2cp,(20,18))
        #           # Image1rcopy.save(str(image_path_output) + "/" + "_pap_1_" + str(fl2)+str(value)+ ".jpg")
        #           # rr = Image1srcopy.paste(Image2cp,(20,18))
        #           # Image1scopy.save(str(image_path_output) + "/" + "_pap_1_" + str(fl2)+str(value)+ ".jpg")


        #           a11 = a11 + 0.65
        #           print(a11)

        #           # count=count+12
        #           # image0 = os.path.join(images,fl)
        #           # a0=864
        #           # b0=595
        #           # Image1 = Image.open(image0)
        #           # Imageres1=Image1.resize((b0,a0))
        #           # Image1copy=Imageres1.copy()
        #           # image2 = os.path.join(folder,i)
        #           # Image3 = Image.open(image2)
        #           # a1=340
        #           # b1=128
        #           # Imageres2=Image3.resize((a1,b1))

        #           # value = random()
        #           # Image2cp = Imageres2.copy()
        #           # fl2 = fl.split('.')[0]
        #           # rr = Image1copy.paste(Image2cp,(20,18))
        #           # value = str(value).replace(".", "_")
        #           # Image1copy.save(str(image_path_output) + "/" + "_pap_1_" + str(fl2)+str(value)+ ".jpg")