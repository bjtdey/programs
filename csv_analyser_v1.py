import pandas as pd 
import os, numpy as np

path="/content/"
x=[]
for i in os.listdir(path):
  if ".csv" in i:
    x.append(path + i)

for i in x:
  d1 = pd.read_csv(i)
  d2=d1.loc[d1['GT']=="fake"]
  print(i)
  print("fake_acc=",(d2.loc[d2["pred_score"]>=0.5].shape[0])/len(d2)*100,"%")
  d2=d1.loc[d1['GT']=="real"]
  print("real_acc=",(d2.loc[d2["pred_score"]<0.5].shape[0])/len(d2)*100,"%")
  print(10*".............")