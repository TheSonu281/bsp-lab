import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter,filtfilt
import math

signal=np.loadtxt('C:/Users/mec/Documents/SONU SREYA/hr.csv',delimiter=',')
b, a = butter(2, 0.2, btype='high', analog=False,fs=500) 
y = filtfilt(b, a, signal) 
b, a=butter(2,100, btype='low', analog=False,fs=500)
yy = filtfilt(b,a,y)
signal = yy
plt.subplot(2,2,1)
plt.xlabel("position")
plt.ylabel("amplitude")
plt.title("ECG before thresholding")
plt.plot(signal[0:2000])
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
plt.plot(msig[0:2000])
l1=len(msig)
rpos = []
rpeak = []
rcount =0
for i in range(l1):
    if(msig[i]>msig[i-1] and msig[i]>msig[i+1]):
        rpos=np.append(rpos,i)
        rpeak = np.append(rpeak,msig[i])
        rcount = rcount + 1
f=500
rpos = rpos/f
sd = []
l1 = len(rpos)
for i in range(l1-1):
    d=rpos[i+1]-rpos[i]
    sd = np.append(sd, d)
avnn=np.mean(sd)
print("AVNN: ",avnn)
sdnn=np.std(sd)
print("SDNN: ", sdnn)
ssd = sd**2
mssd = np.mean(ssd)
rmssd = math.sqrt(mssd)
print("RMSSD: ",rmssd)
sdsd = np.std(sd)
print("SDSD: ",sdsd)

nn50 = 0
for i in range(len(sd)):
    if sd[i]>0.050:
        nn50 = nn50 + 1
print("NN50: ",nn50)
pnn50=(nn50/rcount)*100
print("PNN50: ",pnn50)
mhr = 60/avnn
min_hr = 60/max(sd)
max_hr = 60/min(sd)
print("Mean heart rate: ",mhr)
print("minimum heart rate: ",min_hr)
print("maximum heart rate: ",max_hr)