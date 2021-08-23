import pandas as pd
import numpy as np
import scipy as sp
from collections import Counter
import os

def main():
    ## to be changed to UI later on
    #tmp =  input("File name: ")
    #file = str(tmp) + ".xlsx"
    #sheet = input("Sheet Name: ")
    file = "Book2.xlsx"
    sheet = "2020"
    df = readFile(file,sheet)
    #os.mkdir(sheet)
    getNullIndices(df)



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
        

    
##Reads the specified file and sheet ,filtering the "unneeded data"
#Params : 
# fName : String specifying the file's name
def readFile(fName : str, sName : str) -> pd.DataFrame:

    dataset = pd.read_excel( fName ,skiprows=lambda x: x in [0, 1], usecols=lambda x: 'Unnamed' not in x,sheet_name = sName)

    #reads companywhitelist
    with open("CompanyWhiteList.txt", "r", newline="\n") as cWhite:
        comWhite = cWhite.read().splitlines()     
    cWhite.close()

    #Filters read excel file to a dataframe to only include wanted columns
    data = dataset[['Month','Group','AM','Client','Type','Solution Portfolio','Product',
                    'Project','TOTAL Amount in Php', 'GP', "% GP", 'Date Received',
                    'PO#','SO# 1st Round','HANA SO#', 'PS#', 'IO#', 'Ticket#', 'SOR#']]

    return data

if __name__ == '__main__':
    main()