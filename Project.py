import pandas as pd
import numpy as np
import scipy as sp
from collections import Counter

def main():
    read  = "Test"
    file = read + ".xlsx"
    dataset = pd.read_excel(open(file))
    
    #reads companywhitelist
    with open("CompanyWhiteList.txt", "r", newline="\n") as cWhite:
        comWhite = cWhite.read().splitlines()     
    cWhite.close()



    test = ["Globe","Smart","DATA"]
    #checks if there is companies outside company whitelist
    companyDirt= list((Counter(test)-Counter(comWhite)).elements())
    print( companyDirt)



    pass

if __name__ == '__main__':
    main()