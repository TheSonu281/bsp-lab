# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 08:23:36 2026

@author: USER
"""

import math
import numpy as np
data = [1,2,3,4,5]
l = len(data)
m = np.mean(data)
su = 0
for i in data:
    s = (i-m)**2
    su = su + s
sd = math.sqrt(su/l)
g = np.std(data)
print("Standard deviation: ", sd)
print(g)