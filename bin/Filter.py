#['Group','AM','Client','Solution Portfolio']
import os
import pandas as pd
def filter(df):
    base_path = os.path.abspath(os.path.dirname(__file__))
    
    file_path = os.path.join(base_path,"../Config/ClientWhiteList.txt")
    with open(file_path, "r", newline="\n") as cols:
        filter = cols.read().splitlines()     
    cols.close()
    cInd = df[df.isin(list(set(df['Client'].values.tolist()) - set(filter))).any(axis=1)].index.tolist()
    cInd = [ 1+ i for i in cInd]

    file_path = os.path.join(base_path,"../Config/AMWhiteList.txt")
    with open(file_path, "r", newline="\n") as cols:
        filter = cols.read().splitlines()     
    cols.close()
    AMInd = df[df.isin( list(set(df['AM'].values.tolist()) - set(filter)) ).any(axis=1)].index.tolist()
    AMInd = [ 1+ i for i in AMInd]    

    file_path = os.path.join(base_path,"../Config/GroupWhiteList.txt")
    with open(file_path, "r", newline="\n") as cols:
        filter = cols.read().splitlines()     
    cols.close()
    gInd = df[df.isin( list(set(df['Group'].values.tolist()) - set(filter)) ).any(axis=1)].index.tolist()
    gInd = [ 1+ i for i in gInd]    

    file_path = os.path.join(base_path,"../Config/GroupWhiteList.txt")
    with open(file_path, "r", newline="\n") as cols:
        filter = cols.read().splitlines()     
    cols.close()
    sInd = df[df.isin( list(set(df['Group'].values.tolist()) - set(filter)) ).any(axis=1)].index.tolist()
    sInd = [ 1+ i for i in sInd]


    if (not gInd and not sInd and not AMInd and not cInd):
        return True
    else:
        f = open("WhiteListLog.txt", "w")
        f.write("Rows which have values outside the whitelisted values under Client: " + ' '.join(str(x) for x in cInd)+ "\n\n")
        f.write("Rows which have values outside the whitelisted values under AM: " + ' '.join(str(x) for x in AMInd)+ "\n\n")
        f.write("Rows which have values outside the whitelisted values under Groups: " + ' '.join(str(x) for x in gInd)+ "\n\n")
        f.write("Rows which have values outside the whitelisted values under Solution Portfolio: " + ' '.join(str(x) for x in sInd)+ "\n\n")
        f.close()
        return False