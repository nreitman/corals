#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 14:08:37 2018

@author: nadine
"""

import numpy as np

def coralGrowthRate(depth):
    """
    Doctest:
    >>> depth = np.array([-1.,0.,1.,2.,])
    >>> G = coralgrowth(depth)
    >>> G
    np.array([0,0,...,...])
    """
    Gm = .012 # max upward growth rate, 10-15 mm/yr
    I0 = 2200. * 365.25*24*60*60 # surface light intentsity 2000-2500 muE/m^2*s
    Ik = 200.  * 365.25*24*60*60 # saturating light intensity 50-450 muE/m^2*s
    k = 0.08  # extinction coefficient 0.04-0.16 per m
    G = np.zeros(len(depth))
    below = np.where(depth>0.)[0]
    G[below] = Gm * np.tanh((I0*np.exp(-k*depth[below]))/Ik)
    return G
