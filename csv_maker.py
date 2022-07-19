import pandas as pd
from sqlalchemy import column
txt_path = '/home/dell/Documents/bo_superconvergence/Mhere_occlusion_best_trials.txt'
file = open(txt_path,'r')
lines = file.readlines()
count = 1
columns = []
for line in lines[7:]:
    columns.append(line.split(":")[0])
    if count == 10:
        break
    count+=1
print(columns)
lr = []
beta_1 = []
beta_2 = []
epsilon = []
batch_size = []
epochs = []
phase_1_pct = []
div_factor = []
shuffle = []
Score = []
for line in lines[5:]:
    key = line.split(":")[0]
    value = line.split(": ")[-1][:-1]
    # print(key,value)
    if key == 'lr':
        lr.append(value)
    elif key == 'beta_1':
        beta_1.append(value)
    elif key == 'beta_2':
        beta_2.append(value)
    elif key == 'epsilon':
        epsilon.append(value)
    elif key == 'batch_size':
        batch_size.append(value)
    elif key == 'epochs':
        epochs.append(value)
    elif key == 'phase_1_pct':
        phase_1_pct.append(value)
    elif key == 'div_factor':
        div_factor.append(value)
    elif key == 'shuffle':
        shuffle.append('True')
    elif key == 'Score':
        Score.append(value)
df = pd.DataFrame(list(zip(lr, beta_1, beta_2, epsilon, batch_size, epochs, phase_1_pct, div_factor, shuffle, Score)),columns= columns)
print(df)
df.to_csv('mhere_occlusion_20000.csv',index=False)
