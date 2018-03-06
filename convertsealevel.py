#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 21:49:55 2018

@author: nadine
"""

import numpy as np
import matplotlib.pyplot as plt


#%% import del18O data and its time
file = open('LR04stack_no_header.txt','r')
data = file.readlines()
time = []
del18O = []
for line in data:
    test = line.split()
    print test
    time.append(test[0])
    del18O.append(test[1])

time = np.asarray(time,dtype=np.float)
del18O = np.asarray(del18O,dtype=np.float)

scaling = 160./(5.-3.)
sealevel = 254. - (scaling * del18O) # scaling by Bob

#%%  plot unscaled del18O vs time
    
plt.plot(time,del18O)
plt.xlabel('time [yrs]')
plt.ylabel('del18O [o/oo]')
plt.show()

plt.plot(time,sealevel)
plt.xlabel('time [yrs]')
plt.ylabel('sea level [m]')
plt.show()