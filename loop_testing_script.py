'''README:
Run the script as: python3 script_name.py -i images_folder -m models_folder
Note1: images_folder should contain folders with names "real","fake" for real data and fake data respectivelly(atleast one folder is accepted )
Note2: models_folder should contain atleast one model
Note3: we will get the best model's accuracy in "final.txt" file'''

import argparse
import os
import random
import shutil
import numpy as np
import tensorflow as tf

def preprocessing_img(image):
    # Converting the image to tensor
    img = tf.keras.preprocessing.image.load_img(image, target_size=(224, 224), interpolation="lanczos")
    # this function Loads the image and resizes it to the specified size using PIL(Nearest Neighbour)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    # this function converts the image to numpy Array
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.
    # the numpy array are normalized between 0 and 1
    return img_array

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--image', type=str, default='', help='path')
    ap.add_argument('-m', '--model', type=str, default='', help='path') #give the models folder
    # ap.add_argument('-d', '--destination', type=str, default='true',
    #                 help="path to destination folder")
    args = vars(ap.parse_args())
    # destination = args["destination"]
    image_path = args['image']
    ran_val=random.random()
    str_ran_value=str(ran_val)
    models_ = args["model"]
    # print(models_)
    models = os.listdir(models_)
    for folder in os.listdir(image_path):
        # print(folder)
        real_dest='real_dest'
        pathr=os.path.join(image_path,real_dest)
        fake_dest='fake_dest'
        pathf=os.path.join(image_path,fake_dest)
########## FOR FAKE ###############
        if folder=='fake':
            folder_fake = os.path.join(image_path, folder)
            images = os.listdir(folder_fake)
            # print(images)
            data_count = len(images)
            imgs = []
            val = 0
            a_val = ''
            each_model_ = ''
            count_of__FP = 0
            count_of_total_images = 0

            for each_model in models:
                model = os.path.join(models_, each_model)
                model = tf.keras.models.load_model(model)
                a = []
                count_of_total_images = 0

                for each_image in images:
                    count_of_total_images += 1
                    # print(each_image)
                    try:
                        # print(each_image)
                        img_path = os.path.join(folder_fake, each_image)
                        # print(img_path)
                        new_image = preprocessing_img(img_path)
                        # print(new_image)
                        pred = model.predict(new_image)
                        print(each_image, pred)
                        if pred[0][0] < 0.5:
                            a.append(each_image)
                        else:
                            continue
                    except:
                        # print(each_image)
                        continue
                val = len(a)
                print("fps :",val)

                tns=count_of_total_images-val
                accuracy=(tns/(val+tns))*100
                # print("tns:",tns)
                # print("accuracy:",accuracy)           
                if val == 0:
                    print("fake accuracy is 100%")
                    a_val = a
                    data_count = 0
                    each_model_ = each_model
                    print(each_model_)
            
                elif data_count > val:
                    data_count = val
                    a_val = a
                    each_model_ = each_model
                    # a_val = a_val
            
                else:
                    pass

                print("model: ", each_model)
                print("accepted images: ", val)
                print("accuracy: ",accuracy)
                print("*********************************************************************************")
                print("*********************************************************************************")
                f= open("final.txt","a")
                f.write("***********************************************************\r\n")
                f.write("Model name: {}\r\n".format(each_model))
                f.write("Accepted images: {}\r\n".format(val))
                f.write("Model accuracy is: {}\r\n".format(accuracy))
                f.write("***********************************************************\r\n")

            else:
                print("best model for fake data is: ", each_model_)
                # print("accepted images of the best model :", val)
            ran_val = random.random()
            str_ran_value = str(ran_val)
            
            fi = open(str_ran_value, "x")
            # print(a)
            for i in a_val:
                s = str(i)
                # fi.write("\n")
                fi.write(s)
                fi.write(os.linesep)
            fi.close()
            # data moving script
            src = image_path+'/'+'fake'
            os.mkdir(pathf)
            
            fil = open(str_ran_value)
            lines = fil.readlines()
            # src=image_path
            for file_name in lines:
                count_of__FP += 1
                try:
                    source = src + '/' + file_name
                    val = shutil.move(source[:-1],pathf)
                except:
                    continue
            
            fil.close()
            rem_data = (count_of_total_images - count_of__FP)
            print("text file created is:", str_ran_value)
            print("total images processed are:", count_of_total_images)
            print("total TN's are:", rem_data)
            print("total FP's are/total images moved to destination are:", count_of__FP)
            
            # finding accuracies
            # print("choose accuracies acc to your data")
            fake_acc = (rem_data / (rem_data + count_of__FP)) * 100
            # print("FAKE ACCURACY is :", fake_acc)
            print("-------------------------------------------------------------------------------------------------")
            print("*************************************************************************************************")
            print("*************************************************************************************************")
            print("-------------------------------------------------------------------------------------------------")
            f.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\r\n")
            f.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\r\n")
            f.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\r\n")
            f.write(" Best model for fake data is : {}\r\n".format(each_model_))
            f.write(" Total images processed are : {}\r\n".format(count_of_total_images))
            f.write(" Total TN's are : {}\r\n".format(rem_data))
            f.write(" Total FP's are/total images moved to destination are : {}\r\n".format(count_of__FP))
            f.write(" Model fake accuracy is : {}%\r\n".format(fake_acc))
            f.write("\r\n")
            # f.close() 

        
#################FOR REAL###################
        elif folder=='real':
            folder_real = os.path.join(image_path, folder)
            images = os.listdir(folder_real)
            # print(images)
            data_count = len(images)
            imgs = []
            val = 0
            a_val = ''
            each_model_ = ''
            count_of__FP = 0
            count_of_total_images = 0

            for each_model in models:
                model = os.path.join(models_, each_model)
                model = tf.keras.models.load_model(model)
                a = []
                count_of_total_images = 0

                for each_image in images:
                    count_of_total_images += 1
                    # print(each_image)
                    try:
                        # print(each_image)
                        img_path = os.path.join(folder_real, each_image)
                        # print(img_path)
                        new_image = preprocessing_img(img_path)
                        # print(new_image)
                        pred = model.predict(new_image)
                        print(each_image, pred)
                        if pred[0][0] >= 0.5:
                            a.append(each_image)
                        else:
                            continue
                    except:
                        # print(each_image)
                        continue
                val = len(a)
                tps=count_of_total_images-val
                accuracy=(tps/(val+tps))*100
                f= open("final.txt","a")
                f.write("***********************************************************\r\n")
                f.write("Model name: {}\r\n".format(each_model))
                f.write("Rejected images: {}\r\n".format(val))
                f.write("Model accuracy is: {}\r\n".format(accuracy))
                f.write("***********************************************************\r\n")
            
                if val == 0:
                    print("real accuracy is 100%")
                    a_val = a
                    data_count = 0
                    each_model_ = each_model
                    print(each_model_)
            
                elif data_count > val:
                    data_count = val
                    a_val = a
                    each_model_ = each_model
            
                else:
                    pass
                print("model: ", each_model)
                print("rejected images: ", val)
                print("accuracy: ",accuracy)
                print("*********************************************************************************")
                print("*********************************************************************************")

            else:
                print("best model for real data is: ", each_model_)
                # print("rejected images of the best model :", val)
            ran_val = random.random()
            str_ran_value = str(ran_val)
            
            fi = open(str_ran_value, "x")
            # print(a)
            for i in a_val:
                s = str(i)
                # fi.write("\n")
                fi.write(s)
                fi.write(os.linesep)
            fi.close()
            # data moving script
            src = image_path+'/'+'real'
            os.mkdir(pathr)
            
            fil = open(str_ran_value)
            lines = fil.readlines()
            # src=image_path
            for file_name in lines:
                count_of__FP += 1
                try:
                    source = src + '/' + file_name
                    val = shutil.move(source[:-1], pathr)
                except:
                    continue
            
            fil.close()
            rem_data = (count_of_total_images - count_of__FP)
            print("text file created is:", str_ran_value)
            print("total images processed are:", count_of_total_images)
            print("total FN's are:", count_of__FP)
            print("total TP's are:", rem_data)
            
            # finding accuracies
            real_acc = (rem_data / (rem_data + count_of__FP)) * 100
            # print("REAL ACCURACY is :", real_acc)
            print("-------------------------------------------------------------------------------------------------")
            print("*************************************************************************************************")
            print("*************************************************************************************************")
            print("-------------------------------------------------------------------------------------------------")

            f= open("final.txt","a")
            f.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\r\n")
            f.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\r\n")
            f.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\r\n")
            f.write(" Best model for real data is : {}\r\n".format(each_model_))
            f.write(" Total images processed are : {}\r\n".format(count_of_total_images))
            f.write(" Total TP's are/total images moved to destination are : {}\r\n".format(rem_data))
            f.write(" Total FN's are : {}\r\n".format(count_of__FP))
            f.write(" Model real accuracy is : {}%\r\n".format(real_acc))
            f.write("\r\n")
            # f.close()            
        else:
            pass
f.close() 











