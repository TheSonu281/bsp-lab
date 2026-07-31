# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 08:16:03 2026

@author: USER
"""

f1 = 0
f2 = 1
n = int(input("Enter range: "))
print("Fibonacci series:")
for i in range(n):
    print(f1, end=" ")
    f3 = f1 + f2
    f1 = f2
    f2 = f3
