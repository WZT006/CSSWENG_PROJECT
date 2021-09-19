import pandas as pd
import pathlib
from graphs import Graph
import readFile as rf
import Filter
import sys
import os
##TODO: MOVE whitelist to different file
#cols_to_use = ['Month','Group','AM','Client','Type','Solution Portfolio','Product',
#                    'Project','TOTAL Amount in Php', 'GP', "% GP", 'Date Received',
#                    'PO#','SO# 1st Round','HANA SO#', 'PS#', 'IO#', 'Ticket#', 'SOR#']
def Driver(file : str, month : str):


    f = open(file)
    f = os.path.realpath(f.name)
    
    df, space = rf.readFile(f)
    dir = "Output/"
    pathlib.Path(dir).mkdir(parents=True, exist_ok=True)
    if (getNullIndices(df,space)):
        if (Filter.filter(df,space)):
            dir = "Output/"+ month
            pathlib.Path(dir).mkdir(parents=True, exist_ok=True)
            graph = Graph(dir,df,month)
            graph.create_graphs()
            print("Finished")
        else:
            print('Invalid Values found. Please Check WhiteListLog.txt for more Details.')
    else:
        print("Null values found")


## Checks for any null indices returns which row if there are null values
def getNullIndices(df : pd.DataFrame,space) -> bool:
    space += 1
    print("Checking Null Values...")
    nulls = df[df.isnull().any(axis=1)].index.tolist()
    nulls = [ space + i for i in nulls]

    if(nulls == []):
        return True
    else:
        f = open("Output/MissingValues.txt", "w")
        f.write("Rows which have missing values: " + ' '.join(str(x) for x in nulls)+ "\n\n")
        return False
