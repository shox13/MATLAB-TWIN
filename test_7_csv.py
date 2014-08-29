import csv
import pytz
import pandas as pd # great library for examining data \('3')/
#import numpy as np
import matplotlib.pyplot as plt
from pylab import plotfile, show, gca
import matplotlib.cbook as cbook

#default condtions to for csv. commands
dia = csv.excel()
dia.quoting = csv.QUOTE_NONE


#user specifies location
location=raw_input("What data do you want to process?:")#C:\\Users\\SMathew\\Desktop\\TEMP\\bob.csv
print "I thought so"
df=pd.read_csv(location, index_col=[0])
local_0=df['Capacity']# you can index this listof values by doing local_0[i]
queue=0     

#function reads selected column's indexed data from location
def read_data(location): 
        df=pd.read_csv(location, index_col=[0])
        local_0=df['Capacity']# you can index this listof values by doing local_0[i]
        return #local_0[i:len(local_0)]

# plots data contionusly until it notices that voltage hits zero, then its starts a new plot
def multi_plot():
        #Iteration starts 
        i=6
        t=0
        unit=0
        read_data(location)
        
        while t<len(local_0):
                if local_0[i]==0:
                        read_data(location)
##                        writer = csv.writer(open("Voltage"+[unit]+".csv", "wb"))
##                        ##String[] entries = "Time#Voltage".split("#");
##                        writer.writerows(local_0[i])
##                        writer.close()
                       
                else:
                       plotfile(local_0,0,1) 
                
                               
                i=i+1
                t=t+1
                print "lol"
        return

multi_plot()
# set up the three lines

trace1 = Scatter(
    x=[0, 1, 2],
    y=[10, 11, 12]
)
trace2 = Scatter(
    x=[2, 3, 4],
    y=[100, 110, 120],
    yaxis='y2'
)
trace3 = Scatter(
    x=[3, 4, 5],
    y=[1000, 1100, 1200],
    yaxis='y3'
)

data = Data([trace1, trace2, trace3])

layout = Layout(
    yaxis=YAxis(
        domain=[0, 0.33]
    ),
    legend=Legend(
        traceorder='reversed'
    ),
    yaxis2=YAxis(
        domain=[0.33, 0.66]
    ),
    yaxis3=YAxis(
        domain=[0.66, 1]
    )
)
fig = Figure(data=data, layout=layout)

plot_url = py.plot(fig, filename='stacked-coupled-subplots')

        
        ##if local_0[i] is not 0:
        ##        print local_0[i]
        ##else:
        ##	print "Boo!"	
        ##i=i+1
        #going to the next cycle when voltage=0

        ##location=raw_input("What data do you want to process?:")
        ##fname = cbook.get_sample_data(location, asfileobj=False)
        ##print "I thought so"

        ##plotfile(fname,(0,1,5,6,8,30))# file name, cycle #, discharge per cycle, Ah, Wh, Charge time per cycle, discharge time from 13.8 to the end.

        ##show()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
