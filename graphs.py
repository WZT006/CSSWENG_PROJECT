import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
        self.exportTable(df,path)

        colors = ['#892F38','#F6957C']
        cols =list(df.columns)
        self.exportGraph(df,path,cols,colors)

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
        
        colors = ['#1F77B4','#ACD7E5']
        cols =list(df.columns)
        self.exportGraph(df,path,cols,colors)

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
        
        colors = ['#CBEAA6','#8190C5']
        cols =list(df.columns)
        self.exportGraph(df,path,cols,colors)        

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
        
        colors = ['#4F772D','#ECF39E']
        cols =list(df.columns)
        self.exportGraph(df,path,cols,colors)




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
        
        colors = ['#656D4A']
        cols =list(df.columns)
        self.exportGraph(df,path,cols,colors)
     
    def TOTAL_Salesperson(self):
        if (self.month == "Year"):
            df = self.data[['AM','TOTAL Amount in Php']].copy()
        else:
            df = self.data.loc[self.data['Month'] == self.month][['TOTAL Amount in Php','AM']].copy()
    
        df = df.groupby('AM',as_index=False).sum()

        #sets filename to save to
        filename = "TOTAL amount in PHP by AM"

        #exports to a table
        path = os.path.join(self.directory,filename)
        self.exportTable(df,path + "_Table")

        colors = ['#012A4A']
        cols =list(df.columns)
        self.exportGraph(df,path,cols,colors)

    def TOTAL_Client(self):
        if (self.month == "Year"):
            df = self.data[['Client','TOTAL Amount in Php',]].copy()
        else:
            df = self.data.loc[self.data['Month'] == self.month][['TOTAL Amount in Php','Client']].copy()
    
        df = df.groupby('Client',as_index=False).sum()

        #sets filename to save to
        filename = "TOTAL amount in PHP by Client"

        #exports to a table
        path = os.path.join(self.directory,filename)
        self.exportTable(df,path + "_Table")

        colors = ['#892F38']
        cols =list(df.columns)
        self.exportGraph(df,path,cols,colors)

    def TOTAL_Solutions(self):
        if (self.month == "Year"):
            df = self.data[['Solution Portfolio','TOTAL Amount in Php']].copy()
        else:
            df = self.data.loc[self.data['Month'] == self.month][['TOTAL Amount in Php','Solution Portfolio']].copy()
    
        df = df.groupby('Solution Portfolio',as_index=False).sum()

        #sets filename to save to
        filename = "TOTAL amount in PHP by Solution Portfolio"

        #exports to a table
        path = os.path.join(self.directory,filename)
        self.exportTable(df,path + "_Table")

        colors = ['#8190C5']
        cols =list(df.columns)
        self.exportGraph(df,path,cols,colors)



    def GP_Group(self):
        if (self.month == "Year"):
            df = self.data[['Group', 'GP']].copy()
        else:
            df = self.data.loc[self.data['Month'] == self.month][['GP','Group']].copy()
    
        df = df.groupby('Group',as_index=False).sum()

        #sets filename to save to
        filename = "GP by Group"

        #exports to a table
        path = os.path.join(self.directory,filename)
        self.exportTable(df,path + "_Table")

        colors = ['#656D4A']
        cols =list(df.columns)
        self.exportGraph(df,path,cols,colors)

    def GP_Salesperson(self):
        if (self.month == "Year"):
            df = self.data[['AM', 'GP']].copy()
        else:
            df = self.data.loc[self.data['Month'] == self.month][['GP','AM']].copy()
    
        df = df.groupby('AM',as_index=False).sum()

        #sets filename to save to
        filename = "GP by AM"

        #exports to a table
        path = os.path.join(self.directory,filename)
        self.exportTable(df,path + "_Table")

        colors = ['#012A4A']
        cols =list(df.columns)
        self.exportGraph(df,path,cols,colors)

    def GP_Client(self):
        if (self.month == "Year"):
            df = self.data[['Client','GP']].copy()
        else:
            df = self.data.loc[self.data['Month'] == self.month][['GP','Client']].copy()
    
        df = df.groupby('Client',as_index=False).sum()

        #sets filename to save to
        filename = "GP by Client"

        #exports to a table
        path = os.path.join(self.directory,filename)
        self.exportTable(df,path + "_Table")

        colors = ['#892F38']
        cols =list(df.columns)
        self.exportGraph(df,path,cols,colors)

    def GP_Solutions(self):
        if (self.month == "Year"):
            df = self.data[['Solution Portfolio','GP']].copy()
        else:
            df = self.data.loc[self.data['Month'] == self.month][['GP','Solution Portfolio']].copy()
    
        df = df.groupby('Solution Portfolio',as_index=False).sum()

        #sets filename to save to
        filename = "GP by Solution Portfolio"

        #exports to a table
        path = os.path.join(self.directory,filename)
        self.exportTable(df,path + "_Table")

        colors = ['#8190C5']
        cols =list(df.columns)
        self.exportGraph(df,path,cols,colors)



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

    def exportGraph(self, df : pd.DataFrame, path : str, cols,colors):

        name = path + "_GRAPH"
        if os.path.exists(name):
            os.remove(name)

        if 'Client' in df.columns:
            df = df.sort_values(by='Client', ascending= False)
            head = df.head(10)
            if (len(df) > 10):
                tail = df.tail(len(df) - 10).sum()
                tail['Client'] = "Others"
                df = head.append(tail,ignore_index= True)
                pass
        #TODO CHANGE number parameters to make it dynamic (figsize, ind calculation, and width)
        plt.figure(figsize=(50,20),facecolor='w') 
        ind = np.arange(df[cols[0]].count())
        width = 0.25
        
        if( len(cols) == 3):
            bar1 = plt.bar(ind, df[cols[1]], width,color = colors[0])
            bar2 = plt.bar(ind+width, df[cols[2]], width, color = colors[1])
            plt.legend( (bar1, bar2), (cols[1],cols[2]),prop={'size': 30})
            plt.xticks( ind+(width/2),df[cols[0]].values.tolist(),rotation=45)
            plt.tick_params(axis = 'both', which = 'major', labelsize = 20)
            
        else:
            bar1 = plt.bar(ind, df[cols[1]], width,color = colors[0])
            plt.xticks( ind,df[cols[0]].values.tolist(),rotation = 45)
            plt.tick_params(axis = 'both', which = 'major', labelsize = 24)
            
            
        
        plt.xlabel(cols[0])
        plt.ylabel("Value (Millions)")
           
        plt.savefig(name, bbox_inches='tight',dpi= 100)
        plt.close()
