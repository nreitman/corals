#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Code for Exercise 6: Coral Growth in the face of sea level and tectonic change.

Created on Thu Mar  1 13:23:43 2018

@author: nadine
"""
#%% import modules 
import numpy as np
import matplotlib.pyplot as plt
import os
import sinusoid
import coralgrowth

#%% INITIALIZE

# define variables
xmax = 2000.
dx = 1.
x = np.arange(0,xmax+dx,dx)

tmax = 40000. # run model for this many years
dt = 1 # some portion of one year 
time = np.arange(0,tmax+dt,dt)

# initial topography must cross sea level and be high and low enough to accommodate upflit and subsidence
zbmax = 300. # meters
#zmin = -300. # meters
slope = .3 # slope in meters/meters
zb = np.zeros(shape=(len(x),len(time)),dtype=float)
zb[:,0] = zbmax - (slope*x)  # initial bedrock topography in meters...start with a slope
zb[:,1] = zbmax - (slope*x)

U = np.zeros(len(time))
U[:] = .001 # uplift rate...start with steady rate [m/yr] for all time

#sea level parameters
mean = 0.
amplitude = 150. # meters
period = 40000. # period for sinusoidal sea level in years
SL = sinusoid.sinusoid(mean,amplitude,time,period)

# initialize arrays
topo = np.zeros(shape=(len(zb),len(time)),dtype=float)
topo[:,0] = zb[:,0]
depth = SL[0] - topo[:,0]
coral = np.zeros(shape=(len(zb),len(time)),dtype=float)

#%% PLOT INITIAL CONDITIONS

# plot initial topography
plt.plot(x,zb[:,0],color='black')
plt.axhline(SL[0],0,xmax,color='blue')
#plt.fill_between(depth[:,0],topo[:,0],facecolor='blue')
plt.xlim(0,xmax)
plt.xlabel('distance [m]')
plt.ylabel('initial topography [m]')
plt.title('initial topography & mean sea level')
plt.axes().set_aspect('equal', 'datalim')
#plt.ylim(-500,500)
plt.grid(color='lightgray',linestyle=':')
plt.show()

# plot sea level condition
plt.plot(time,SL,color='blue')
plt.xlabel('time [years]')
plt.ylabel('sea level [meters]')
plt.title('sea level condition')
plt.grid(color='lightgray',linestyle=':')
plt.show()



#%% RUN

#for i in range(1,len(time)-1):
#    topo[:,i] = topo[:,i] + (U[i] * dt) # uplift topography for this time step and all space
#    depth = SL[i] - topo[:,i] # calculate ocean depth at this time for all space
#    coral[:,i] = coral[:,i-1] + (coralgrowth.coralGrowthRate(depth) * dt) # grow coral for this time and all space
#    topo[:,i+1] = topo[:,i] + coral[:,i]  # add coral growth at this time to topo at the time for all space to get topo at next time
#    zb[:,i+1] = topo[:,i+1] - coral[:,i] # calculate uplifted bedrock for next time
    
#% RUN v2
for i in range(0,len(time)-1):
    depth = SL[i] - topo[:,i] # calculate ocean depth at this time for all space
    coral[:,i] = coral[:,i-1] + (coralgrowth.coralGrowthRate(depth) * dt) # grow coral for this time and all space
    zb[:,i+1] = zb[:,i] + (U[i] * dt) # calculate uplifted bedrock for next time
    topo[:,i+1] = zb[:,i+1] + coral[:,i] # add coral growth at this time to upliftted bedrock at next time for all space to get topo at next time


#%% PLOT OUTPUT

# plot coral growth only
        
plot = 1000

for i in range(1,len(time)-1):
    if i % plot == 0:
        #plt.fill_between(x,coral[:,i],zb[:,i],color='lightcoral')
        #plt.plot(x,coral[:,i],color='lightcoral')
        plt.plot(x,coral[:,i],label=str(int(i*dt))+' years')

plt.ylabel('height [m]')
plt.xlabel('distance [m]')
plt.title('coral growth')
plt.legend(bbox_to_anchor=(1.05, 1.025),fancybox=False, shadow=False) #edgecolor='black')
plt.show()
    
##%% plot few frames of everything
#
#for i in 1,2,3,4,5,6,7,8,9,10:
#    fig, (ax1, ax2, ax3) = plt.subplots(3, 1,sharex=True)
#    plt.tight_layout()
#    plt.xlim(0,xmax)
#    
#    ax1.plot(x,coral[:,i],color='lightcoral',linewidth=0.5,label='coral growth')
#    ax1.set_ylabel('coral height [m]')
#    ax1.set_title('coral growth')
#    ax1.set_ylim(0,.2)
#    ax1.text(250,.16,str(time[i])+' years')
#    
#    #ax2.plot(x,topo[:,i],color='gray',linewidth=0.5,label='topo')
#    ax2.fill_between(x,SL[i],topo[:,i],color='royalblue',where=(topo[:,i]<=0.))
#    ax2.fill_between(x,topo[:,i],-300,color='gray',alpha=0.5)
#    ax2.fill_between(x,zb[:,i]+coral[:,i],zb[:,i],color='lightcoral',where=(coral[:,i]>0.01))
#    ax2.set_ylabel('elevation [m]')
#    ax2.set_title('topography')
#    #ax2.set_ylim(-250,250)
#    ax2.set_aspect('equal', 'datalim')
#
#    #ax3.plot(x,zb[:,i],linewidth=0.5,color='black',label=str(int(i*dt))+' years') #label='bedrock')
#    ax3.axhline(SL[i],0,xmax,linewidth=0.5,color='blue')
#    ax3.set_ylabel('elevation [m]')
#    ax3.set_xlabel('distance [m]')
#    ax3.set_ylim(0,1)
#    ax3.set_title('sea level')
#
#    plt.savefig('tmp'+str(i)+'.png',bbox_inches="tight",dpi=200)
#    plt.close()

#%% plot many frames of everything

plot = 200

for i in range(0,len(time)-1):
    if i % plot == 0:

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1,sharex=False,figsize=(6,5))
        plt.tight_layout(h_pad=4.0)
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        #plt.suptitle('GENERAL FIGURE TITLE', fontsize=12)
    
        ax1.plot(x,coral[:,i],color='lightcoral',linewidth=0.75)
        ax1.set_ylabel('coral height [m]',fontsize=10)
        ax1.set_xlabel('distance [m]',fontsize=10)
        ax1.set_title('coral growth',fontsize=11)
        ax1.set_xlim(0,xmax)
        ax1.set_ylim(0,135)
        ax1.text(100,100,str(np.int(time[i]))+' years')
    
        ax2.fill_between(x,SL[i],topo[:,i],color='royalblue',where=(topo[:,i]<=SL[i]))
        ax2.fill_between(x,topo[:,i],-300,color='gray',alpha=0.5)
        ax2.fill_between(x,zb[:,i]+coral[:,i],zb[:,i],color='lightcoral',where=(coral[:,i]>0.015))
        #ax2.axhline(SL[i],0,xmax,linewidth=0.5,color='blue')
        #ax2.fill_between(x,topo[:,i],topo[:,i-1],color='lightcoral',where=(coral[:,i]>0.015))
        ax2.set_ylabel('elevation [m]',fontsize=10)
        ax2.set_xlabel('distance [m]',fontsize=10)
        ax2.set_title('topography',fontsize=11)
        ax2.set_ylim(-300,300)
        ax2.set_xlim(0,xmax)
        #ax2.set_aspect('equal', 'datalim')
        

        #ax3.axhline(SL[i],0,xmax,linewidth=0.5,color='blue')
        ax3.plot(time,SL,color='blue')
        ax3.plot(time[i],SL[i],'.',color='red')
        ax3.set_ylabel('elevation [m]',fontsize=10)
        ax3.set_xlabel('time [yrs]',fontsize=10)
        ax3.set_xlim(0,tmax)
        ax3.set_ylim(-170,170)
        #ax3.set_xlabel('distance[m]')
        ax3.set_title('sea level',fontsize=11)
        ax3.grid(color='lightgray',linestyle=':')

        plt.savefig('tmp'+str(i/plot)+'.png',bbox_inches="tight",dpi=300)
        plt.close()
    
#%% make a movie with ffmpeg
## -r = fps
os.system("rm movie.mp4") # remove a previous movie.mp4 file so don't get overwrite problems
os.system("ffmpeg -r 5 -pattern_type sequence -i tmp'%d'.png -vcodec mpeg4 movie.mp4") 
os.system("rm tmp*.png")

    
