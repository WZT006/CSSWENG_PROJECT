#['Group','AM','Client','Solution Portfolio']
import os
import pandas as pd
def filter(df):
    base_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(base_path,"../Config/ClientWhiteList.txt")
    
    with open(file_path, "r", newline="\n") as cols:
        filter = cols.read().splitlines()     
    cols.close()
    
    errors = list(set(df['Client'].values.tolist()) - set(filter))
    indices = df[df.isin(errors).any(axis=1)].index.tolist()

    pass