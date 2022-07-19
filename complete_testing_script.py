from distutils import text_file
import shutil

# from sympy import re
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from efficientnet.tfkeras import EfficientNetB0
import numpy as np
import os
import argparse
import csv
import cv2
import pandas as pd 
# import efficientnet.keras

ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',type=str,default='',help='path')
ap.add_argument('-m','--model',type=str,default='',help='model')
# ap.add_argument('-c','--csv',type=str,default='',help='model')
args=vars(ap.parse_args())

image_folder_path=args['image']
models_folder_path=args['model']
# c=args['csv']
c=models_folder_path

print(models_folder_path)

def load_image(img_path, show=False):
    img = image.load_img(img_path, target_size=(224, 224),interpolation='lanczos')
    img_tensor = image.img_to_array(img)# (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)# (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    if show:
        plt.imshow(img_tensor[0])                           
        plt.axis('off')
        plt.show()
    return img_tensor
    
model_list = os.listdir(models_folder_path)
for m in model_list:
    print(m)
    # os.mkdir(models_folder_path+"/"+str(m.split('.h')[0]))
    f=models_folder_path+"/"+str(m.split('.h')[0])
    os.mkdir(f)
    my_list = []
    csv_file_name = m.split('.h')[0]+'.csv'
    csv_path = os.path.join(c,csv_file_name)
    
    # txt_file = m.split('.h')[0]+'.txt'
    txt_path = os.path.join(c,'model_accuracies.txt')
    fieldnames=['image_name','class','pred_score']
    
    model_path = os.path.join(models_folder_path,m)
    model = load_model(model_path)
    print(model)
    # print(model.summary())
    for each_fol in os.listdir(image_folder_path):
        images=os.listdir(os.path.join(image_folder_path, each_fol))
        # os.mkdir(image_path+'_after_testing')
        for each_image in images:
            print(each_image)
            img_path = os.path.join(image_folder_path, each_fol,each_image)
            new_image = load_image(img_path)
            pred = model.predict(new_image)[0][0]
            print(pred)
            x=float(pred)
            if "real" in str(each_fol):
                if x>=0.5:
                    if not os.path.exists(f+"/fp"):
                        os.mkdir(f+"/fp")
                    shutil.copy(img_path,f+"/fp")
            elif "fake" in str(each_fol):
                if x<0.5:    
                    if not os.path.exists(f+"/fn"):
                        os.mkdir(f+"/fn")
                    shutil.copy(img_path,f+"/fn")
            my_list.append((each_image,each_fol,pred))
            # img = cv2.imread(img_path)
            # cv2.imwrite(image_path+'_after_testing/'+str(pred[0])+'.png',img)
    df = pd.DataFrame(my_list,columns=fieldnames)
    print(df)
    df.to_csv(csv_path,index=False)

    total_real_images_count = df['class'].value_counts()['real']
    total_fake_images_count = df['class'].value_counts()['fake']
    # print(df.dtypes)
    df1 = df.loc[df['pred_score']<0.5]
    df2 = df1.loc[df['class']=='real']
    total_pred_real_images_count = df2['class'].value_counts()['real']
    # print(total_pred_real_images_count)

    df1 = df.loc[df['pred_score']>=0.5]
    df2 = df1.loc[df['class']=='fake']
    total_pred_fake_images_count = df2['class'].value_counts()['fake']
    df3 = df2.loc[df['class']=='real']
    # print(total_pred_fake_images_count)

    real_accuracy = (total_pred_real_images_count/total_real_images_count)*100
    fake_accuracy = (total_pred_fake_images_count/total_fake_images_count)*100
    print(real_accuracy,fake_accuracy)
    txt_file = open(txt_path,'a+')
    txt_file.write('\n----------------------------------\n')
    txt_file.write('Model name : '+m+'\n')
    txt_file.write('real_accuracy = '+str(real_accuracy)+'\n')
    txt_file.write('fake_accuracy = '+str(fake_accuracy)+'\n')
    txt_file.close()