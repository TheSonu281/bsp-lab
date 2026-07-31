# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 07:58:09 2026

@author: USER
"""

import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0,10,0.1)
f = 0.25
A = 2
a = A*np.sin(2*np.pi*f*t)
plt.subplot(2,2,1)
plt.plot(t,a)
plt.title("sine wave 1")
plt.xlabel("time")
plt.ylabel("amp")
plt.grid(True)

f1 = 2
B = 3
b = B*np.sin(2*np.pi*f1*t)
plt.subplot(2,2,2)
plt.plot(t,b)
plt.title("sine wave 2")
plt.xlabel("time")
plt.ylabel("amp")
plt.grid(True)

c = a+b
plt.subplot(2,2,3)
plt.plot(t,c)
plt.title("sine wave 3")
plt.xlabel("time")
plt.ylabel("amp")
plt.grid(True)