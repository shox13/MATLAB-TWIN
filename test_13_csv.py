import csv
import pytz
import numpy as np
import pandas as pd # great library for examining data \('3')/
from pandas import DataFrame
import matplotlib.pyplot as plt
from pylab import plotfile, show, gca
import matplotlib.cbook as cbook
plt.figure()

#default condtions to for csv. commands
dia = csv.excel()
dia.quoting = csv.QUOTE_NONE

#user specifies location
#location=raw_input("What data do you want to process?:")#C:\\Users\\SMathew\\Desktop\\TEMP\\bob.csv
location='C:\\Users\\SMathew\\Desktop\\TEMP\\bob.csv'
print "I thought so"

df=pd.read_csv(location, index_col=[0])
local_0=df['Energy']# you can index this list of values by doing local_0[i]

time=[1,2,3,4,45,5,6,7,7,88,90,5,3,2]# for a sample x-axis, not very important
count=0

#function reads selected column's indexed data from location !!!!REPEAT!!!!!
def read_data(location): 
        df=pd.read_csv(location, index_col=[0])
        local_0=df['Energy']# you can index this listof values by doing local_0[i]
        return #local_0[i:len(local_0)]

# plots data contionusly until it notices that voltage hits zero, then its starts a new plot
def cycle_find(count,j):
      #Iteration starts 
        t=0
        
        #inital i stored as 
        read_data(location)
        while t<1000:#len(local_0)-1:
                if local_0[j]==0:
                        count=count+1
                        t=t+1
                        read_data(location)
                           
                else:       
                        print local_0[j]
                t=t+1
                j=j+1
        return j
                                                
#keep plotting until the data set is clear        

def multi_plot(count):
        ping=1#len(local_0)-1# just used for a while loop condition
        while ping>0:
                
                #print local_0[i]# starting index
                cycle_find(count,j)
                
                
                ping=ping-1
                #print local_0[i:cycle_find(count,j)]
                return local_0[i:45]#cycle_find(count,j)]

#multi_plot(count)


#graphy=raw_input("What series do you want to plot?:")#multi_plot(count)
i=6
j=6
print "We have to plot stuff now!"
print count
##t1 = np.arange(0.0, 5.0, 0.02)
plt.plot(multi_plot(1),'b*',multi_plot(2),'r-')
plt.axis([0, 50, 0, 50])
plt.show()
        
        #print cycle_find(j)
        #print local_0[i:cycle_find(j)]
       # plt.plot(local_0[i],local_0[cycle_find(j)])# takes the array of data values and plots them
       # plt.plot(trace[count])


#p=1; #iterations for different races/plots
##def trace(p):#each plot
##        cycle_find()
##        return local_0[i:j]
##while p>0:
##        trace(p)
##        p=p+1
##        plt.plot(local_0[i:j])

        
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
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
