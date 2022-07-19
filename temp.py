import pandas as pd, os
from zipfile import ZipFile

path="/home/bijit/Videos/exp"

def main(path):
    for i in os.listdir(path):
            for j in os.listdir(os.path.join(path,i)):
                print(j)