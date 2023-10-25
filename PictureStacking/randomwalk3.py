import numpy as np
from matplotlib import pyplot as plt
import math 
from math import sqrt
import random
import array as arr
from matplotlib.patches import Rectangle
import pylab as pl
from matplotlib import collections  as mc
from numpy import sin, cos, pi, linspace
from datetime import datetime

def ABS_Dist(x1,x2,y1,y2):
    result=sqrt((x1 - x2)**2 + (y1 - y2)**2)
    #print(result)
    return result
def onSegment(px,py,qx,qy,rx,ry):
    if qx<= max(px,rx) and qx >= min(px,rx) and qy <= max(py,ry) and qy >= min(py,ry):
        return True
    return False

def orientation(px,py,qx,qy,rx,ry):
    val=(qy-py)*(rx-qx)-(qx-px)*(ry-qy)
    if val>0:
        return 1
    elif val<0:
        return 2
    else:
        return 0

def intersection_check(p1x,p1y,q1x,q1y,p2x,p2y,q2x,q2y):
    o1=orientation(p1x,p1y,q1x,q1y,p2x,p2y)
    o2=orientation(p1x,p1y,q1x,q1y,q2x,q2y)
    o3=orientation(p2x,p2y,q2x,q2y,p1x,p1y)
    o4=orientation(p2x,p2y,q2x,q2y,q1x,q1y)
    if o1 != o2 and o3 != o4:
        return True
    if o1==0 and onSegment(p1x,p1y,p2x,p2y,q1x,q1y):
        return True
    if o2==0 and onSegment(p1x,p1y,q2x,q2y,q1x,q1y):
        return True
    if o3==0 and onSegment(p2x,p2y,p1x,p1y,q2x,q2y):
        return True
    if o1==0 and onSegment(p2x,p2y,q1x,q1y,q2x,q2y):
        return True
    return False
def intersection_test(p1x,p1y,q1x,q1y,trap):#require pass by reference
    valid=False
    for x in range (97):
        #print("kill", x)
        valid=intersection_check(p1x,p1y,q1x,q1y,edge[x,0,0],edge[x,0,1],edge[x,1,0],edge[x,1,1])
        if valid==True:
            return False
    if prisoner[trap]==1:
        for x in range (11):
            #print("kill", x)
            valid=intersection_check(p1x,p1y,q1x,q1y,edge[x,0,0],edge[x,0,1],edge[x,1,0],edge[x,1,1])
            if valid==True:
                return False
    else:
        for x in range (11):
            #print("kill", x)
            valid=intersection_check(p1x,p1y,q1x,q1y,edge[x,0,0],edge[x,0,1],edge[x,1,0],edge[x,1,1])
            if valid==True:
                prisoner[trap]=1
                return True
    return True
    
random.seed(datetime.now().timestamp())

ax=plt.subplot(1,1,1)
edge = [[(3,0),(4,0)], [(4.3,3.3),(4.3,-0.3)], [(4.3,3.3),(7.7,3.3)], [(3,-0.3),(4.3,-0.3)], [(0.6,0),(0.6,6)], [(1,0),(0.6,0)], [(1,-0.3),(1,0)], [(3,0),(3,-0.3)], [(1,-0.3),(-3.8,-0.3)], [(4,4),(4,0)], [(-0.3,6),(0.6,6)], [(-1.1,6),(-1.1,5.8)], [(-1.1,5.8),(-2.9,5.8)], [(-2.9,5.8),(-2.9,5.1)], [(-3.5,6),(-1.1,6)], [(-3.5,5.1),(-2.9,5.1)], [(-3.5,5.1),(-3.5,2.5)], [(-1.1,1.8),(-1.1,1.5)], [(-1.1,1.5),(-3.5,1.5)], [(-3.5,1.5),(-3.5,0)], [(-0.3,0.5),(-0.3,6)], [(-1.5,1.8),(-1.5,2.5)], [(-1.5,2.5),(-3.5,2.5)], [(-1.5,1.8),(-1.1,1.8)], [(-0.3,7),(0,7)], [(-1.1,7),(-1.1,7.3)], [(-3.5,7),(-3.5,6)], [(-3.5,7),(-1.1,7)], [(-1.1,7.3),(-2,7.3)], [(-2,7.3),(-2,7.9)], [(-2,7.9),(-3.5,7.9)], [(-3.5,7.9),(-3.5,9)], [(-3.5,9),(-2.8,9)], [(-2.8,9),(-2.8,10.5)], [(-2.8,10.5),(-0.3,10.5)], [(-0.3,10.5),(-0.3,7)], [(0,10.8),(0,7)], [(-2.8,10.8),(0,10.8)], [(-2.8,13.6),(-2.8,10.8)], [(-0.3,11.6),(0,11.6)], [(-0.3,11.6),(-0.3,13.6)], [(-0.3,13.6),(-2.8,13.6)], [(4.3,4),(4.3,3.6)], [(4.3,3.6),(6,3.6)], [(4,4),(4.3,4)], [(6,3.6),(6,5.1)], [(6,5.1),(6.6,5.1)], [(6.6,5.1),(6.6,3.6)], [(6.6,3.6),(7.4,3.6)], [(7.4,3.6),(7.4,6.3)], [(7.4,6.3),(4,6.3)], [(4,6.3),(4,8)], [(4,8),(4.3,8)], [(4.3,8),(4.3,7.8)], [(4.3,7.8),(4.8,7.8)], [(4.8,7.8),(4.8,7.3)], [(4.8,7.3),(7.4,7.3)], [(7.4,7.3),(7.4,8.8)], [(7.4,8.8),(4,8.8)], [(4,8.8),(4,9.1)], [(2,3.5),(2.7,3.5)], [(2.7,3.5),(2.7,2)], [(2.7,2),(2,2)], [(2,2),(2,3.5)], [(-0.3,0.5),(-0.8,0.5)], [(-0.8,0.5),(-0.8,0)], [(-0.8,0),(-3.5,0)], [(4,9.1),(6.7,9.1)], [(6.7,9.1),(6.7,13.1)], [(6.7,13.1),(2.5,13.1)], [(4.5,12.1),(5.5,12.1)], [(5.5,12.1),(5.5,10.1)], [(5.5,10.1),(4.5,10.1)], [(4.5,10.1),(4.5,12.1)], [(0,13.1),(0,11.6)], [(0,13.1),(1.7,13.1)], [(1.7,13.1),(1.7,13.4)], [(1.7,13.4),(0,13.4)], [(0,13.4),(0,13.9)], [(0,13.9),(-2.8,13.9)], [(-2.8,13.9),(-2.8,14.4)], [(-2.8,14.4),(-3.5,14.4)], [(-3.5,14.4),(-3.5,16.1)], [(-3.5,16.1),(-0.3,16.1)], [(-0.3,16.1),(-0.3,14.7)], [(-0.3,14.7),(0,14.7)], [(0,14.7),(0,15.4)], [(0,15.4),(6.7,15.4)], [(6.7,15.4),(6.7,13.4)], [(6.7,13.4),(2.5,13.4)], [(2.5,13.4),(2.5,13.1)], [(7.7,3.3),(7.7,16.4)], [(7.7,16.4),(-3.8,16.4)], [(-3.8,16.4),(-3.8,-0.3)], [(-3.8,-0.3),(-3.8,-6)], [(-3.8,-6),(7.7,-6)], [(7.7,-6),(7.7,3.3)]]
trap=[[(-2.1,13.6),(-2.1,12.1)],[(-2.1,12.1),(-0.3,12.1)],[(-2.1,10.5),(-2.1,9)],[(-2.1,9),(-0.3,9)],[(-2.9,5.1),(-1.7,5.1)],[(-1.7,5.1),(-1.7,3.6)],[(-1.7,3.6),(-3.5,3.6)],[(3.3,0),(3.3,2)],[(3.3,2),(3.3,4)],[(3.3,4),(4,4)],[(3.3,2),(4,2)]]
edge=np.array(edge)
trap=np.array(trap)


sprawn=[[-2,0.6], [-2,15], [3,14], [5.5,15], [-2.5,12.7], [-2.6,5.4], [-2,2.8], [-2.7,8.4], [-2.5,9.6], [2,-1], [3,2.5], [3,1], [7,4.2], [5.5,7.7], [4,10.5], [4,11.5], [6,10.5], [6,11.5], [2,7.5], [5,5.5], [2,10], [3,-3], [2,5], [6,0], [2,12.5]]
user_count=random.randint(1,20)
if user_count<6:
    user_count=6
sprawn=np.array(sprawn)
#ax=plt.subplot(1,1,1)
user_loc=np.zeros((user_count,2),dtype=float)
#choose 6~20 out of 25 location to activate
chosen_loc = random.sample(range(0, 25), user_count)
prisoner=np.zeros(user_count,dtype=int)
for x in range (0,user_count):
    user_loc[x,0]=sprawn[chosen_loc[x],0]
    user_loc[x,1]=sprawn[chosen_loc[x],1]
duration=10 #sampling duration (1/sampling rate)
T_time=300
counter=user_count
all_loc=np.zeros((duration*T_time*user_count,2),dtype=float)
direction=np.zeros(user_count,dtype=int)
for x in range(user_count):
    all_loc[x,0]=user_loc[x,0]
    all_loc[x,1]=user_loc[x,1]
    #print(all_loc[x,0],"\t",all_loc[x,1])
for x in range(1,T_time*duration):
    if x%100==0:
        print(x)
    for y in range (0,user_count):
        speed=np.random.normal(0.0,2.0)
        direction[y]=random.randint(1,8)
            #print(y,"	",direction[y])
        passed=False
        #print(x,"\t",y)
        while not passed:
            if direction[y]==1:
                passed=intersection_test(user_loc[y,0],user_loc[y,1],user_loc[y,0]+speed/duration,user_loc[y,1], y)
                #print(passed)
                if not passed:
                    direction[y]=random.randint(1,8)
                    #print(y,"	",direction[y])
                else:
                    all_loc[counter,0]=user_loc[y,0]+speed/duration
                    all_loc[counter,1]=user_loc[y,1]
                    user_loc[y,0]=all_loc[counter,0]
                    user_loc[y,1]=all_loc[counter,1]
                    counter+=1
            elif direction[y]==2:
                passed=intersection_test(user_loc[y,0],user_loc[y,1],user_loc[y,0]+0.707*speed/duration,user_loc[y,1]+0.707*speed/duration, y)
                #print(passed)
                if not passed:
                    direction[y]=random.randint(1,8)
                    #print(y,"	",direction[y])
                else:
                    all_loc[counter,0]=user_loc[y,0]+0.707*speed/duration
                    all_loc[counter,1]=user_loc[y,1]+0.707*speed/duration
                    user_loc[y,0]=all_loc[counter,0]
                    user_loc[y,1]=all_loc[counter,1]
                    counter+=1
            elif direction[y]==3:
                passed=intersection_test(user_loc[y,0],user_loc[y,1],user_loc[y,0],user_loc[y,1]+speed/duration, y)
                #print(passed)
                if not passed:
                    direction[y]=random.randint(1,8)
                    #print(y,"	",direction[y])
                else:
                    all_loc[counter,0]=user_loc[y,0]
                    all_loc[counter,1]=user_loc[y,1]+speed/duration
                    user_loc[y,0]=all_loc[counter,0]
                    user_loc[y,1]=all_loc[counter,1]
            elif direction[y]==4:
                passed=intersection_test(user_loc[y,0],user_loc[y,1],user_loc[y,0]-0.707*speed/duration,user_loc[y,1]+0.707*speed/duration, y)
                #print(passed)
                if not passed:
                    direction[y]=random.randint(1,8)
                    #print(y,"	",direction[y])
                else:
                    all_loc[counter,0]=user_loc[y,0]-0.707*speed/duration
                    all_loc[counter,1]=user_loc[y,1]+0.707*speed/duration
                    user_loc[y,0]=all_loc[counter,0]
                    user_loc[y,1]=all_loc[counter,1]
                    counter+=1
            elif direction[y]==5:
                passed=intersection_test(user_loc[y,0],user_loc[y,1],user_loc[y,0]-speed/duration,user_loc[y,1], y)
                #print(passed)
                if not passed:
                    direction[y]=random.randint(1,8)
                    #print(y,"	",direction[y])
                else:
                    all_loc[counter,0]=user_loc[y,0]-speed/duration
                    all_loc[counter,1]=user_loc[y,1]
                    user_loc[y,0]=all_loc[counter,0]
                    user_loc[y,1]=all_loc[counter,1]
                    counter+=1
            elif direction[y]==6:
                passed=intersection_test(user_loc[y,0],user_loc[y,1],user_loc[y,0]-0.707*speed/duration,user_loc[y,1]-0.707*speed/duration, y)
                #print(passed)
                if not passed:
                    direction[y]=random.randint(1,8)
                    #print(y,"	",direction[y])
                else:
                    all_loc[counter,0]=user_loc[y,0]-0.707*speed/duration
                    all_loc[counter,1]=user_loc[y,1]-0.707*speed/duration
                    user_loc[y,0]=all_loc[counter,0]
                    user_loc[y,1]=all_loc[counter,1]
                    counter+=1
            elif direction[y]==7:
                passed=intersection_test(user_loc[y,0],user_loc[y,1],user_loc[y,0],user_loc[y,1]-speed/duration, y)
                #print(passed)
                if not passed:
                    direction[y]=random.randint(1,8)
                    #print(y,"	",direction[y])
                else:
                    all_loc[counter,0]=user_loc[y,0]
                    all_loc[counter,1]=user_loc[y,1]-speed/duration
                    user_loc[y,0]=all_loc[counter,0]
                    user_loc[y,1]=all_loc[counter,1]
                    counter+=1
            elif direction[y]==8:
                passed=intersection_test(user_loc[y,0],user_loc[y,1],user_loc[y,0]+0.707*speed/duration,user_loc[y,1]-0.707*speed/duration, y)
                #print(passed)
                if not passed:
                    direction[y]=random.randint(1,8)
                    #print(y,"	",direction[y)
                else:
                    all_loc[counter,0]=user_loc[y,0]+0.707*speed/duration
                    all_loc[counter,1]=user_loc[y,1]-0.707*speed/duration
                    user_loc[y,0]=all_loc[counter,0]
                    user_loc[y,1]=all_loc[counter,1]
                    counter+=1
                    
for x in range (0,duration*user_count*T_time):
    angle_error=np.random.normal(0.0,360.0)
    length_error=np.random.normal(0.0,0.1)
    x_error=math.cos(math.radians(angle_error))*length_error
    y_error=math.sin(math.radians(angle_error))*length_error
    all_loc[x,0]+=x_error
    all_loc[x,1]+=y_error
    
grid=np.zeros((2240,1150),dtype=int)
g_truth=np.zeros((2240,1150),dtype=int)
for m in range (440,480):
    for n in range(570,600):
        g_truth[n,m]=200
for m in range (350,440):
    for n in range(570,1200):
        g_truth[n,m]=200
for m in range (300,350):
    for n in range(570,600):
        g_truth[n,m]=200
for m in range (0,300):
    for n in range(570,600):
        g_truth[n,m]=200
for m in range (0,30):
    for n in range(600,2240):#5
        g_truth[n,m]=200
for m in range (30,230):
    for n in range(750,850):
        g_truth[n,m]=200
for m in range (230,270):
    for n in range(750,780):
        g_truth[n,m]=200
for m in range (30,90):
    for n in range(1110,1170):
        g_truth[n,m]=200
for m in range (30,270):
    for n in range(1170,1200):
        g_truth[n,m]=200
for m in range (30,180):#10
    for n in range(1300,1390):
        g_truth[n,m]=200
for m in range (180,270):
    for n in range(1300,1330):
        g_truth[n,m]=200
for m in range (30,100):
    for n in range(1500,2040):
        g_truth[n,m]=200
for m in range (100,380):
    for n in range(1650,1680):
        g_truth[n,m]=200
for m in range (350,380):
    for n in range(1300,1650):
        g_truth[n,m]=200
for m in range (100,380):#15
    for n in range(1960,1990):
        g_truth[n,m]=200
for m in range (350,380):
    for n in range(1760,1960):
        g_truth[n,m]=200        
for m in range (380,550):
    for n in range(1910,1940):
        g_truth[n,m]=200
for m in range (30,350):
    for n in range(2210,2240):
        g_truth[n,m]=200
for m in range (350,380):
    for n in range(2070,2240):
        g_truth[n,m]=200
for m in range (380,1150):#20
    for n in range(2140,2240):
        g_truth[n,m]=200
for m in range (1050,1150):
    for n in range(1510,2240):
        g_truth[n,m]=200
for m in range (630,1050):
    for n in range(1910,1940):
        g_truth[n,m]=200
for m in range (830,930):
    for n in range(1610,1810):
        g_truth[n,m]=200
for m in range (780,1150):
    for n in range(1480,1510):
        g_truth[n,m]=200
for m in range (1120,1150):
    for n in range(1530,1480):#25
        g_truth[n,m]=200
for m in range (780,810):
    for n in range(1380,1400):
        g_truth[n,m]=200
for m in range (780,860):
    for n in range(1330,1380):
        g_truth[n,m]=200
for m in range (780,1150):
    for n in range(1230,1330):
        g_truth[n,m]=200
for m in range (810,1120):
    for n in range(930,960):
        g_truth[n,m]=200
for m in range (1120,1150):#30
    for n in range(930,1480):
        g_truth[n,m]=200
for m in range (780,810):
    for n in range(600,1000):
        g_truth[n,m]=200
for m in range (680,810):
    for n in range(570,600):
        g_truth[n,m]=200
for m in range (980,1040):
    for n in range(960,1110):
        g_truth[n,m]=200
for m in range (580,650):
    for n in range(800,950):
        g_truth[n,m]=200

threshold_val=1.3
for x in range (0,duration*user_count*T_time):
    if x%100==0:
        print(x)
    for y in range (x,duration*user_count*T_time):
        check=ABS_Dist(all_loc[x,0],all_loc[y,0],all_loc[x,1],all_loc[y,1])
        if check<(threshold_val*2/duration):
            #print(check,all_loc[x],all_loc[y])
            if all_loc[x,0]>all_loc[y,0] and all_loc[x,1]>all_loc[y,1]:
                start_x=int(round(all_loc[y,0]*100))+380
                start_y=int(round(all_loc[y,1]*100))+600
                end_x=int(round(all_loc[x,0]*100))+380
                end_y=int(round(all_loc[x,1]*100))+600
                for m in range(max(start_x,0),min(end_x,1150)):
                    for n in range(max(start_y,0),min(end_y,2240)):
                        grid[n,m]=200
            elif all_loc[x,0]<all_loc[y,0] and all_loc[x,1]>all_loc[y,1]:
                start_x=int(round(all_loc[x,0]*100))+380
                start_y=int(round(all_loc[y,1]*100))+600
                end_x=int(round(all_loc[y,0]*100))+380
                end_y=int(round(all_loc[x,1]*100))+600
                for m in range(max(start_x,0),min(end_x,1150)):
                    for n in range(max(start_y,0),min(end_y,2240)):
                        grid[n,m]=200
            elif all_loc[x,0]>all_loc[x,0] and all_loc[x,1]<all_loc[y,1]:
                start_x=int(round(all_loc[y,0]*100))+380
                start_y=int(round(all_loc[x,1]*100))+600
                end_x=int(round(all_loc[x,0]*100))+380
                end_y=int(round(all_loc[y,1]*100))+600
                for m in range(max(start_x,0),min(end_x,1150)):
                    for n in range(max(start_y,0),min(end_y,2240)):
                        grid[n,m]=200
            elif all_loc[x,0]<all_loc[y,0] and all_loc[x,1]<all_loc[y,1]:
                start_x=int(round(all_loc[x,0]*100))+380
                start_y=int(round(all_loc[x,1]*100))+600
                end_x=int(round(all_loc[y,0]*100))+380
                end_y=int(round(all_loc[y,1]*100))+600
                for m in range(max(start_x,0),min(end_x,1150)):
                    for n in range(max(start_y,0),min(end_y,2240)):
                        grid[n,m]=200

positive=0 #accessible
negative=0 # obstacles
true_positive=0
true_negative=0
for m in range(0,1150):
    for n in range(0,2240):
        if g_truth[n,m]==200:
            negative+=1
            if grid[n,m]==0:
                true_negative+=1
        if g_truth[n,m]==0:
            positive+=1
            if grid[n,m]==200:
                true_positive+=1
print("Accessible area accuracy: ",float(true_positive/positive))
print("Obstacle area accuracy: ",float(true_negative/negative))
print("Total accuracy: ",float((true_positive+true_negative)/(positive+negative)))
plt.imshow(grid,cmap='Blues',origin='lower')
np.save("grid.npy",grid)
#plt.scatter(all_loc[:,0]*100+380,all_loc[:,1]*100+600,color = 'green',s=1)
plt.show()
