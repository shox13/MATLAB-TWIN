import csv
#import numpy as np
#import matplotlib.pyplot as plt
from pylab import plotfile, show, gca
import matplotlib.cbook as cbook

location=raw_input("What data do you want to process?:")
fname = cbook.get_sample_data(location, asfileobj=False)
print "I thought so"

plotfile(fname,(0,8,5,6,8,30))# file name, cycle #, discharge per cycle, Ah, Wh, Charge time per cycle, discharge time from 13.8 to the end.
fig,ax = plt.subplots()
ax.plot(dat1['timeDiff'],dat1['Value'])
ax.plot(dat2['timeDiff'],dat2['Value'])
plt.show()

show()
