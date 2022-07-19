import pandas as pd
import glob, os

path = r'/home/bijit/bijit/SukshiCli/recent data_may/non/' # use your path
all_files = glob.glob(os.path.join(path, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent

df_from_each_file = (pd.read_csv(f) for f in all_files)
concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)
print(concatenated_df)