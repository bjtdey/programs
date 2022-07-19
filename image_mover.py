import os
import shutil,os

path = ""
for i in os.listdir(path):
    if ".py" not in i:
        print(i)
        # os.chdir(os.path.join(path,i))
        # for j in os.listdir(os.getcwd()):
        #     if ".jpg" or ".png" in j:
        #         shutil.move(os.path.join(os.getcwd(),j),os.path.join(path,j))


