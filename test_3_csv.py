import csv
#import numpy as np
import matplotlib.pyplot as plt
from pylab import plotfile, show, gca
import matplotlib.cbook as cbook

dia = csv.excel()

dia.quoting = csv.QUOTE_NONE

#set dialecting for default csv.
pd.read_csv(StringIO(data), dialect=dia)
# read file location and select column for indexing
pd.read_csv('foo.csv', index_col=[0, 'A'])


location=raw_input("What data do you want to process?:")
fname = cbook.get_sample_data(location, asfileobj=False)
print "I thought so"

plotfile(fname,(0,8,5,6,8,30))# file name, cycle #, discharge per cycle, Ah, Wh, Charge time per cycle, discharge time from 13.8 to the end.


show()
