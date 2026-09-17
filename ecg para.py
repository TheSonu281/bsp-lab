# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:26:57 2026

@author: mec
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:39:34 2026

@author: mec
"""

import numpy as np
import matplotlib.pyplot as plt
signal=np.loadtxt('C:/Users/mec/Documents/SONU SREYA/ECG normal.csv',delimiter=',')
plt.subplot(2,2,1)
plt.xlabel("position")
plt.ylabel("amplitude")
plt.title("ECG before thresholding")
plt.plot(signal)
l = len(signal)
m = max(signal)
msig=[]
t = (50/100)*m
for i in range(l):
    if(signal[i]>t):
        msig=np.append(msig,signal[i])
    else:
        msig=np.append(msig,0)
plt.subplot(2,2,2)
plt.xlabel("position")
plt.ylabel("amplitude")
plt.title("ECG after thresholding")
plt.plot(msig)
l1=len(msig)
rpos = []
rpeak = []
for i in range(l1):
    if(msig[i]>msig[i-1] and msig[i]>msig[i+1]):
        rpos=np.append(rpos,i)
        rpeak = np.append(rpeak,msig[i])
#qrs normal range from 0.07-0.1 

q = []
s = []

for i in rpos:
    u = int( i) 
    l = int(i-5)
    for j in range(l,u+1):
        if(signal[j]<signal[j-1] and signal[j]<signal[j+1]):
            q = np.append(q,j)
            
for k in rpos:
    l = int( k) 
    u = int(k+5)
    for m in range(l,u+1):
        if(signal[m]<signal[m-1] and signal[m]<signal[m+1]):
            s = np.append(s,m)
            
print("The q peak values are",q)
print("The s peak values are",s)

dur = s - q
print("The QRS width is ",(np.mean(dur)/125))
ppos=[]
pamp=[]
for i in q:
    u = int(i)
    l = int(i-20)
    D = signal[l:u]
    maximum=max(D)
    n=np.argmax(D)
    n=n+l
    ppos=np.append(ppos,n)
    pamp=np.append(pamp,maximum)
print("P wave positions are",ppos)
print("p wave amplitudes are",pamp)
print("p wave amplitude mean is ",np.mean(pamp))

#pwave duration is normally 0.08-0.11sec
a=[]
b=[]
pdur=[]
for i in ppos:
    u=int(i)
    l=int(i-8)
    for k in [u,l+1,-1]:
        ponset=max(0,signal[k])
        if(ponset==0):
            a=np.append(a,k)
            break
        
print(a) 

for j in ppos:
    l=int(j)
    u=int(j+8)
    for t in [l,u+1]:
        poffset=max(0,signal[t])
        if(poffset==0):
            b=np.append(b,t)
            break  
# # print(b)       
# pdur=b-a
# # print(pdur)
# pmean=np.mean(pdur)
# # print(pmean)
# # print("P wave duration is:",pmean/125)

tpos=[]
tamp=[]
l3=len(s)
s=s[0:l3-1]
for i in s:
    l = int(i)
    u = int(i+20)
    print(u)
    print(l)
    D1 = signal[l:u]
    maxim=max(D1)
    nt=np.argmax(D1)
    nt=nt+l
    tpos=np.append(tpos,nt)
    tamp=np.append(tamp,maxim)
print("T wave positions are",tpos)
print("T wave amplitudes are",tamp)
print("T wave amplitude mean is ",np.mean(tamp))
a1=[]
b1=[]
tdur=[]

for i in tpos:
    u=int(i)
    l=int(i-30)
    print(u)
    print(l)
    for k in [u,l+1,-1]:
        tonset=max(0,signal[k])
        print(tonset)
        
        if(tonset==0):
            a1=np.append(a1,k)
            
            break
        


for j in tpos:
    l=int(j)
    u=int(j+20)
    for t in [l,u+1]:
        toffset=max(0,signal[t])
        if(toffset==0):
            b1=np.append(b1,t)
            break  
print(b1)       
tdur=b1-a1
print(tdur)
tmean=np.mean(tdur)
print(tmean)
print("T wave duration is:",tmean/125)









    