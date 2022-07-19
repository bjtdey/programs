import pandas as pd, os

path=str
for i in os.listdir(os.getcwd()):
  if ".csv" in i:
    # print(i)
    d1 = pd.read_csv(i)
    d2=d1.loc[d1['GT']=="fake"]
    file=open("csv_analysis", "a+")
    file.write(i+"\n")
    # print(i)
    file.write("fake_acc="+str((d2.loc[d2["pred_score"]>=0.5].shape[0])/len(d2)*100)+"%"+"\n")
    d2=d1.loc[d1['GT']=="real"]
    file.write("real_acc="+str((d2.loc[d2["pred_score"]<0.5].shape[0])/len(d2)*100)+"%"+"\n")
    file.write(10*"............."+"\n")
file.close()
