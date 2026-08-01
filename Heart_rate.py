import numpy as np
import matplotlib.pyplot as plt

signal = np.loadtxt('C:/Users/USER/OneDrive/Dokumen/Resorces and notes/2026(S5)/PCEBL508(BSP lab)/ECG normal.csv',delimiter= ',')

plt.subplot(2,2,1)
plt.xlabel("position")
plt.ylabel("amplitude")
plt.title("ECG before thresholding")
plt.plot(signal)
l=len(signal)
m=max(signal)
msig=[]
t=(50/100)*m
for i in range(l):
    if(signal[i]>t):
        msig = np.append(msig,signal[i])
    else:
        msig = np.append(msig, 0)

plt.subplot(2,2,2)
plt.xlabel("position")
plt.ylabel("amplitude")
plt.title("ECG after thresholding")
plt.plot(msig)
l1 = len(msig)
rpos = []
rpeak = []
for i in range(l1):
    if(msig[i]>msig[i-1] and msig[i]>msig[i+1]):
        rpos = np.append(rpos, i)
        rpeak = np.append(rpeak,msig[i])
print(rpos)
print(rpeak)
l2 = len(rpos)
rdiff = []

for i in range(l2 - 1):
    diff = rpos[i+1] - rpos[i]
    rdiff = np.append(rdiff, diff)

print(rdiff)
avg = np.mean(rdiff)
print(avg)
hr = (60*125)/avg
print("heart rate: ",round(hr))








#C:/Users/USER/OneDrive/Dokumen/Resorces and notes/2026(S5)/PCEBL508(BSP lab)
#C:/Users/mec/Documents/SONU SREYA/ECG normal.csv'
#"C:\Users\USER\OneDrive\Dokumen\Resorces and notes\2026(S5)\PCEBL508(BSP lab)\ECG normal.csv"