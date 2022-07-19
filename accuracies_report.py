import os

path=os.getcwd()
list=os.listdir(path)
count="../real/"
count=len(os.listdir(count))
print(count)
for i in list:
    if ".h5" in i:
        if ".csv" not in i:
            if ".py" not in i:
                tp=len(os.listdir(os.path.join(path,i)))
                fn=count-tp
                file=open("acc_report", "a+")
                file.write(i+"\n"+str(tp)+"/"+str(count)+"  or   "+str(fn)+"f"+"/"+str(count)+"\n")
                file.write(10*"................."+"\n")
file.close()