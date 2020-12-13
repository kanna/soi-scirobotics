#!/usr/bin/env python3


import glob
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()
df = pd.read_csv("Flt2.csv")
print(df.shape)
y = df['Latitude']
x = df['Longitude']
dms = df['Final.out']
plt.scatter(x,y,c=dms,cmap='jet',label="DMS concentration",s=0.1)
plt.colorbar()
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
#plt.figure().set_title("sadfsdf")
#plt.show()
