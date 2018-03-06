#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 14:08:37 2018

@author: nadine
"""

import numpy as np

def sealevelSinusoid(mean,amplitude,time,period):
    sealevel = mean + (amplitude * np.sin((2*np.pi*time)/period))
    return sealevel