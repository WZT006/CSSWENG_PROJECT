import pandas as pd
import numpy as np
import scipy as sp
from collections import Counter

def main():
    

    ## to be changed to UI later on
    tmp =  input("File name: ")
    file = str(tmp) + ".xlsx"
    sheet = input("Sheet Name: ")
    
    #read_file = pd.read_excel(file, skiprows=lambda x: x in [0, 1],usecols=lambda x: 'Unnamed' not in x)
    #read_file.to_csv(r'Converted.csv', index = None, header=True)

    dataset = pd.read_excel(file, skiprows=lambda x: x in [0, 1],usecols=lambda x: 'Unnamed' not in x,sheet_name = sheet)
    
    #reads companywhitelist
    with open("CompanyWhiteList.txt", "r", newline="\n") as cWhite:
        comWhite = cWhite.read().splitlines()     
    cWhite.close()

    data = dataset[['Month','Group','AM','Client','Type','Solution Portfolio','Product',
                    'Project','TOTAL Amount in Php', 'GP', "% GP", 'Date Received',
                    'PO#','SO# 1st Round','HANA SO#', 'PS#', 'IO#', 'Ticket#', 'SOR#']]



    test = ["Globe","Smart","DATA"]
    #checks if there is companies outside company whitelist
    companyDirt= list((Counter(test)-Counter(comWhite)).elements())
    #print( companyDirt)

    data.info()



    pass

if __name__ == '__main__':
    main()