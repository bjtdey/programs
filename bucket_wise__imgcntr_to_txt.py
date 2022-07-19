import os

from matplotlib.pyplot import close

path=r"/home/bijit/bijit/paperspoof_Repositeries/analysis/jan16/fake/image/paperspoof_v_0_5/m"
os.chdir(path)
list=os.listdir(path)
for i in list:
    l=os.listdir(path=path+"/"+i)
    file=open("bucketed_data_count", "a+")
    file.write(i+"="+str(len(l))+"\n")
file.close()
