# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:58:59 2026

@author: mec
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter,filtfilt
data =np.loadtxt("C:/Users/mec/Documents/SONU SREYA/ppg.csv",delimiter=',')


plt.figure(figsize=(12,10)) 
 

 
b, a = butter(4, 0.2, btype='high', analog=False,fs=500) 
y = filtfilt(b, a, data) 
b, a=butter(4,200, btype='low', analog=False , fs=500)
yy = filtfilt(b,a,y)
data = yy
data=data[0:2000]
plt.subplot(5,1,1) 
plt.xlabel("position") 
plt.ylabel("amp") 
plt.title("filtered data")
plt.plot(data)

dlen=len(data)
p=[] 
sec=[]
for i in range(2,dlen-2):
    p=(2*data[i-2])-(data[i-1])-(2*data[i])-(data[i+1])+(2*data[i+2])
    sec=np.append(sec,p)

plt.subplot(5,1,2) 
plt.xlabel("position") 
plt.ylabel("amp") 
plt.title("second derivative of data")
plt.plot(sec)
s=[]
smoo=[]
m=32
l=len(sec)

for n in range(31,l):
    sum_=0
    for k in range(1,m):
        w=m-k+1
        s=((sec[n-k+1])**2)*w
        sum_=sum_+ s
    smoo=np.append(smoo,sum_)
    
plt.subplot(5,1,3) 
plt.xlabel("position") 
plt.ylabel("amp") 
plt.title("smoothened data")        
plt.plot(smoo)

#thresholding
l1=len(smoo)
ma=max(smoo)
threshold=ma*0.15 
tsmoo=[] 
for i in range(l1): 
    if(smoo[i]>threshold): 
        tsmoo.append(smoo[i]) 
    else: 
        tsmoo.append(0) 
plt.subplot(5,1,4) 
plt.xlabel("position") 
plt.ylabel("amp") 
plt.title("threshold data") 
plt.plot(tsmoo) 

#turning point algorithm
l2=len(tsmoo)
ppos = []
ppeak = []
for i in range(l2-1):
    if(tsmoo[i]>tsmoo[i-1] and tsmoo[i]>tsmoo[i+1]):
        ppos=np.append(ppos,i)
        ppeak = np.append(ppeak,tsmoo[i])
dpos=[]        
for i in range(len(ppos)-1):
    diff=ppos[i+1]-ppos[i]
    if diff > 100:
        dpos=np.append(dpos,ppos[i])
print(ppos)
print("The approx dicrotic notch positions are:",dpos)

dicroval=[]
l3=len(dpos)
for i in range(l3):
    u=int(dpos[i]+50)
    lo=int(dpos[i]-50)
    z=data[lo:u]
    k= np.argmin(z)
    dicro=k+lo
    dicroval=np.append(dicroval,dicro)
print("final dicrotic notch positions:",dicroval)
dicroval=dicroval.astype(int)
plt.subplot(5,1,5) 
plt.xlabel("position") 
plt.ylabel("amp") 
plt.title("dicrotic notch") 
plt.plot(data)
plt.plot(dicroval,data[dicroval],"r" "*") 

    


    
    
    
        
        
        