import time
from pylab import *

plt.ion()               # turn interactive mode on

# initial data
na_data = np.loadtxt('C\Users\SMathew\Documents\4186-56-03699.txt', delimiter=',',skiprows=0, usecols=None)

na_temp1_x = na_data[::2,0]         #every odd row x axis
na_temp2_x = na_data[1::2,0]            #every even row x axis

na_temp1_y = na_data[::2,1]         #every odd row 
na_temp2_y = na_data[1::2,1]            #every even row
o
# initial plot
plt.plot(na_temp1_x, na_temp1_y, label="Temp 1")            #plots graph for temp     sensor 1
plt.plot(na_temp2_x, na_temp2_y, label="Temp2")         #plots graph for temp sensor 2
plt.axis([0, 100, 0, 40])
plt.legend(loc="upper left")                    #puts legend in top left
plt.ylabel('Temp')
plt.xlabel('Time')
grid()
draw()

while True:
    time.sleep(1) # delays for 1 seconds

# update data
na_data = np.loadtxt('/home/pi/Desktop/real_time/ram/data_temp.csv', delimiter=',', skiprows=0, usecols=None)

na_temp1_x = na_data[::2,0]         #every odd row x axis
na_temp2_x = na_data[1::2,0]            #every even row x axis

na_temp1_y = na_data[::2,1]         #every odd row 
na_temp2_y = na_data[1::2,1]            #every even row

#plt.relim()
#plt.autoscale_view(True,True,True)

# initial plot
plt.plot(na_temp1_x, na_temp1_y, label="Temp 1")            #plots graph for temp sensor 1
plt.plot(na_temp2_x, na_temp2_y, label="Temp2")         #plots graph for temp sensor 2


draw()

#time.sleep(30)
