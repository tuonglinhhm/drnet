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
import statistics

npy_lst = ["track76.npy", "track77.npy", "track78.npy", "track79.npy", "track80.npy",
           "track81.npy", "track82.npy", "track83.npy", "track84.npy", "track85.npy",
           "track86.npy", "track87.npy", "track88.npy", "track89.npy", "track90.npy",
           "track91.npy", "track92.npy", "track93.npy", "track94.npy", "track95.npy",
           "track96.npy", "track97.npy", "track98.npy", "track99.npy", "track100.npy"]

choose = [1,2,3,4,5]

room = 1

pairs = 5 # const

number = [a for a in range(25)]

T_time = 60 # const

threshold = 1.0 # const

grid = np.zeros((2240, 1150), dtype=int)
g_truth = np.zeros((2240, 1150), dtype=int)
for m in range(440, 480):
    for n in range(570, 600):
        g_truth[n, m] = 200
for m in range(350, 440):
    for n in range(570, 1200):
        g_truth[n, m] = 200
for m in range(300, 350):
    for n in range(570, 600):
        g_truth[n, m] = 200
for m in range(0, 300):
    for n in range(570, 600):
        g_truth[n, m] = 200
for m in range(0, 30):
    for n in range(600, 2240):  # 5
        g_truth[n, m] = 200
for m in range(30, 230):
    for n in range(750, 850):
        g_truth[n, m] = 200
for m in range(230, 270):
    for n in range(750, 780):
        g_truth[n, m] = 200
for m in range(30, 90):
    for n in range(1110, 1170):
        g_truth[n, m] = 200
for m in range(30, 270):
    for n in range(1170, 1200):
        g_truth[n, m] = 200
for m in range(30, 180):  # 10
    for n in range(1300, 1390):
        g_truth[n, m] = 200
for m in range(180, 270):
    for n in range(1300, 1330):
        g_truth[n, m] = 200
for m in range(30, 100):
    for n in range(1500, 2040):
        g_truth[n, m] = 200
for m in range(100, 380):
    for n in range(1650, 1680):
        g_truth[n, m] = 200
for m in range(350, 380):
    for n in range(1300, 1650):
        g_truth[n, m] = 200
for m in range(100, 380):  # 15
    for n in range(1960, 1990):
        g_truth[n, m] = 200
for m in range(350, 380):
    for n in range(1760, 1960):
        g_truth[n, m] = 200
for m in range(380, 550):
    for n in range(1910, 1940):
        g_truth[n, m] = 200
for m in range(30, 350):
    for n in range(2210, 2240):
        g_truth[n, m] = 200
for m in range(350, 380):
    for n in range(2070, 2240):
        g_truth[n, m] = 200
for m in range(380, 1150):  # 20
    for n in range(2140, 2240):
        g_truth[n, m] = 200
for m in range(1050, 1150):
    for n in range(1510, 2240):
        g_truth[n, m] = 200
for m in range(630, 1050):
    for n in range(1910, 1940):
        g_truth[n, m] = 200
for m in range(830, 930):
    for n in range(1610, 1810):
        g_truth[n, m] = 200
for m in range(780, 1150):
    for n in range(1480, 1510):
        g_truth[n, m] = 200
for m in range(1120, 1150):
    for n in range(1530, 1480):  # 25
        g_truth[n, m] = 200
for m in range(780, 810):
    for n in range(1380, 1400):
        g_truth[n, m] = 200
for m in range(780, 860):
    for n in range(1330, 1380):
        g_truth[n, m] = 200
for m in range(780, 1150):
    for n in range(1230, 1330):
        g_truth[n, m] = 200
for m in range(810, 1120):
    for n in range(930, 960):
        g_truth[n, m] = 200
for m in range(1120, 1150):  # 30
    for n in range(930, 1480):
        g_truth[n, m] = 200
for m in range(780, 810):
    for n in range(600, 1000):
        g_truth[n, m] = 200
for m in range(680, 810):
    for n in range(570, 600):
        g_truth[n, m] = 200
for m in range(980, 1040):
    for n in range(960, 1110):
        g_truth[n, m] = 200
for m in range(580, 650):
    for n in range(800, 950):
        g_truth[n, m] = 200
def avg(a):
    return np.round(statistics.mean(a),6)
def sigma(a):
    return np.round(statistics.stdev(a,None),6)

def main(numbers, test1, test2, test3, test4, test5):
    for m in range(0,1150):
        for n in range(0,2240):
            ok = False
            # if numbers not over then neglet
            if numbers >= 1:
                ok = ok or (test1[n,m]==200)
            if numbers >= 2:
                ok = ok or (test2[n,m]==200)
            if numbers >= 3:
                ok = ok or (test3[n,m]==200)
            if numbers >= 4:
                ok = ok or (test4[n,m]==200)
            if numbers >= 5:
                ok = ok or (test5[n,m]==200)
            if ok:
                grid[n,m]=200

    positive = 0  # accessible
    negative = 0  # obstacles
    true_positive = 0
    true_negative = 0
    for m in range(0, 1150):
        for n in range(0, 2240):
            if g_truth[n, m] == 200:
                negative += 1
                if grid[n, m] == 0:
                    true_negative += 1
            if g_truth[n, m] == 0:
                positive += 1
                if grid[n, m] == 200:
                    true_positive += 1
    print("Accessible area accuracy: ",float(true_positive/positive))
    print("Obstacle area accuracy: ",float(true_negative/negative))
    print("Total accuracy: ",float((true_positive+true_negative)/(positive+negative)))
    # plt.imshow(grid,cmap='Blues',origin='lower')
    # np.save("result.npy",grid)
    # plt.show()
    return [float(true_positive / positive), float(true_negative / negative),float((true_positive + true_negative) / (positive + negative))]

def MAIN(choose, number,npy_list):
    print("T_time = " + str(T_time) + ", threshold = " + str(threshold))
    print("25 .npy finished")
    tot = 0
    d = {}
    for c in choose:
        random.shuffle(number) # Make sure no npy is used twice in one round
        res = []
        for i in range(pairs):
            res.append([0.0,0.0,0.0])
        for i in range(pairs):
            arr = []
            for j in range(0, c, 1):
                arr.append(npy_list[number[i*pairs+j]])
            while len(arr) < 5:
                arr.append(npy_list[number[i*pairs]])
            print(arr)
            print("We put " + str(c) + " .npy together, " + "and this is pair " + str(i) + str(" \'s result"))
            tot += 1
            res[i] = main(c,np.load(arr[0]),np.load(arr[1]),np.load(arr[2]),np.load(arr[3]),np.load(arr[4]))
            print("----------------------------------------")
        # return res
        pos = [a[0] for a in res]
        neg = [a[1] for a in res]
        mix = [a[2] for a in res]
        d[(threshold, c)] = ((avg(pos), sigma(pos)), (avg(neg), sigma(neg)), (avg(mix), sigma(mix)))
    print("tot = ", tot)
    for aa in d:
        print("Threshold " + str(aa[0]) + ",and we put : " + str(aa[1]) + " together", end="\n")
        print("Accessible area accuracy: " + "average = " + str(d[aa][0][0]) + ", standard deviation = " + str(d[aa][0][1]))
        print("Obstacle area accuracy: " + "average = " + str(d[aa][1][0]) + ", standard deviation = " + str(d[aa][1][1]))
        print("Total accuracy: " + "average = " + str(d[aa][2][0]) + ", standard deviation = " + str(d[aa][2][1]))
        print("-------------------------------------------------------------------------------------------------")

MAIN(choose, number, npy_lst)
