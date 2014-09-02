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
local_0=df['Capacity']# you can index this list of values by doing local_0[i]
queue=0     
i=0

#function reads selected column's indexed data from location !!!!REPEAT!!!!!
def read_data(location): 
        df=pd.read_csv(location, index_col=[0])
        local_0=df['Capacity']# you can index this listof values by doing local_0[i]
        return #local_0[i:len(local_0)]

# plots data contionusly until it notices that voltage hits zero, then its starts a new plot
def cycle_find():
      #Iteration starts 
            t=0
            unit=0
            read_data(location)
            
            while t<len(local_0):
                    if local_0[i]==0:
                        read_data(location)
##                        writer = csv.writer(open("Voltage"+[unit]+".csv", "wb"))
##                        String[] entries = "Time#Voltage".split("#");
##                        writer.writerows(local_0[i])
##                        writer.close()                           
                    else:
                           plotfile(local_0,0,1)          
                    i=i+1
                    t=t+1
                    print "lol"
            return i

#while the list of data is full
while local_0>0
p=0
def trace(p):
        j=i
        print j
        cycle_find()
        return local_0[j:i]
        p=p+1

data = Data([trace(p))

layout = Layout(
    yaxis=YAxis(
        domain=[0, 17]
    ),
    legend=Legend(
        traceorder='reversed'
    ),
    )
fig = Figure(data=data, layout=layout)

plot_url = py.plot(fig, filename='stacked-coupled-subplots')
    

    return "hello"
        
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
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
