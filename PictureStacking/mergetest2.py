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

grid = np.zeros((960, 1230), dtype=int)
g_truth = np.zeros((960, 1230), dtype=int)
for m in range(170, 200):
    for n in range(330, 960):
        g_truth[n, m] = 200
for m in range(170, 1230):
    for n in range(930, 960):
        g_truth[n, m] = 200
for m in range(1000, 1230):
    for n in range(0, 960):
        g_truth[n, m] = 200
for m in range(170, 1230):
    for n in range(0, 30):
        g_truth[n, m] = 200
for m in range(1130, 1200):
    for n in range(30, 330):
        g_truth[n, m] = 200
for m in range(400, 1200):
    for n in range(160, 530):
        g_truth[n, m] = 200
for m in range(200, 270):
    for n in range(630, 930):
        g_truth[n, m] = 200
for m in range(400, 500):
    for n in range(630, 930):
        g_truth[n, m] = 200
for m in range(700, 800):
    for n in range(630, 930):
        g_truth[n, m] = 200
for m in range(1000, 1100):
    for n in range(630, 930):
        g_truth[n, m] = 200
def avg(a):
    return np.round(statistics.mean(a),6)
def sigma(a):
    return np.round(statistics.stdev(a,None),6)

def main(numbers, test1, test2, test3, test4, test5):
    for m in range(0,1230):
        for n in range(0,960):
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
    for m in range(0, 1230):
        for n in range(0, 960):
            if m > 170 or n < 230:
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
