from scipy import ndimage, misc
import numpy as np
import os
import cv2
def main():
    outPath = "/home/bijit/bijit/paperspoof_Repositeries/datasets/Paperspoof_april_5/real_rotate/"
    path = "/home/bijit/bijit/paperspoof_Repositeries/datasets/Paperspoof_april_5/real_v7/"
   # iterate through the names of contents of the folder
    for image_path in os.listdir(path):
        # create the full input path and read the file
        input_path = os.path.join(path, image_path)
        #image_to_rotate = ndimage.imread(input_path)
        image_to_rotate = cv2.imread(input_path)
        
        #List = [0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6,2.8,3,-0.2,-0.4,-0.6,-0.8,-1,-1.2,-1.4,-1.6,-1.8,-2,-2.2,-2.4,-2.6,-2.8,-3]#30
        #List = [0,0.3,-0.3,0.6,-0.6,0.9,-0.9,1.2,-1.2,1.5,-1.5,1.8,-1.8,2.1,-2.1,2.4,-2.4,2.7,-2.7,3,-3,0.5, 1,2.05,-1,-0.5,-2.05]#27
        #List = [0,0.3,-0.3,0.6,-0.6,0.9,-0.9,1.2,-1.2,1.5,-1.5,1.8,-1.8,2.1,-2.1,2.4,-2.4,2.7,-2.7,3,-3]#21
        #List = [0.5, 1, 1.5, 2]
        #List = [0,0.3,-0.3,0.6,-0.6,0.9,-0.9,1.2,-1.2,1.5,-1.5,1.8,-1.8,2.1,-2.1]#15
        #List = [0.1,0.09,359.5]
        List = [0.1]
        #List = [359.5,359,]
        #List = [0.5, 1, 1.5, 2, 2.5, 358, 358.5, 357, 357.5,359]
        #ListList = [0.5, 1, 1.5, 358, 357, 357.5]
        #List = [0.2,0.4,0.6]
        #List = [0.5]
        for i in List:
            rotate = ndimage.rotate(image_to_rotate,i)
            #fullpath = os.path.join(outPath, 'rotate_'+str(i)+'_'+image_path)
            cv2.imwrite( str(outPath) + "rotate" + str(i) +"_"+image_path,rotate)
            #misc.imsave(fullpath,rotate)
if __name__ == '__main__':
    main()      
