import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import style
import os




class Graph(object):
    
    def __init__(self,directory,data,month):
        self.directory = directory
        self.data = data
        self.month = month
        
        
        
    

    

    ##creates and exports all graphs
    #calls specific graph functions
    def create_graphs(self):

        self.TOTAL_GP_Group()
        self.TOTAL_GP_Salesperson()
        self.TOTAL_GP_Client()
        self.TOTAL_GP_Solutions()

        self.TOTAL_group()
        self.TOTAL_Salesperson()
        self.TOTAL_Client()
        self.TOTAL_Solutions()

        self.GP_Group()
        self.GP_Salesperson()
        self.GP_Client()
        self.GP_Solutions()



    def TOTAL_GP_Group(self):
        if (self.month == "Year"):
            df = self.data[['Group','TOTAL Amount in Php','GP']].copy()
        else:
            df = self.data.loc[self.data['Month'] == self.month][['Group','TOTAL Amount in Php','GP']].copy()
        df = df.groupby('Group',as_index=False).sum()
        
        filename = "TOTAL Amount in Php & GP By Group"
        #exports to a table
        
        path = os.path.join(self.directory,filename)
        self.exportTable(df,path + "_Table")

        name = path + "_GRAPH"
        if os.path.exists(name):
            os.remove(name)

        ##TODO: add last bar
        #creates graph
        sns.set_theme(style="darkgrid")
        plt.figure(figsize=(20,20)) 

        # ax = sns.barplot(x="Group",y="TOTAL Amount in Php",data = df,errcolor="Gray",errwidth = 0)
        # ax.bar_label(ax.containers[0])
        # ax.set_xlabel(None)
        # ax.set_ylabel(None)
    
        ind = np.arange(df['Group'].count())
        width = 0.25
        bar1 = plt.bar(ind, df['TOTAL Amount in Php'], width,color = 'teal')
        bar2 = plt.bar(ind+width, df['GP'], width, color = 'red')
        plt.xticks( ind+width,df['Group'].values.tolist() )
        plt.legend( (bar1, bar2), ('REVENUE','GP') )
        plt.xlabel("Groups")
        plt.ylabel("Value (Millions)")
           
        plt.savefig(name, bbox_inches='tight')


    def TOTAL_GP_Salesperson(self):
        if (self.month == "Year"):
            df = self.data[['TOTAL Amount in Php','GP', 'AM']].copy()
        else:
            df = self.data.loc[self.data['Month'] == self.month][['TOTAL Amount in Php','GP', 'AM']].copy()
        df.rename(columns={'TOTAL Amount in Php': 'TOTAL amount in PHP'},inplace = True)
        df = df.groupby('AM',as_index=False).sum()

        #sets filename to save to
        filename = "TOTAL amount in PHP & GP by Salesperson"

        #exports to a table
        path = os.path.join(self.directory,filename)
        self.exportTable(df,path + "_Table")

    def TOTAL_GP_Client(self):
        if (self.month == "Year"):
            df = self.data[['TOTAL Amount in Php','GP', 'Client']].copy()
        else:
            df = self.data.loc[self.data['Month'] == self.month][['TOTAL Amount in Php','GP', 'Client']].copy()
    
        df = df.groupby('Client',as_index=False).sum()

        #sets filename to save to
        filename = "TOTAL amount in PHP & GP by Client"

        #exports to a table
        path = os.path.join(self.directory,filename)
        self.exportTable(df,path + "_Table")

    def TOTAL_GP_Solutions(self):
        if (self.month == "Year"):
            df = self.data[['TOTAL Amount in Php','GP', 'Solution Portfolio']].copy()
        else:
            df = self.data.loc[self.data['Month'] == self.month][['TOTAL Amount in Php','GP', 'Solution Portfolio']].copy()
    
        df = df.groupby('Solution Portfolio',as_index=False).sum()

        #sets filename to save to
        filename = "TOTAL amount in PHP & GP by Solution Portfolio"

        #exports to a table
        path = os.path.join(self.directory,filename)
        self.exportTable(df,path + "_Table")



    def TOTAL_group(self):
        if (self.month == "Year"):
            df = self.data[['Group','TOTAL Amount in Php']].copy()
        else:
            df = self.data.loc[self.data['Month'] == self.month][['Group','TOTAL Amount in Php']].copy()
        df = df.groupby('Group',as_index=False).sum()

        #sets filename to save to
        filename = "TOTAL Amount in Php By Group"

        #exports to a table
        path = os.path.join(self.directory,filename)
        self.exportTable(df,path + "_Table")

        #xAxis = df.count()['Group']
        #df.plot.bar()
        #plt.xlabel('Primary Type')
        #plt.ylabel('Count')
        #plt.title('Pokemon count per primary type')
        #plt.plot()
     
    def TOTAL_Salesperson(self):
        if (self.month == "Year"):
            df = self.data[['TOTAL Amount in Php','AM']].copy()
        else:
            df = self.data.loc[self.data['Month'] == self.month][['TOTAL Amount in Php','AM']].copy()
    
        df = df.groupby('AM',as_index=False).sum()

        #sets filename to save to
        filename = "TOTAL amount in PHP by AM"

        #exports to a table
        path = os.path.join(self.directory,filename)
        self.exportTable(df,path + "_Table")

    def TOTAL_Client(self):
        if (self.month == "Year"):
            df = self.data[['TOTAL Amount in Php','Client']].copy()
        else:
            df = self.data.loc[self.data['Month'] == self.month][['TOTAL Amount in Php','Client']].copy()
    
        df = df.groupby('Client',as_index=False).sum()

        #sets filename to save to
        filename = "TOTAL amount in PHP by Client"

        #exports to a table
        path = os.path.join(self.directory,filename)
        self.exportTable(df,path + "_Table")

    def TOTAL_Solutions(self):
        if (self.month == "Year"):
            df = self.data[['TOTAL Amount in Php','Solution Portfolio']].copy()
        else:
            df = self.data.loc[self.data['Month'] == self.month][['TOTAL Amount in Php','Solution Portfolio']].copy()
    
        df = df.groupby('Solution Portfolio',as_index=False).sum()

        #sets filename to save to
        filename = "TOTAL amount in PHP by Solution Portfolio"

        #exports to a table
        path = os.path.join(self.directory,filename)
        self.exportTable(df,path + "_Table")



    def GP_Group(self):
        if (self.month == "Year"):
            df = self.data[['GP','Group']].copy()
        else:
            df = self.data.loc[self.data['Month'] == self.month][['GP','Group']].copy()
    
        df = df.groupby('Group',as_index=False).sum()

        #sets filename to save to
        filename = "GP by Group"

        #exports to a table
        path = os.path.join(self.directory,filename)
        self.exportTable(df,path + "_Table")

    def GP_Salesperson(self):
        if (self.month == "Year"):
            df = self.data[['GP','AM']].copy()
        else:
            df = self.data.loc[self.data['Month'] == self.month][['GP','AM']].copy()
    
        df = df.groupby('AM',as_index=False).sum()

        #sets filename to save to
        filename = "GP by AM"

        #exports to a table
        path = os.path.join(self.directory,filename)
        self.exportTable(df,path + "_Table")

    def GP_Client(self):
        if (self.month == "Year"):
            df = self.data[['GP','Client']].copy()
        else:
            df = self.data.loc[self.data['Month'] == self.month][['GP','Client']].copy()
    
        df = df.groupby('Client',as_index=False).sum()

        #sets filename to save to
        filename = "GP by Client"

        #exports to a table
        path = os.path.join(self.directory,filename)
        self.exportTable(df,path + "_Table")

    def GP_Solutions(self):
        if (self.month == "Year"):
            df = self.data[['GP','Solution Portfolio']].copy()
        else:
            df = self.data.loc[self.data['Month'] == self.month][['GP','Solution Portfolio']].copy()
    
        df = df.groupby('Solution Portfolio',as_index=False).sum()

        #sets filename to save to
        filename = "GP by Solution Portfolio"

        #exports to a table
        path = os.path.join(self.directory,filename)
        self.exportTable(df,path + "_Table")



    def exportTable(self,df,name):
        fig, ax = plt.subplots()

        name = name+ '.png'
        xls = name+'.xlsx'
        df = df.round(decimals = 2)
        floatcol = df.select_dtypes(include=['float64']).columns
        
        df[floatcol] = df[floatcol].apply(lambda series: series.apply(lambda value: f"{value:,}"))
        table = ax.table(cellText=df.values, 
                        colLabels=df.columns, 
                        loc='center')

        
        ax.axis('off')
        table.set_fontsize(20)
        table.scale(1,4)                        
        if os.path.exists(name):
            os.remove(name)
        if os.path.exists(xls):
            os.remove(xls)        
        
        plt.savefig(name, bbox_inches='tight',pad_inches= 1)
        df.to_excel(xls)

