import os
from zipfile import ZipFile
import csv_analyser_v2

cwd=os.getcwd()
script_path="/home/bijit/Downloads/Scripts/csv_analyser_v2.py"
# path=os.listdir(os.getcwd())
path=os.listdir(os.getcwd())
for i in path:
    if ".zip" in str(i):
        # opening the zip file in READ mode
        with ZipFile(i, 'r') as zip:
            # printing all the contents of the zip file
            zip.printdir()
        
            # extracting all the files
            print('Extracting all the files now...')
            zip.extractall()
            k=str(cwd)+"/"str(i)+"/"
            print(k)
        print(i) 