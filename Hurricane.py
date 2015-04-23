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
                
#plt.hist(timeTrack)
#plt.title("Spin Up time in hours")
    
#Calculate Time at cat 3 or above
catTrack = []

ID = storms[0][0]
time1 = time2 =0
size = len(storms)
a=0
for i in range(0, size, 1):
    if storms[i][0] == ID:
        if storms[i][7] >= 3:
            if a == 0: #If first time looking at storm
                time1 = storms[i][6]
                a=1
            else:
                time2 = storms[i][6]
            
    else:
        a=0
        ID = storms[i][0]
        if time2-time1 < 1000 and time2-time1>0: #function fails for single entry Storm !Ds
            catTrack.append(time2-time1)
            catTrack.append(storms[i-1][5])
 #       catTrack.append(storms[i-1][5])
        time1 = time2 = 0
        if storms[i][7] >= 3:
            if a == 0: #If first time looking at storm
                time1 = storms[i][6]
                a=1
            else:
                time2 = storms[i][6]
         
catSorted = np.reshape(catTrack, ((len(catTrack)/2,2)))
#print catTrack
plt.hist(catSorted[:,0] , bins = [1,2,3,4,5,6,7,8,9,10,11,12])
plt.show()


#Find histogram of cat time per decade
aveHours = []
i =1900
temp = 0
count =0

for j in range(0, len(catTrack)/2+1,1):
    if j ==len(catTrack)/2:
        aveHours.append(temp/count)
    elif catSorted[j,1] >= i and catSorted[j,1] <= i+10:
        temp += catSorted[j,0]
        count +=1
    else:
        if count != 0:
            aveHours.append(temp/count)
        i+=10
        count = temp =0
print aveHours
            
#Florida Coast
            
ID = storms[0][0]
florida = np.zeros((11))
size = len(storms)
a=0

for i in range(0, size, 1):
    if storms[i][0] == ID:
        if storms[i][1] >= 25 and storms[i][1] <= 30 and storms[i][2] <= -75 and storms[i][2] >= -80:
            
            if a == 0: #If first time looking at storm
                florida[int(storms[i][5]/10)-190] += 1
                a=1
               
            else:
                a=0
                
    else:
        ID =  storms[i][0]
        if storms[i][1] >= 25 and storms[i][1] <= 30 and storms[i][2] <= -75 and storms[i][2] >= -80:
            
            if a == 0: #If first time looking at storm
                florida[int(storms[i][5]/10)-190] += 1
                a=1
               
            else:
                a=0
                
                
#Max Intensity at coast
ID = storms[0][0]
floridaCat = np.zeros((412,3))
size = len(storms)
a=0
count =0

for i in range(0, size, 1):
    
    if storms[i][0] == ID:
        if storms[i][1] >= 25 and storms[i][1] <= 30 and storms[i][2] <= -75 and storms[i][2] >= -80:
            
            if storms[i][7]> floridaCat[count,2]: #If category is higher
                floridaCat[count,0] = storms[i][1]
                floridaCat[count,1] = storms[i][2]
                floridaCat[count,2] = storms[i][7]
                               
            
                
    else:
        ID =  storms[i][0]
        count +=1
    
#There are a bunch of 0 rows in floridaCat, find and delete
garbagePos =[]
for i in range(0, 412,1):
    if floridaCat[i,0]==0 and floridaCat[i,1]==0:
        garbagePos.append(i)
floridaCat = np.delete(floridaCat, (garbagePos), axis =0)        
print floridaCat 