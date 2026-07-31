# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 07:34:30 2026

@author: USER
"""

import numpy as np
sum = 0
n = np.arange(0,121,2)
for i in range(len(n)):
    sum = sum+n[i]
print("The sum of even numbers below 121 is: ",sum)
