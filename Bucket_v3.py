import cv2, os, shutil

path=r"/home/bijit/bijit/SukshiCli/Feb month FPs n FNs/Fns/de_poi_micro/image/real/"
li=os.listdir(path)
covered=[]
list=['major_cut','partial_micro_cut', 'proper', 'Paper', 'double_card','bad_quality', 'photo_cut','Tagline_cut', 'wrong_tag', 'Poa']
#           0           1               2               3           4         5               6           7               8         9
if not os.path.exists(path+"coverd"):
    os.mkdir(path+"coverd")
covered=os.listdir(path + "coverd/")

def file_mnm(d=int):
    if not os.path.exists(path+list[d]):
#         new_path = os.path.join(path,list[d])
        os.mkdir(path+list[d])
    cv2.imwrite(path+list[d]+"/"+ i, image)
    cv2.destroyAllWindows()
    # covered.append(i)
    shutil.move(path+i, path+"coverd/"+i)
    print(len(covered))

for i in li:
    if ".jpg" in str(i):    
        image = cv2.imread(path + i)
        cv2.imshow(i, image)
        k=cv2.waitKey(0)
        k
        if i not in covered:
            if k == ord('m'):  # wait for 's' key to save and exit
                file_mnm(0)
            elif k == ord('p'):  # wait for 's' key to save and exit
                file_mnm(1)
            elif k == ord('a'):  # wait for 's' key to save and exit
                file_mnm(2)
            elif k == ord('s'):  # wait for 's' key to save and exit
                file_mnm(3)
            elif k == ord('d'):  # wait for 's' key to save and exit
                file_mnm(4)
            elif k == ord('b'):  # wait for 's' key to save and exit
                file_mnm(5)
            elif k == ord('c'):  # wait for 's' key to save and exit
                file_mnm(6)
            elif k == ord('t'):  # wait for 's' key to save and exit
                file_mnm(7)
            elif k == ord('w'):  # wait for 's' key to save and exit
                file_mnm(8)
            elif k == ord('o'):  # wait for 's' key to save and exit
                file_mnm(9)
        
print(covered)
