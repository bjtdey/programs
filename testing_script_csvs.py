"""README
Install all the necessary requirements and run the script as:
python3 script_name.py -i source_folder -d destination_folder -m model
i)source_folder is the folder with which you want to test the model with
ii)destination folder is the folder to which you want to move the accepted images to 
Finally, we'll get the model accuracy in the terminal and get all the images and their scores in a csv file """

import matplotlib.pyplot as plt
import numpy as np
import os
import argparse
import csv
import tensorflow as tf
import shutil  
import random


ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',type=str,default='',help='path')
# ap.add_argument('-c','--csv',type=str,default='',help='path')
ap.add_argument('-m','--model',type=str,default='',help='path')
ap.add_argument('-d','--destination', type=str, default='true',
 help="path to destination folder")
args=vars(ap.parse_args())

dest = args["destination"]
os.mkdir(dest)
image_path=args['image']

def preprocessing_img(img_path):
    #Converting the image to tensor
    img = tf.keras.preprocessing.image.load_img(img_path,target_size=(224, 224),interpolation = "lanczos")
    #this function Loads the image and resizes it to the specified size using PIL(Nearest Neighbour)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    #this function converts the image to numpy Array
    img_array = np.expand_dims(img_array, axis=0)
    #(1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_array /= 255.
    #the numpy array are normalized between 0 and 1
    return img_array

ran_val=random.random()
# ran_val1=random.random()
str_ran_value=str(ran_val)
# str_ran_value1=str(ran_val1)
str_ran_value=str_ran_value+'.csv'
str_ran_value1="sample"+'.csv'

messi = args["model"]
model = tf.keras.models.load_model(messi)
images=os.listdir(image_path)
a=[]
b=[]
b_val=''
count_of_total_images=0
count_of__FP =0
for each_image in images:
    count_of_total_images+=1
   # print("messi")
   # print(each_image)
    
    try:
        # print(str(each_image))
        img_path = os.path.join(image_path,each_image)
       # print("img_path is:",img_path)
        new_image = preprocessing_img(img_path)
        pred = model.predict(new_image)
        print(each_image , pred)
        if pred[0][0]<0.5:
            val=pred[0][0]
            val=str(val)
            a.append(each_image)
            count_of__FP=count_of__FP+1

            b.append([each_image,val])          
            
        else:
            val=pred[0][0]
            val=str(val)
            b.append([each_image,val])
    except:
        print(each_image)
        continue
#To get the CSV file
csvfile=open(str_ran_value1,'w', newline='')
obj=csv.writer(csvfile)
for val in b:
    obj.writerow(val)
csvfile.close()

#to move the accepted images to a different folder
fi=open(str_ran_value,"x")
for i in a:
    s=str(i)
    #fi.write("\n")
    fi.write(s)
    fi.write(os.linesep)
fi.close()
#data moving script
src=image_path
fil=open(str_ran_value)
lines = fil.readlines()
for file_name in lines:
    # count_of__FP+=1
    try:
        
        source=src+'/'+file_name
        #print(source)
        val=shutil.move(source[:-1], dest)

    except:
        continue

fil.close()

rem_data=(count_of_total_images-count_of__FP)
print("text file created is:",str_ran_value)
print("total images processed are:",count_of_total_images)
print("total TN's or FN's are:",rem_data)
print("total FP's or TP's are/total images moved to destination are:",count_of__FP)

#finding accuracies
print("choose accuracies acc to your data")
fake_acc=(rem_data/(rem_data+count_of__FP))*100
print("If the tested data is fake then FAKE ACCURACY is :",fake_acc)


real_acc=(count_of__FP/(rem_data+count_of__FP))*100
print("if the tested data is real then REAL ACCURACY is :",real_acc)


