import pandas as pd
import numpy as np
import scipy as sp
from collections import Counter
import pathlib
from graphs import Graph
import readFile as rf

#cols_to_use = ['Month','Group','AM','Client','Type','Solution Portfolio','Product',
#                    'Project','TOTAL Amount in Php', 'GP', "% GP", 'Date Received',
#                    'PO#','SO# 1st Round','HANA SO#', 'PS#', 'IO#', 'Ticket#', 'SOR#']
def main():
    #To be changed to UI later on
    tmp =  input("File name: ")
    file = str(tmp) + ".xlsx"
    #sheet = input("Sheet Name: ")
    month = input("Month (Year for year report),format 'Month' :")
    #file = "Book2.xlsx"
    #sheet = "2020"
    #month = "Year"
    
    df = rf.readFile(file)

    #print(df[['TOTAL Amount in Php', 'GP']])

  
    if (getNullIndices(df)):
        pathlib.Path(tmp).mkdir(parents=True, exist_ok=True)
        graph = Graph(df,tmp,month)
        graph.create_graphs()

    print("Finished")


## Checks for any null indices returns which row if there are null values
def getNullIndices(df : pd.DataFrame) -> bool:
    for x in df:
        nulls = df[df[x].isnull()].index.tolist()
        nulls = [ 1+ i for i in nulls]
    if(nulls == []):
        print("No Empty Values Detected")
        return True
    else:
        print('There are missing values on entries:', nulls)
        return False
        

if __name__ == '__main__':
    main()