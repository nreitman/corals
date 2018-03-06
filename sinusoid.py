#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Calculate a sinusoidal signal

for anything
(time or ELA or temperature or sea level, ETC)

inputs are mean value, amplitude, time, and period

Created on Mon Feb 26 09:45:06 2018
@author: nadine
"""
import numpy as np

def sinusoid(mean,amplitude,time,period):
    signal = mean + (amplitude * np.sin((2*np.pi*time)/period))
    return signal