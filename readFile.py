import pandas as pd
from collections import Counter

##Reads the specified file and sheet ,filtering the "unneeded data"
#Params : 
# fName : String specifying the file's name
def readFile(fName : str) -> pd.DataFrame:

    #dataset = pd.read_excel( fName ,skiprows=lambda x: x in [0, 1], usecols=lambda x: 'Unnamed' not in x,sheet_name = sName)
    
    data = removeBorders(fName)
    
    #reads companywhitelist
    with open("Config\CompanyWhiteList.txt", "r", newline="\n") as cWhite:
        comWhite = cWhite.read().splitlines()     
    cWhite.close()
    with open("Config\Col_to_Use.txt", "r", newline="\n") as cols:
        cols_to_use = cols.read().splitlines()     
    cols.close()
    

    #Filters read excel file to a dataframe to only include wanted columns
    data = data[cols_to_use]
    #data.rename(columns={'TOTAL Amount in Php' : 'Revenue'}, inplace = True)
    data['TOTAL Amount in Php'] = data['TOTAL Amount in Php'] / 1_000_000
    data['GP'] = data['GP'] / 1_000_000

    return data


##Removes variable amount of filler before header column and row
def removeBorders(fName : str):
    df = pd.read_excel(fName)
    ##check which row has "Month"
    idx = df.loc[(df == 'Month').any(axis=1)].index.values
    
    if (not idx): idx = 0 
    else: idx = idx[0] + 1

    #filter out rows above idx
    df = pd.read_excel(fName,header= idx)
    
    return df