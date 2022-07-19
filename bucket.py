import shutil, os
from PIL import Image 

img_path = r"/home/bijit/bijit/bijit/"
den1 = r"/home/bijit/bijit/bijit"

list=['Emblem_cut', 'QR_cut', 'Address_cut','Issue&Downloadcuts', 'Slight_QR_cut', 'Aadhar_logo_cut', 'Proper_card', 'others', 'redline']
#list=['Emblem_cut', 'QR_cut', 'Address_cut','Issue&Downloadcuts', 'Slight_QR_cut', 'Aadhar_logo_cut', 'Proper_card', 'others', 'redline'] 
#           0            1           2                 3                   4                 5                6           7          8
count=0

for image in os.listdir(img_path):
# creating an og_image object -->
    img = img_path + image
    og_image = Image.open(img)
    og_image.show()
    key=int(input("Enter a key : "))

    dst_dir = den1 + "//"+ list[key]+"//"
    if not os.path.exists(dst_dir):
        path = os.path.join(den1,list[key])
        os.mkdir(path)
        
    src = img
    dst = dst_dir + image
    shutil.move(src,dst)
    count=count+1
    print(count)