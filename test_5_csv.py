import csv
import pytz
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
from pylab import plotfile, show, gca
import matplotlib.cbook as cbook

dia = csv.excel()

dia.quoting = csv.QUOTE_NONE
i=0

# read file location and select column for indexing
df=pd.read_csv('C:\\Users\\SMathew\\Desktop\\TEMP\\bob.csv', index_col=[0])
local_0=df['Capacity']# you can index this listof values by doing local_0[i]
#print local_0[8]

##if local_0[i] is not 0:
##        print local_0[i]
##else:
##	print "Boo!"	
##i=i+1
#going to the next cycle when voltage=0

##location=raw_input("What data do you want to process?:")
##fname = cbook.get_sample_data(location, asfileobj=False)
##print "I thought so"

##plotfile(fname,(0,8,5,6,8,30))# file name, cycle #, discharge per cycle, Ah, Wh, Charge time per cycle, discharge time from 13.8 to the end.

##show()
