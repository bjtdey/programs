import os
import shutil

path1="/home/bijit/bijit/azcopy_linux_amd64_10.13.0/redLineCutNovDec/redLineCutDec01to16_/00/images/fake/deleted"

path="/home/bijit/bijit/azcopy_linux_amd64_10.13.0/redLineCutNovDec/redLineCutDec01to16_/00/images/fake/fake"
li=os.listdir(path)
# print(len(li))
count=0
for i in li:
    if "copy" in i:
        shutil.move(os.path.join(path,i),path1)
print(count)