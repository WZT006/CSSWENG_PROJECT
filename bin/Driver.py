import pandas as pd
import pathlib
from graphs import Graph
import readFile as rf
import os

#cols_to_use = ['Month','Group','AM','Client','Type','Solution Portfolio','Product',
#                    'Project','TOTAL Amount in Php', 'GP', "% GP", 'Date Received',
#                    'PO#','SO# 1st Round','HANA SO#', 'PS#', 'IO#', 'Ticket#', 'SOR#']
def main():
    #To be changed to UI later on
    tmp =  input("File name: ")
    file = str(tmp) + ".xlsx"
    month = input("Month (Year for year report),format 'Month' : ")

    f = open(file)
    f = os.path.realpath(f.name)
    
    df = rf.readFile(f)


    #print(df[['TOTAL Amount in Php', 'GP']])

  
    if (getNullIndices(df)):
        dir = "Output/"+ month
        pathlib.Path(dir).mkdir(parents=True, exist_ok=True)
        graph = Graph(dir,df,month)
        graph.create_graphs()

    print("Finished")


## Checks for any null indices returns which row if there are null values
def getNullIndices(df : pd.DataFrame) -> bool:
    for x in df:
        nulls = df.loc[df[x].isnull()].index.tolist()
        nulls = [ 1+ i for i in nulls]
    if(nulls == []):
        return True
    else:
        print('There are missing values on entries:', nulls)
        return False
        

if __name__ == '__main__':
    main()