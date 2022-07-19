import pandas as pd, os
from zipfile import ZipFile

path="/home/bijit/bijit/paperspoof_Repositeries/paperspoof_retrained_models/retrained models/march_retrained models/"
# completed=[]

def csv():
    # print(os.getcwd())
    for i in os.listdir(os.getcwd()):
        if ".csv" in i: 
        # and str(i) not in completed:
            d1 = pd.read_csv(i)
            d2=d1.loc[d1['GT']=="fake"]
            file=open("csv_analysis", "a+")
            file.write(i+"\n")
            file.write("fake_acc="+str((d2.loc[d2["pred_score"]>=0.5].shape[0])/len(d2)*100)+"%"+"\n")
            d2=d1.loc[d1['GT']=="real"]
            file.write("real_acc="+str((d2.loc[d2["pred_score"]<0.5].shape[0])/len(d2)*100)+"%"+"\n")
            file.write(10*"............."+"\n")
            file.close()

def extract(p=str):
    if ".zip" in str(p):
        # opening the zip file in READ mode
        with ZipFile(p, 'r') as zip:
            # printing all the contents of the zip file
            # zip.printdir()
        
            # extracting all the files
            # print('Extracting all the files now...')
            zip.extractall()
            

def main():
    c=0
    for i in os.listdir(path):
        for j in os.listdir(os.path.join(path,i)):
            for k in os.listdir(os.path.join(path,i,j)):
                if ".zip" in str(k):
                    x=path+str(i)+"/"+str(j)
                    os.chdir(x)
                    extract(k)
                    p=k.split(".")
                    p=str(p[0])
                    os.chdir(x+"/"+p)
                    csv()
                    # print(x+k)
                    c=c+1
    return c

if __name__=="__main__":
    main()
    # f=main()
    # print("{}".format(f))