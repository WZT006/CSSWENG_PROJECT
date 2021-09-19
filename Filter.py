#['Group','AM','Client','Solution Portfolio']
import os
import pandas as pd
import numpy as np
def filter(df,space):
    space = space + 2
    base_path = os.path.abspath(os.path.dirname(__file__))
    
    file_path = os.path.join(base_path,"Config/ClientWhiteList.txt")
    with open(file_path, "r", newline="\n") as cols:
        filter = cols.read().splitlines()     
    cols.close()
    cInd = []
    out = list(set(df['Client'].values.tolist()) - set(filter))
    for x in out:
        cInd += df.index[ (df['Client'] == x)].tolist()
    cInd = [ space + i for i in cInd] 

    file_path = os.path.join(base_path,"Config/AMWhiteList.txt")
    with open(file_path, "r", newline="\n") as cols:
        filter = cols.read().splitlines()     
    cols.close()
    AMInd = []
    out = list(set(df['AM'].values.tolist()) - set(filter))
    for x in out:
        AMInd += df.index[ (df['AM'] == x)].tolist()
    AMInd = [ space + i for i in AMInd]    


    file_path = os.path.join(base_path,"Config/GroupWhiteList.txt")
    with open(file_path, "r", newline="\n") as cols:
        filter = cols.read().splitlines()     
    cols.close()
    gInd = []
    out = list(set(df['Group'].values.tolist()) - set(filter))
    for x in out:
        gInd += df.index[ (df['Group'] == x)].tolist()
    gInd = [ space + i for i in gInd]   

    file_path = os.path.join(base_path,"Config/SolPortWhiteList.txt")
    with open(file_path, "r", newline="\n") as cols:
        filter = cols.read().splitlines()     
    cols.close()

    sInd = []
    out = list(set(df['Solution Portfolio'].values.tolist()) - set(filter))
    for x in out:
        sInd += df.index[ (df['Solution Portfolio'] == x)].tolist()
    sInd = [ space + i for i in sInd] 


    if (not gInd and not sInd and not AMInd and not cInd):
        return True
    else:
        f = open("Output/WhiteListLog.txt", "w")
        f.write("Rows which have values outside the whitelisted values under Client: " + ' '.join(str(x) for x in cInd)+ "\n\n")
        f.write("Rows which have values outside the whitelisted values under AM: " + ' '.join(str(x) for x in AMInd)+ "\n\n")
        f.write("Rows which have values outside the whitelisted values under Groups: " + ' '.join(str(x) for x in gInd)+ "\n\n")
        f.write("Rows which have values outside the whitelisted values under Solution Portfolio: " + ' '.join(str(x) for x in sInd)+ "\n\n")
        f.close()
        return False