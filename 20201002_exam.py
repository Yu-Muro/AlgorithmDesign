# -*- coding: utf-8 -*-
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import average

class Data:
    def __init__(self):
        self.num = int(1e4)
        self.x = random.sample( range(self.num), self.num )

    def set_number(self, num):
        self.num = num
        self.x = random.sample( range(self.num), self.num )

    def quick_sort(tmp):
        if len(tmp) > 1:
            pivot = tmp.pop(-1)
            left = [i for i in tmp if i > pivot]
            right = [i for i in tmp if i < pivot]
            left = Data.quick_sort(left)
            right = Data.quick_sort(right)
            return (left + [pivot] + right)
        else:
            return tmp

    def merge_sort(List):
        if len(List) < 2:
            return List
        i = len(List) // 2
        x = Data.merge_sort(List[:i])
        y = Data.merge_sort(List[i:])
        m = []
        while x != [] and y != []:
            if x[0] < y[0]:
                m.append(y.pop(0))
            else:
                m.append(x.pop(0))
        if x != []:
            m.extend(x)
        if y != []:
            m.extend(y)
        return m

    def selection_sort(x):
        for k in range(len(x) - 1):
            for j in range(k+1, len(x)):
                if x[k] < x[j]:
                    x[k], x[j] = x[j], x[k]
        return x

    def bubble_sort(x):
        for i in range(len(x)):
            for j in range(len(x)-1-i):
                if x[j] < x[j+1]:
                    x[j], x[j+1] = x[j+1], x[j]
        return x

class Coordinate:
    def __init__(self):
        self.xlist, self.ylist = [], []

    def set_coordinate(self, x, y):
        self.xlist.append(x)
        self.ylist.append(y)

    def get_number(self):
        ymax = max(self.ylist)
        ymin = min(self.ylist)
        return ymax, ymin

    def get_std(self):
        return np.std(self.ylist)

    def get_ave(self):
        return average(self.ylist)

def print_sample(a, b, c, d):
    print(a, "sec")
    print("Max:", b, "Mid", c, "Min", d)

tmp = [10**(i+1) for i in range(5)]
for num in tmp:
    coodinate = Coordinate()
    for j in range(10): #xが同じ状況
        data = Data()
        data.set_number(num)
        start = time.time()
        data.x = Data.quick_sort(data.x)
        elapsed_time = time.time() - start
        coodinate.set_coordinate(num, elapsed_time)

        print_sample(elapsed_time, data.x[0], data.x[num//2], data.x[num-1])
    std = coodinate.get_std()
    ave = coodinate.get_ave()
    print("標準偏差", std, "平均", ave, "sec")

print("-------------------------------------------------------------------------------")

input()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#クイックソート
num = int(1e3)
coordlist = Coordinate()
for i in range(10):
    coodinate = Coordinate()
    for j in range(10): #xが同じ状況
        data = Data()
        data.set_number(num)
        start = time.time()
        data.x = Data.quick_sort(data.x)
        elapsed_time = time.time() - start
        coodinate.set_coordinate(num, elapsed_time)

        print_sample(elapsed_time, data.x[0], data.x[num//2], data.x[num-1])
    std = coodinate.get_std()
    ave = coodinate.get_ave()
    print("標準偏差", std, "平均", ave, "sec")
    y = list(coodinate.get_number())
    y.append(coodinate.get_ave())
    x = [num] * 3
    print(y)
    ax.plot(x, y, marker = "x", color = "red", linestyle = "dotted")
    coordlist.set_coordinate(num, coodinate.get_ave())
    num = int(1e4) * (i+1)
ax.plot(coordlist.xlist, coordlist.ylist, color = "red", linestyle = "solid")

#マージソート
num = int(1e3)
coordlist = Coordinate()
for i in range(10):
    coodinate = Coordinate()
    for j in range(10): #xが同じ状況
        data = Data()
        data.set_number(num)
        start = time.time()
        data.x = Data.merge_sort(data.x)
        elapsed_time = time.time() - start
        coodinate.set_coordinate(num, elapsed_time)

        print_sample(elapsed_time, data.x[0], data.x[num//2], data.x[num-1])
    std = coodinate.get_std()
    ave = coodinate.get_ave()
    print("標準偏差", std, "平均", ave, "sec")
    y = list(coodinate.get_number())
    y.append(coodinate.get_ave())
    x = [num] * 3
    print(y)
    ax.plot(x, y, marker = "x", color = "blue", linestyle = "dotted")
    coordlist.set_coordinate(num, coodinate.get_ave())
    num = int(1e4) * (i+1)
ax.plot(coordlist.xlist, coordlist.ylist, color = "blue", linestyle = "solid")

#セレクションソート
num = int(1e3)
coordlist = Coordinate()
for i in range(10):
    coodinate = Coordinate()
    for j in range(10): #xが同じ状況
        data = Data()
        data.set_number(num)
        start = time.time()
        data.x = Data.selection_sort(data.x)
        elapsed_time = time.time() - start
        coodinate.set_coordinate(num, elapsed_time)

        print_sample(elapsed_time, data.x[0], data.x[num//2], data.x[num-1])
    std = coodinate.get_std()
    ave = coodinate.get_ave()
    print("標準偏差", std, "平均", ave, "sec")
    y = list(coodinate.get_number())
    y.append(coodinate.get_ave())
    x = [num] * 3
    print(y)
    ax.plot(x, y, marker = "x", color = "green", linestyle = "dotted")
    coordlist.set_coordinate(num, coodinate.get_ave())
    num += int(1e3)
ax.plot(coordlist.xlist, coordlist.ylist, color = "green", linestyle = "solid")

#バブルソート
num = int(1e3)
coordlist = Coordinate()
for i in range(10):
    coodinate = Coordinate()
    for j in range(10): #xが同じ状況
        data = Data()
        data.set_number(num)
        start = time.time()
        data.x = Data.bubble_sort(data.x)
        elapsed_time = time.time() - start
        coodinate.set_coordinate(num, elapsed_time)

        print_sample(elapsed_time, data.x[0], data.x[num//2], data.x[num-1])
    std = coodinate.get_std()
    ave = coodinate.get_ave()
    print("標準偏差", std, "平均", ave, "sec")
    y = list(coodinate.get_number())
    y.append(coodinate.get_ave())
    x = [num] * 3
    print(y)
    ax.plot(x, y, marker = "x", color = "magenta", linestyle = "dotted")
    coordlist.set_coordinate(num, coodinate.get_ave())
    num += int(1e3)
ax.plot(coordlist.xlist, coordlist.ylist, color = "magenta", linestyle = "solid")

#メソッド
num = int(1e3)
coordlist = Coordinate()
for i in range(10):
    coodinate = Coordinate()
    for j in range(10): #xが同じ状況
        data = Data()
        data.set_number(num)
        start = time.time()
        data.x.sort(reverse = True)
        elapsed_time = time.time() - start
        coodinate.set_coordinate(num, elapsed_time)

        print_sample(elapsed_time, data.x[0], data.x[num//2], data.x[num-1])
    std = coodinate.get_std()
    ave = coodinate.get_ave()
    print("標準偏差", std, "平均", ave, "sec")
    y = list(coodinate.get_number())
    y.append(coodinate.get_ave())
    x = [num] * 3
    print(y)
    ax.plot(x, y, marker = "x", color = "yellow", linestyle = "dotted")
    coordlist.set_coordinate(num, coodinate.get_ave())
    num = int(1e4) * (i+1)
ax.plot(coordlist.xlist, coordlist.ylist, color = "yellow", linestyle = "solid")

ax.set_ylim(top = 5)
ax.set_title("Sort Time")
ax.set_xlabel("Number of data")
ax.set_ylabel("Time")
ax.grid(True)
plt.show()