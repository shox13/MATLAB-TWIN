import csv
import pytz
import pandas as pd # great library for examining data \('3')/
from pandas import DataFrame
import matplotlib.pyplot as plt
from pylab import plotfile, show, gca
import matplotlib.cbook as cbook
import time

plt.figure('Energy') # Name the graph antyhing you want!

#default condtions to for csv. commands=================================================================================
dia = csv.excel()
dia.quoting = csv.QUOTE_NONE
o=0# bla 

#user specifies location
location=raw_input("What data do you want to process?:")#C:\\Users\\SMathew\\Desktop\\TEMP\\bob.csv
#location='C:\\Users\\SMathew\\Desktop\\TEMP\\bob.csv'
print "I thought so"

df=pd.read_csv(location, index_col=[0])
kicks=raw_input("What column do you want to look at?")#Energy
#kicks='Energy'
local_0=df[kicks]# you can index this list of values by doing local_0[i]

#time=[1,2,3,4,45,5,6,7,7,88,90,5,3,2]# for a sample x-axis, not very important
count=0

#function reads selected column's indexed data from location !!!!REPEAT!!!!!

def read_data(location): #=============================================================================================
        df=pd.read_csv(location, index_col=[0])
        local_0=df[kicks]# you can index this listof values by doing local_0[i]
        return

def cycle_find(count,delta):#==========================================================================================
      #Iteration starts 
        o=0
        t=0
        i=0
        j=1
        #inital i stored as 
        read_data(location)
        while i<len(local_0):#loops through the whole list, please don't be long :S
               
                if local_0[j]==0:
                        count=count+1
                        t=t+1
                        read_data(location)
                        print i,j-1
                        delta=j-i
                        i=i+delta# move up i to next starting position after j.
                                                                                        
                else:       
                        j=j+1
                                        
                t=t+1
                j=j+1

        return local_0[i:cycle_find(count,j)]#cycle_find(count,j)]


#GLOBAL ASSIGNMENTS========LEGGO!================================================================================
j=1
i=0
delta=0


cycle_find(0,0)# this is the key function being carried out to find your phases

#This is where the magic happens!!!!!! Yayyyyyy (*U*)/*+*+* =====================================================

# plt.plot(local_0[0:103],'b*-',local_0[118:275],'go-',local_0[291:461],'r-',)#multi_plot(2),'b*')#'b*-',multi_plot(31),'go',)
# plt.axis([0, 10, 0, 5]) # axis scales, don't worry  we zoom in.
# plt.xlabel('X-title')
# plt.ylabel('Y-title')
# plt.title('EBB S/N')
# plt.annotate('A graph!', xy=(2, 1), xytext=(3, 1.5),arrowprops=dict(facecolor='black', shrink=0.05))
# plt.show()#um, you want to show the plot on the figure right?


#Leave an uplifting message

print "Wow, that was fast"        
     


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
