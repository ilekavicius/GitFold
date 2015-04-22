import numpy as np
import matplotlib.pyplot as plt
import sys
from math import sqrt
        
with open('C:/Users/IL/Documents/SciComp/HWK3/pt1.txt') as file:
    storms = [[float(digit) for digit in line.split()] for line in file]
#storms 2d array, 8 X something
# (ID, Lat, Long, wind speed, central pressure, year, time, categ )


#Get Hurricane frequency
size = len(storms)
ID = storms[0][0]
track = []

for i in range(0, size, 1):
    if storms[i][0] != ID:
       
        ID = storms[i][0]
        track.append(storms[i][5])
        
 
      
counts = plt.hist(track, bins = [1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010])   
plt.show()
print counts


#Central Pressure Histogram
#New text file, no 0's in central pressure
with open('C:/Users/IL/Documents/SciComp/HWK3/new4.txt') as file:
    storms = [[float(digit) for digit in line.split()] for line in file]
    
pressTrack = []
thresh = 2000
ID = storms[0][0]
size = len(storms)
for i in range(0, size, 1):
    if storms[i][0] == ID:
        if storms[i][4] <thresh:
            thresh = storms[i][4]
    else:
        ID = storms[i][0]
        pressTrack.append(thresh)
        thresh = storms[i][4]
        
 
      
plt.hist(pressTrack)   
plt.show()
#Calc mean and std
print reduce(lambda x, y: x+y, pressTrack)/len(pressTrack)

print np.std(pressTrack)

#Calculate spin up time
timeTrack = []

ID = storms[0][0]
time1 = time2 =0
size = len(storms)

for i in range(0, size, 1):
    if storms[i][0] == ID:
        if storms[i][4] >= 1000:
            time1 = storms[i][6]
        elif  storms [i][4] <= 970:
            time2 = storms[i][6]
            if time1!=0:
                timeTrack.append(time2-time1)
                time1 =0 #So I don't repeat this step for this ID
    else:
        ID = storms[i][0]
        time1 = time2 = 0
        if storms[i][4] >= 1000:
            time1 = storms[i][6]
        elif  storms [i][4] <= 970:
            time2 = storms[i][6]
            if time1!=0:
                timeTrack.append(time2-time1)
                time1 =0
                
plt.hist(timeTrack)
    