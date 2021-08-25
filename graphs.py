import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import kaleido
import os



class Graph(object):
    
    def __init__(self,data,directory):
        self.directory = directory
        self.data = data
    

    ##creates and exports all graphs
    #calls specific graph functions
    def create_graphs(self):
        pass

    def revenueXgroup(self):
        df = self.data[['Group','Revenue']].copy()
        filename = "revenueXgroup.png"
        path = os.path.join(self.directory,filename)
        
        self.exportTable(df,path)


    def exportTable(self,df,name):
        fig =  ff.create_table(df)
        fig.update_layout(
            autosize=False,
            width=500,
            height=200,
        )
        if os.path.exists(name):
            os.remove(name)
        fig.write_image(name, scale=2,)
        fig.show()
